#ifndef __PYX_HAVE__numba__numbawrapper
#define __PYX_HAVE__numba__numbawrapper


#ifndef __PYX_HAVE_API__numba__numbawrapper

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

__PYX_EXTERN_C DL_IMPORT(PyObject) *Create_NumbaUnboundMethod(PyObject *, PyObject *);

#endif /* !__PYX_HAVE_API__numba__numbawrapper */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initnumbawrapper(void);
#else
PyMODINIT_FUNC PyInit_numbawrapper(void);
#endif

#endif /* !__PYX_HAVE__numba__numbawrapper */
