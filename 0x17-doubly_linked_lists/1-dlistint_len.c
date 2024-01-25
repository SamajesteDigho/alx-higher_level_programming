#include "lists.h"
/**
 * dlistint_len - Count nodes
 * @h: Header of the list
 * Desription: Get the number of nodes in the list
 * Return: Number of elements in the list
*/
size_t dlistint_len(const dlistint_t *h)
{
int node_count;
const dlistint_t *tmp;
tmp = h;
node_count = 0;
while (tmp != NULL)
{
tmp = tmp->next;
node_count++;
}
return (node_count);
}
