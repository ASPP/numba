from __future__ import print_function
import numba.unittest_support as unittest
import numpy as np
from numba.compiler import compile_isolated, Flags
from numba import types
from numba.pythonapi import NativeError

def setitem_slice(a, start, stop, step, scalar): 
    a[start:stop:step] = scalar


def usecase(obs, nPoints, B, sigB, A, sigA, M, sigM):
    center = nPoints / 2
    print(center)
    obs[0:center] = np.arange(center)
    obs[center] = 321
    obs[(center + 1):] = np.arange(nPoints - center - 1)


class TestStoreSlice(unittest.TestCase):
    def test_usecase(self):
        n = 10
        obs_got = np.zeros(n)
        obs_expected = obs_got.copy()

        flags = Flags()
        flags.set("enable_pyobject")
        cres = compile_isolated(usecase, (), flags=flags)
        cres.entry_point(obs_got, n, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0)
        usecase(obs_expected, n, 10.0, 1.0, 2.0, 3.0, 4.0, 5.0)

        print(obs_got, obs_expected)
        self.assertTrue(np.allclose(obs_got, obs_expected))

    def test_array_slice_setitem(self):
        n = 10
        cres = compile_isolated(setitem_slice, (types.int64[:], types.int64, types.int64, types.int64, types.int64))
        a = np.arange(n, dtype=np.int64)
        # tuple is (start, stop, step, scalar)
        tests = ((2, 6, 1, 7),
                (2, 6, -1, 7),
                (-2, len(a), 2, 77),
                (-2, 2 * len(a), 2, 77),
                (-2, -6, 3, 88),
                (-2, -6, -3, 9999),
                (-6, -2, 4, 88),
                (-6, -2, -4, 88),
                (16, 20, 2, 88),
                (16, 20, -2, 88),
                )

        for start, stop, step, scalar in tests:
            a = np.arange(n, dtype=np.int64)
            b = np.arange(n, dtype=np.int64)
            cres.entry_point(a, start, stop, step, scalar)
            setitem_slice(b, start, stop, step, scalar)
            self.assertTrue(np.allclose(a, b))
        
        #test if step = 0
        a = np.arange(n, dtype=np.int64)
        b = np.arange(n, dtype=np.int64)
        with self.assertRaises(NativeError):
            cres.entry_point(a, 3, 6, 0, 88)
   

if __name__ == '__main__':
    unittest.main()

