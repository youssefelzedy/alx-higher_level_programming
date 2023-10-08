#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *current;
	listint_t *first_half;
	listint_t *last_half;
	listint_t *middle;
	int size, i;

	first_half = last_half = *head;
	size = i = 0;

	if (*head == NULL)
		return (1);
	
	size++;

	while (first_half->next != NULL && first_half->next->next != NULL)
	{
		first_half = first_half->next->next;
		last_half = last_half->next;
		size++;
	}

	middle = first_half->next;
	last_half = first_half->next;

	while (middle != NULL && middle->next != NULL)
	{
		current = middle->next;
		middle->next = middle->next->next;
		current->next = last_half;
		last_half = current;
	}

	first_half->next = last_half;
	first_half = *head;

	for (i = 0; i < size && last_half != NULL; i++)
	{
		if (first_half->n != last_half->n)
			return (0);
		first_half = first_half->next;
		last_half = last_half->next;
	}
	return (1);
}