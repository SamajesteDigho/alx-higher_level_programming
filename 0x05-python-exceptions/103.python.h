#ifndef CPYTHON
#define CPYTHON

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

#endif /* CYPYTHON */
