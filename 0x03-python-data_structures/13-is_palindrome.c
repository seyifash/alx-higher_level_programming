#include "lists.h"
#include <stdio.h>
/**
 * is_palindrome - checks if a singly linked list is a plaindrome
 * @head: the head pointer
 *
 * Return: returns 1 if is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	int length = 0, middle = 0, i;
	listint_t *current = *head;
	listint_t *prev = NULL, *next = NULL;

	while (current != NULL)
	{
	length++;
	current = current->next;
	}
	middle = length / 2;
	current = *head;
	for (i = 0; i < middle; i++)
	{
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
	}
	if (length % 2 != 0)
	{
	current = current->next;
	}
	while (current != NULL && prev != NULL)
	{
	if (current->n != prev->n)
	{
	return (0);
	}
	current = current->next;
	prev = prev->next;
	}

	return (1);
}
