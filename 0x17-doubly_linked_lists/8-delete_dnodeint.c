#include "lists.h"
/**
 * delete_dnodeint_at_index - delete node
 * @head: Head of list
 * @index: Index of node to be delete
 * Desription: Deletes a node at the given index
 * Return: 1 if succeded and -1 otherwise
*/
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
dlistint_t *tmp, *del;
unsigned int count;
count = 0;
tmp = *head;
if (tmp == NULL)
{
return (-1);
}
if (index == 0)
{
del = *head;
*head = del->next;
del->next = NULL;
free(del);
return (1);
}
while (tmp != NULL && count < index)
{
tmp = tmp->next;
count++;
}
if (tmp == NULL)
{
return (-1);
}
del = tmp;
tmp = tmp->prev;
tmp->next = del->next;
del->next->prev = tmp;
del->next = NULL;
del->prev = NULL;
free(del);
return (1);
}
