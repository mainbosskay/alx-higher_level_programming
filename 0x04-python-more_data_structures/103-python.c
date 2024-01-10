#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Printing basic info of python bytes info
 * @p: pointer
 * Return: it is void
 */

void print_python_bytes(PyObject *p)
{
	char *string;
	long int k;
	long int t;
	long int limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	k = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", k);
	printf("  trying string: %s\n", string);
	if (k >= 10)
		limit = 10;
	else
		limit = k + 1;
	printf("  first %ld bytes:", limit);
	for (t = 0 ; t < limit ; t++)
		if (string[t] >= 0)
			printf(" %02x", string[t]);
		else
			printf(" %02x", 256 + string[t]);
	printf("\n");
}

/**
 * print_python_list - Printing basic info of python list info
 * @p: pointer
 * Return: it is void
 */

void print_python_list(PyObject *p)
{
	long int k;
	long int t;
	PyListObject *list;
	PyObject *object;

	k = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", k);
	printf("[*] Allocated = %ld\n", list->allocated);
	for (t = 0 ; t < k ; t++)
	{
		object = ((PyListObject *)p)->ob_item[t];
		printf("Element %ld: %s\n", t, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
}
