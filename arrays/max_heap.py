class Solution:
    def __init__(self, max_size):
        self.heap = [max_size]
        self.size = 0

    def get_parent(self, node):
        return node // 2

    def get_left_child(self, node):
        return node * 2

    def get_right_child(self, node):
        return (node * 2) + 1

    def add_element(self, element):
        self.heap.append(element)
        self.size += 1
        if self.size == 1:
            return
        node = self.size

        while node > 1 and self.heap[node] > self.heap[self.get_parent(node)]:
            print(f"parent of {node} is {self.get_parent(node)}")
            self.heap[node], self.heap[self.get_parent(node)] = self.heap[self.get_parent(node)], self.heap[node]
            node = self.get_parent(node)

    def get_max_element(self):
        return self.heap[1]

    def extract_max_element(self):
        maxx = self.heap[1]
        self.heap[1], self.heap[self.size] = self.heap[self.size], self.heap[1]
        self.heap = self.heap[:-1]
        self.size -= 1
        self.heapify()
        return maxx

    def exchange_with(self, node):
        left_child = self.get_left_child(node)
        right_child = self.get_right_child(node)

        if left_child > self.size or right_child > self.size:
            return None

        if self.heap[node] >= max(self.heap[left_child], self.heap[right_child]):
            return None
        else:
            if self.heap[left_child] >= self.heap[right_child]:
                return left_child
            else:
                return right_child

    def heapify(self):
        node = 1

        while self.exchange_with(node) and node <= self.size:
            child = self.exchange_with(node)
            self.heap[node], self.heap[child] = self.heap[child], self.heap[node]
            node = child


if __name__ == "__main__":
    obj = Solution(100)
    #            2
    #         /    \
    #        3      4
    #      /   \   /   \
    #     5     6 7     8
    obj.add_element(10)
    obj.add_element(20)
    obj.add_element(30)
    obj.add_element(40)
    breakpoint()
