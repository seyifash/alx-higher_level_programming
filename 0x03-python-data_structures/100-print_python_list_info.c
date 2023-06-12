#include <Python.h>
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
	printf("[*] Size of the Python List = %ld\n", infolist->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", infolist->allocated);
	for (i = 0; i < infolist->ob_base.ob_size; i++)
	{
		printf("Element %d: ", i);
		printf("%s\n", infolist->ob_item[i]->ob_type->tp_name);
	}
}
