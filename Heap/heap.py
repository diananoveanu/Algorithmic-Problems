class Heap:
    """
    Class for representing a heap
    """

    def __init__(self, relation):
        """
        Heap constructor
        :param relation: heap relation
        """
        self.__relation = relation

        self.__heap = []  # list to store the elements

    def add(self, element):
        """
        Function to add an element into the heap
        :param element:
        :return:
        """
        if len(self.__heap) == 0:
            self.__heap.append(element)
        else:
            self.__heap.append(element)
            start_pos = len(self.__heap) - 1
            parent_pos = self.__get_parent(start_pos)
            while parent_pos is not None and not self.__relation(self.__heap[parent_pos], self.__heap[start_pos]):
                self.__heap[parent_pos], self.__heap[start_pos] = self.__heap[start_pos], self.__heap[parent_pos]
                start_pos = parent_pos
                parent_pos = self.__get_parent(parent_pos)

    def delete(self, pos):
        """
        Function to delete the top element of a heap
        :return: the top element
        """
        if len(self.__heap) == 0:
            self.__heap = []
        to_ret = self.__heap[pos]
        self.__heap[pos] = self.__heap[len(self.get_heap()) - 1]
        del self.__heap[len(self.__heap) - 1]
        self.__heapify(pos)
        return to_ret

    def __heapify(self, pos):
        """

        :param pos:
        :return:
        """
        l = self.__get_left_child(pos)
        r = self.__get_right_child(pos)

        if l < len(self.__heap) and self.__heap[l] < self.__heap[pos]:
            largest = l
        else:
            largest = pos

        if r < len(self.__heap) and self.__heap[r] < self.__heap[largest]:
            largest = r
        if largest != pos:
            self.__heap[pos],self.__heap[largest] = self.__heap[largest], self.__heap[pos]
            self.__heapify(largest)


    def __get_parent(self, pos):
        """
        Function to return the parent of a node in heap
        :param pos: position of element in heap list
        :return: index of parent
        """

        val = (pos - 1) // 2
        if val < 0:
            return None
        return val

    def __get_left_child(self, pos):
        """
        Function to get the left child of a node
        :param pos: position of the current node
        :return: index of left child
        """
        return 2 * pos + 1

    def __get_right_child(self, pos):
        """
        Function to get the right child of a node
        :param pos: position of the current node
        :return: index of right chi;d
        """
        return 2 * pos + 2

    def get_top(self):
        """
        Function to get the top element from the heap
        :return: the element
        """
        return self.__heap[0]

    def get_heap(self):
        return self.__heap
