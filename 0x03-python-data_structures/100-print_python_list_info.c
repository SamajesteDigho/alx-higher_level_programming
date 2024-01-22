#define _PyObject_HEAD_EXTRA
#include <stdio.h>

typedef struct _object {
    _PyObject_HEAD_EXTRA
    struct _typeobject *ob_type;
} PyObject;
typedef struct _object
{
    long int ob_size;
    long int allocated;
    struct _object ob_item[5];
    struct _object *ob_base;
} PyListObject;

void print_python_list_info(PyObject *p)
{
    int i;
    PyListObject *pp;
    pp = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", pp->ob_base->ob_size);
    printf("[*] Allocated = %ld\n", pp->allocated);
    for (i = 0; i < pp->ob_base->ob_size; i++)
    {
        printf("Element %d: %s\n", i, pp->ob_item[i]->ob_type->tp_name);
    }
}
