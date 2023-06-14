#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to a PyObject representing the Python list
 *
 * This function prints the size of the Python list, the number of allocated
 * elements, and the type of each element in the list.
 */
void print_python_list(PyObject *p)
{
long int size, i;
PyListObject *list = (PyListObject *)p;

printf("[*] Python list info\n");
if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", list->allocated);
for (i = 0; i < size; i++)
printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
}

void print_python_bytes(PyObject *p)
{
long int size, i;
PyBytesObject *bytes = (PyBytesObject *)p;
char *str;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = bytes->ob_sval;
printf("  size: %ld\n", size);
printf("  trying string: %s\n", str);
if (size < 10)
printf("  first %ld bytes:", size + 1);
else
printf("  first 10 bytes:");
for (i = 0; i <= size && i < 10; i++)
printf(" %02x", str[i] & 0xff);
printf("\n");
}
