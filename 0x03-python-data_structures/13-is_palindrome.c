#include "lists.h"
#include <stdio.h>
/**
 * reverse - reverses a singly linke list
 * @head: pointer to the first node in the list
 *
 * Return: returns the reversed list
 */
listint_t *reverse(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
	next = current->next;
	current->next = prev;
	prev = current;
	current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a plaindrome
 * @head: the head pointer
 *
 * Return: returns 1 if is palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *original = *head;
	listint_t *reversed = reverse(head);

	while (original != NULL && reversed != NULL)
	{
	if (original->n != reversed->n)
	{
	return (0);
	}
	original = original->next;
	reversed = reversed->next;
	}
	return (1);
}
