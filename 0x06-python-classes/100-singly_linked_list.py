#!/usr/bin/python3
""" Defines a node of a singly linked List """


class Node:
    """ Creates a node """

    def __init__(self, data, next_node=None):
        """
        Initializes a node

        Args:
            data(int): Nodes data
            next_node(obj): next node
        """
        self.__data = data
        self.__next_node = next_node

        if type(data) != int:
            raise TypeError("data must be an integer")

        if type(next_node) != object or next_node != None:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """ Gets data """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets new data value

        Args:
            value(int): New data of node
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Retrieves node """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets new next node

        Args:
            value(obj): new next_node value
        """
        if type(value) != object or value != None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


""" Singly linked list """


class SinglyLinkedList:
    """ Creates a singly linked list """

    def __init__(self):
        """ Initializes singly linked list """
        self.__head = None

    def sorted_insert(self, value):
        """
        Sorts nodes 

        Args:
            value: values to sort
        """
