#include "lists.h"

/**
 * rev_listint - Reversing a linked list
 * @head: pointer
 * Return: pointer to the head of the reversed list
 */

void rev_listint(listint_t **head)
{
	listint_t *previousnode = NULL;
	listint_t *newnode = *head;
	listint_t *nextnode = NULL;

	while (newnode)
	{
		nextnode = newnode->next;
		newnode->next = previousnode;
		previousnode = newnode;
		newnode = nextnode;
	}
	*head = previousnode;
}

/**
 * is_palindrome - Checking a linked list if it is a palindrome
 * @head: pointer
 * Return: either 1 if its a palindrome and 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *red = *head;
	listint_t *green = *head;
	listint_t *temptr = *head;
	listint_t *reverselist = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (1)
	{
		green = green->next->next;
		if (green == NULL)
		{
			reverselist = red->next;
			break;
		}
		if (green->next == NULL)
		{
			reverselist = red->next->next;
			break;
		}
		red = red->next;
	}
	rev_listint(&reverselist);
	while (reverselist && temptr)
	{
		if (temptr->n == reverselist->n)
		{
			reverselist = reverselist->next;
			temptr = temptr->next;
		}
		else
			return (0);
	}
	if (reverselist == NULL)
		return (1);
	return (0);
}
