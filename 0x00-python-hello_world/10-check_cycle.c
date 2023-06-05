#include "lists.h"
/**
 * check_cycle - function that checks if a singly linked list has a cycle in it
 * @list: pointer to the beginning of thenode
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *currentlist, *checklist;

	if (list == NULL || list->next == NULL)
	return (0);
	currentlist = list;
	checklist = list->next;

	while (currentlist != NULL && checklist != NULL &&
	checklist->next != NULL)
	{
	if (currentlist == checklist)
	{
		return (1);
	}
		currentlist = currentlist->next;
		checklist = checklist->next->next;
	}
	return (0);
}
