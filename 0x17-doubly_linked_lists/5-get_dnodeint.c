#include "lists.h"
/**
 * get_dnodeint_at_index - Get node at given position
 * @head: Head of the list
 * @index: index of the node to return
 * Desription: Collect the node at a given index
 * Return: Node at a given inde or NULL otherwise
*/
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
dlistint_t *tmp;
unsigned int count;
count = 0;
tmp = head;
while (tmp != NULL)
{
if (count == index)
{
return (tmp);
}
tmp = tmp->next;
count++;
}
return (NULL);
}
