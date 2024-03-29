#include "lists.h"
/**
 * check_cycle - Check Cycle function
 * @list: The list object to check
 * Description: This function permits to chek if a list cyclic or not.
 * Return:  1 or 0
*/
int check_cycle(listint_t *list)
{
listint_t *tmp, *cur, *back;
int cycle;
tmp = list;
cur = list;
cycle = 0;
while (cur != NULL)
{
back = cur;
cur = cur->next;
if (cur == tmp || (cur != NULL && cur->n > back->n)) {
cycle = 1;
break;
}
}
return (cycle);
}
