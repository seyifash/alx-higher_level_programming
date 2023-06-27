#!/usr/bin/python3
"""Defines a class for singly linked list"""


class Node:
    """Represnts the class node"""
    def __init__(self, data, next_node=None):
        """initialise the data and nextnode
        Args:
        data(int): the new data to be added to the list
        nexnode(node): the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Represent a class for a singly linked list"""

    def __init__(self):
        """initializes the head of the list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        Thelist = []
        temp = self.__head
        while temp is not None:
            Thelist.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(Thelist))
