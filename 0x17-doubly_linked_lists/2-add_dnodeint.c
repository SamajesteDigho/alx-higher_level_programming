#include "lists.h"
/**
 * add_dnodeint - add node at head
 * @head: Head of the list
 * @n: Value of the node to be created
 * Desription: This function permits to add a node at the head
 * Return: A pointer of the newly created node
*/
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
dlistint_t *new;
new = (dlistint_t *)malloc(sizeof(dlistint_t));
if (new == NULL)
{
return (NULL);
}
new->n = n;
new->prev = NULL;
new->next = NULL;
if (*head == NULL)
{
*head = new;
return (new);
}
new->next = *head;
*head = new;
return (new);
}
