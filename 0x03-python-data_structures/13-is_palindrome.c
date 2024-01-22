#include "lists.h"
/**
 * is_palindrome - Determines if palindrome
 * @head: The list to determine
 * Description: This function permits to determine if list is a palindrome.
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head){
    listint_t *tmp, *tmp2, *fh, *sh, *front, *back;
    int count, i;

    count = 0;
    tmp = *head;
    /* Counting the elements in the list */
    while (tmp != NULL)
    {
        count++;
        tmp = tmp->next;
    }
    /* If the list is empty or there is only one element */
    if(count == 0 || count == 1)
    {
        return (1);
    }
    /* reating a list of the 2 halfs */
    tmp = *head;
    fh = NULL;
    sh = NULL;
    i = 0;
    while (tmp != NULL)
    {
        if(i < (count + 1) / 2) {
            add_nodeint_end(&fh, tmp->n);
        }
        else {
            add_nodeint_end(&sh, tmp->n);
        }
        tmp = tmp->next;
        i++;
    }
    /* Reverse second list */
    front = sh;
    back = NULL;
    while (front != NULL)
    {
        tmp = front;
        front = front->next;
        tmp->next = back;
        back = tmp;
    }
    sh = back;
    /* Comparing the 2 halfs */
    tmp = fh;
    tmp2 = sh;
    while (tmp2 != NULL)
    {
        if (tmp->n != tmp2->n)
        {
            free_listint(fh);
            free_listint(sh);
            return (0);
        }
        tmp = tmp->next;
        tmp2 = tmp2->next;
    }
    free_listint(fh);
    free_listint(sh);
    return (1);
}