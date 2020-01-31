from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # print(item)
        if self.capacity == len(self.storage):
            if self.current is None:
                self.current = self.storage.tail
            self.current.value = item
            # If there is a previous, then set the previous as the current, else set to tail
            if self.current.prev:
                self.current = self.current.prev
            else:
                self.current = self.storage.tail
        # if it hasn't reached the capacity then add the item to the head
        elif len(self.storage) < self.capacity:
            self.storage.add_to_head(item)



    def get(self):
        list_buffer_contents = []
        storage_node = self.storage.tail

        while storage_node:
            if storage_node.value is not None:
                list_buffer_contents.append(storage_node.value)
            storage_node = storage_node.prev

        return list_buffer_contents



