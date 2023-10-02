#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head of list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
    listint_t *slow, *fast;

    if (list == NULL || list->next == NULL)
        return (0);

    slow = list;
    fast = list->next;

    while (fast != NULL && fast->next != NULL)
    {
        if (fast == slow)
            return (1);

        slow = slow->next;
        fast = fast->next->next;
    }

    return (0);
}