#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

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
		last_half = last_half->next;
		first_half = first_half->next->next;
		size++;
	}

	middle = last_half->next;
	last_half = last_half->next;

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