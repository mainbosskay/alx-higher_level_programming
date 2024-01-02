#include "lists.h"

/**
 * check_cycle - Checking if a singly linked list has a cycle using C function
 * @list: pointer to linked list
 * Return: 1 if there is cycle else 0
 */

int check_cycle(listint_t *list)
{
	listint_t *green;
	listint_t *red;

	if (!list)
	{
		return (0);
	}
	green = list->next;
	red = list;
	while (green != NULL && green->next != NULL && red != NULL)
	{
		if (green == red)
		{
			return (1);
		}
		green = green->next->next;
		red = red->next;
	}
	return (0);
}
