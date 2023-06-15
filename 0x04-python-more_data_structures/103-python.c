#include <Python.h>
#include <stdio.h>
/**
 * print_python_bytes - prints basic infro about a python byte object
 * @p: the pyobject list
 *
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(p))->ob_size;
	string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
	limit = 10;
	else
	limit = size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	if (string[i] >= 0)
	printf(" %02x", string[i]);
	else
	printf(" %02x", 256 + string[i]);

	printf("\n");
}

/**
 * print_python_list_info - prints basic infoo about python lists.
 * @p: the pyObject list.
 *
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *infolist;
	int i;

	infolist = (PyListObject *)p;
	printf("[*] Python list info");
	printf("[*] Size of the Python List = %ld\n", infolist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", infolist->allocated);
	for (i = 0; i < infolist->ob_base.ob_size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", infolist->ob_item[i]->ob_type->tp_name);
		if (PyBytes_Check(infolist->ob_item[i]))
		{
		printf("Printing bytes object:\n");
		print_python_bytes(infolist->ob_item[i]);
	}
	}
}
