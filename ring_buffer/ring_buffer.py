from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        # UPER
        # U - UNDERSTAND
        #     ring buffer is a non-growable buffer with a fixed size
        #     When the ring buffer is full and a new element is inserted,
        #     the oldest element in the ring buffer is overwritten with the newest element

    def append(self, item):
        # DO FIRST - SO I CAN HAVE SOMETHING TO get
        # P - Plan
        if value < self.value:
        #     append adds item to ring buffer
        #     if ring buffer is full:         =====> $$$$$ fix value for at_capacity $$$$$$$
            at_capacity = True
            if at_capacity == True:
        #         oldest element in ring = item
                self.storage[0] == item
            else:
        #         add item to ring buffer
                self.storage.insert_after(item)
        #

        pass

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # AFTER APPEND TESTS PASS


        return list_buffer_contents





















































# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
