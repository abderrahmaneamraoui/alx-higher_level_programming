#include "lists.h"
/**
* is_palindrome - checks if a singly linked list is a palindrome
* @head: pointer to pointer to head of list
* Return: 0 if not a palindrome, 1 if a palindrome
*/
int is_palindrome(listint_t **head)
{
listint_t *node = *head;
int i, j, len = 0;
int arr[10000]; /* maximum size of linked list */

if (node == NULL || node->next == NULL)
return (1);

while (node != NULL)
{
arr[len++] = node->n;
node = node->next;
}

for (i = 0, j = len - 1; i <= j; i++, j--)
{
if (arr[i] != arr[j])
return (0);
}

return (1);
}
