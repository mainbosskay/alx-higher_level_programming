#include "Python.h"

/**
 * print_python_string - Printing python string
 * @p: pointer to the PyObject
 * Return: it is void
 */

void print_python_string(PyObject *p)
{
	long int strlength;

	fflush(stdout);
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	strlength = ((PyASCIIObject *)(p))->length;
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", strlength);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &strlength));
}
