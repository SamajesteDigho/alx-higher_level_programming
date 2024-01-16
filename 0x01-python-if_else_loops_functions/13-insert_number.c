#include <stdlib.h>
#include <stdio.h>
#include "lists.h"
/**
 * insert_node - Inserting node function
 * @head: The pointer on the list head
 * @number: The value to add as node
 * Description: This function permits to add a node to the tail.
 * Return: The address of the new node node or NULL in case of failure.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *prev;
listint_t *cur;
listint_t *new;
new = (listint_t *)malloc(sizeof(listint_t));
if (new == NULL)
{
printf("Finished here\n");
return (NULL);
}
new->n = number;
new->next = NULL;
prev = *head;
if ( prev == NULL) {
prev = new;
return (new);
}
if (prev->next == NULL) {
prev->next = new;
return (new);
}
while (prev != NULL && prev->next != NULL)
{
cur = prev->next;
if (cur != NULL && cur->n > new->n)
{
prev->next = new;
new->next = cur;
return (new);
}
prev = prev->next;
}
prev->next = new;
return (new);
}
