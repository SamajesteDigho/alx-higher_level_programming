#include "lists.h"
/**
 * sum_dlistint - Add all node
 * @head: Head of the list
 * Desription: Add the values of all the nodes in a list
 * Return: Sum of node values
*/
int sum_dlistint(dlistint_t *head)
{
dlistint_t *tmp;
int sum;
sum = 0;
tmp = head;
while (tmp != NULL)
{
sum += tmp->n;
tmp = tmp->next;
}
return (sum);
}
