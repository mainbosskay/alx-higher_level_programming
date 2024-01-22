#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - Printing PyFloatObject info
 * @p: pointer to the PyObject that represents a PyFloatObject
 * Return: it is void
 */

void print_python_float(PyObject *p)
{
	double floatva = 0;
	char *floatstr = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	floatva = ((PyFloatObject *)p)->ob_fval;
	floatstr = PyOS_double_to_string(floatva, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", floatstr);
}

/**
 * print_python_bytes - Printing PyBytesObject info
 * @p: pointer to the PyObject that represents a PyBytesObject
 * Return: it is void
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t bytsize = 0, k = 0;
	char *bytstring = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bytsize = PyBytes_Size(p);
	printf("  size: %zd\n", bytsize);
	bytstring = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", bytstring);
	printf("  first %zd bytes:", bytsize < 10 ? bytsize + 1 : 10);
	while (k < bytsize + 1 && k < 10)
	{
		printf(" %02hhx", bytstring[k]);
		k++;
	}
	printf("\n");
}

/**
 * print_python_list - Printing PyListObject info
 * @p: pointer to the PyObject that represents a PyListObject
 * Return: it is void
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t lsize = 0;
	PyObject *litem;
	int k = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		lsize = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", lsize);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (k < lsize)
		{
			litem = PyList_GET_ITEM(p, k);
			printf("Element %d: %s\n", k, litem->ob_type->tp_name);
			if (PyBytes_Check(litem))
				print_python_bytes(litem);
			else if (PyFloat_Check(litem))
				print_python_float(litem);
			k++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
