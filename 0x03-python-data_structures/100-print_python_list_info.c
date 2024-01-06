#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Printing some basic info about python lists
 * @p: pointer
 * Return: it is void
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int k;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", obj->allocated);
	for (k = 0 ; k < size ; k++)
		printf("Element %d: %s\n", k, Py_TYPE(obj->ob_item[k])->tp_name);
}
