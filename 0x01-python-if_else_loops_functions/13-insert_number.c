#include "lists.h"
#include <stdlib.h>
/**
 * insert_node
 * @head: A pointer to the haed of the linked list
 * @number: the number to be inserted
 * Return: returns new node or null if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
	new_node->next = *head;
	*head = new_node;
	}
	else
	{
	current = *head;
	while (current->next != NULL && current->next->n < number)
	{
	current = current->next;
	}
	new_node->next = current->next;
	current->next = new_node;
	}
	return (new_node);
}
