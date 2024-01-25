#include "lists.h"
/**
 * add_dnodeint_end - Adding node at the end
 * @head: Head of the list
 * @n: Value of the node to create
 * Desription: Add a new node at the end of a doubly linked list
 * Return: A pointer to the newly created node
*/
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
dlistint_t *new, *tmp;
new = (dlistint_t *)malloc(sizeof(dlistint_t));
if (new == NULL)
{
return (NULL);
}
new->n = n;
new->next = NULL;
new->prev = NULL;
if (*head == NULL)
{
*head = new;
return (new);
}
tmp = *head;
while (tmp->next != NULL)
{
tmp = tmp->next;
}
tmp->next = new;
new->prev = tmp;
return (new);
}
