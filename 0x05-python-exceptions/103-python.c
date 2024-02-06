#include "103.python.h"
/**
 * print_python_list - Python List Info
 * @p: PyObject
 * Description: Here the description
*/
void print_python_list(PyObject *p)
{
Py_ssize_t i;
Py_ssize_t length = PyList_Size(p);
size_t all_size = (size_t)PyObject_Size(p);

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object.\n");
return;
}
printf("[*] Size of the Python List = %ld\n", length);
printf("[*] Allocated = %zu\n", all_size);
for (i = 0; i < length; i++)
{
PyObject *element = PyList_GetItem(p, i);
PyObject *type = PyObject_Type(element);

printf("Element %ld: %s\n", i, Py_TYPE(type)->tp_name);
}
}

/**
 * print_python_bytes - Python Bytes Info
 * @p: PyObject
 * Description: Here the description
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size = PyBytes_Size(p);
int dist = (int)size > 10 ? 10 : (int)size;

printf("[.] bytes object info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid Bytes Object.\n");
return;
}
printf("  size: %d\n", size);
printf("  trying string: %s\n", "??");
printf("  first %d bytes: \n", dist);
for (Py_ssize_t i = 0; i < dist; ++i)
printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
printf("\n");
}

/**
 * print_python_float - Float Info
 * @p: PyObject
 * Description: Here the description
*/
void print_python_float(PyObject *p)
{
double value;
printf("[.] float object info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}
value = PyFloat_AsDouble(p);
printf("  value: %f\n", value);
}
