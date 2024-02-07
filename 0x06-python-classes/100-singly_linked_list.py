#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Node Object module
In this module we define the node class for managing singly
linked lists
"""


class Node:
    """The Node Object class
    Note:
        This class represents an element in a singly linked list
    """

    def __init__(self, data, next_node=None):
        """Constructor for an instance of the Node class
        Args:
            data: Data of the node
            next_node: Address to next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for the data property"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for the data property"""
        if type(value) is not type(0):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter for the next_node property"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for the next_node property"""
        if value is not None and type(value) is not type(self):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """The SinglyLinkedList Object class
    Note:
        This class represents a singly linked list
    """

    def __init__(self):
        """Constructor for an instance of the SinglyLinkedList class"""
        self.__head = None

    def __str__(self):
        """String representation of the SinglyLinkedList"""
        tmp: Node = self.__head
        string = ""
        while tmp is not None:
            string += "{}\n".format(tmp.data)
            tmp = tmp.next_node
        return string[:-1]

    def sorted_insert(self, value):
        """ Inserting a new node in the linked list at a right position
        Args:
            value: Data value of the node to be inserted
        """
        new: Node = Node(data=value)
        tmp: Node = self.__head
        if tmp is None:
            self.__head = new
        elif tmp.next_node is None:
            if tmp.data < value:
                tmp.next_node = new
            else:
                new.next_node = tmp
                self.__head = new
        else:
            if value < tmp.data:
                new.next_node = tmp
                self.__head = new
            else:
                while tmp.next_node is not None and tmp.next_node.data < value:
                    tmp = tmp.next_node
                if tmp.next_node is None:
                    tmp.next_node = new
                else:
                    new.next_node = tmp.next_node
                    tmp.next_node = new
