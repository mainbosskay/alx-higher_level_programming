#include "lists.h"

/**
 * insert_node - Inserting a number into a sorted singly linked list using C
 * @head: pointer
 * @number: numberto be added
 * Return: address of new node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cnode = *head;
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	if (cnode == NULL || cnode->n >= number)
	{
		newnode->next = cnode;
		*head = newnode;
		return (newnode);
	}
	while (cnode && cnode->next && cnode->next->n < number)
		cnode = cnode->next;
	newnode->next = cnode->next;
	cnode->next = newnode;

	return (newnode);
}
