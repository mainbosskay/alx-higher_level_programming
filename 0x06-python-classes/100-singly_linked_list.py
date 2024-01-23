#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list"""


class Node:
    """Singly-linked list node represented"""
    def __init__(self, data, next_node=None):
        """Initializing the node class
        Args: data (int): data of the node
        next_node (Node): next node of the node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Gets and returns the current data of the node"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Setting the node data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets and returns the next node of the node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """Setting the next node of the node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly-linked list represented"""
    def __init__(self):
        """Initializing a singlylinkedlist"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node to singlylinked list at the correct
        ordered index position
        Args: value (Node): the node to insert"""
        newnode = Node(value)
        if self.__head is None:
            newnode.next_node = None
            self.__head = newnode
        elif self.__head.data > value:
            newnode.next_node = self.__head
            self.__head = newnode
        else:
            tempnode = self.__head
            while (tempnode.next_node is not None and
                    tempnode.next_node.data < value):
                tempnode = tempnode.next_node
            newnode.next_node = tempnode.next_node
            tempnode.next_node = newnode

    def __str__(self):
        """Returns a string representation of the singlylinkedlist"""
        values = []
        tempnode = self.__head
        while tempnode is not None:
            values.append(str(tempnode.data))
            tempnode = tempnode.next_node
        return ('\n'.join(values))
