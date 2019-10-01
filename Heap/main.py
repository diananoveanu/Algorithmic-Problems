from heap import Heap


def relation(a, b):
    if a <= b:
        return True
    return False


def min(a, b):
    if a <= b:
        return a
    return b


def test_heap():
    heap = Heap(relation)
    lst = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    for elem in lst:
        heap.add(elem)
    print(heap.get_heap())

    for elem in lst:
        heap.delete(0)
        print(heap.get_heap())



def main():
    test_heap()


main()
