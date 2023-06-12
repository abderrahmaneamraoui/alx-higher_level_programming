#include "lists.h"

/**
* is_palindrome - checks if a singly linked list is a palindrome.
* @head: double pointer to the head of the list.
*
* Return: 1 if the list is a palindrome, 0 otherwise.
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *curr = *head;
listint_t *next = NULL;

while (fast && fast->next)
{
fast = fast->next->next;
next = curr->next;
curr->next = prev;
prev = curr;
curr = next;
}

if (fast != NULL)
{
slow = slow->next;
}

while (prev != NULL)
{
if (prev->n != slow->n)
{
return (0);
}
prev = prev->next;
slow = slow->next;
}

return (1);
}
