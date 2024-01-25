#include "lists.h"
/**
 * free_dlistint - Free list
 * @head: Head of the list
 * Desription: Permits to clear completely a list
*/
void free_dlistint(dlistint_t *head)
{
dlistint_t *cur, *next;
cur = head;
while (cur != NULL)
{
next = cur->next;
cur->next = NULL;
cur->prev = NULL;
free(cur);
cur = next;
}

}
