#include "lists.h"
/**
 * print_dlistint - print a list
 * @h: Head of a doubly linked list
 * Desription: Takes a list as parameter and print all its content
 * Return: Number of nodes
*/
size_t print_dlistint(const dlistint_t *h)
{
int node_count;
const dlistint_t *tmp;
tmp = h;
node_count = 0;
while (tmp != NULL)
{
printf("%d\n", tmp->n);
tmp = tmp->next;
node_count++;
}
return (node_count);
}
