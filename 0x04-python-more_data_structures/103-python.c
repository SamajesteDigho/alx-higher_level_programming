#include "cpython_core.h"

void print_python_list(PyObject *p)
{
    Py_ssize_t i;
    Py_ssize_t length = PyList_Size(p);
    size_t all_size = (size_t) PyObject_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", length);
    printf("[*] Allocated = %zu\n", all_size);
    for (i = 0; i < length; i++)
    {
        PyObject *element = PyList_GetItem(p, i);
        PyObject *type = PyObject_Type(element);
        printf("Element %ld: %s\n", i, Py_TYPE(type)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    printf("  size: %d\n", 5);
    printf("  trying string: %d\n", 5);
    printf("  first %d bytes: \n", 6);
}