from test_framework import generic_test
import heapq


# Min Heap implementation from scratch
class MinHeap:
    def __init__(self):
        # create a heap data structure with first element as some dummy
        self.heap = [0]

    def is_empty(self):
        return len(self.heap) == 1

    def insert(self, k):
        # insert element at the end
        self.heap.append(k)
        # traverse from leaf to root
        i = len(self.heap) - 1
        while i != 1:
            # if parent is higher, then swap parent and child, else break as heap property is preserved
            if self.heap[i] < self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            else:
                break
            i //= 2

    def remove(self):
        if self.is_empty():
            return
        # get minimum value from root
        min_val = self.heap[1]
        # set root value to last leaf node value
        self.heap[1] = self.heap[-1]

        # heapify
        i, s = 1, len(self.heap) - 1
        # iterate until all children are traversed
        while 2 * i < s:
            # check if left or right child is minimum
            if self.heap[2 * i] < self.heap[2 * i + 1]:
                j = 2 * i
            else:
                j = 2 * i + 1
            # if parent is higher, swap parent node with minimum value child node
            if self.heap[i] > self.heap[j]:
                self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            # go to updated child node
            i = j

        # remove last element
        self.heap.pop()

        return min_val


def merge_sorted_arrays(sorted_arrays):
    # Time complexity : O(n log k) where n is the total number of elements and k is the size of heap
    # Space complexity : O(k + n) where k for heap and n for storing the result

    # # using MinHeap class implemented above
    # heap = MinHeap()
    # ans = []
    # for i, sorted_array in enumerate(sorted_arrays):
    #     if sorted_array:
    #         # insert first elements of each array and the array index into min heap
    #         heap.insert((sorted_array[0], i))
    #         # remove the first elements from the arrays
    #         sorted_array.pop(0)
    #
    # # iterate heap is empty
    # while not heap.is_empty():
    #     # get minimum value and array from which it is fetched
    #     min_val, arg_min = heap.remove()
    #     # append the minimum value to ans
    #     ans.append(min_val)
    #     # if still there are elements left from the fetched element array
    #     if sorted_arrays[arg_min]:
    #         # insert next element from the array into heap
    #         heap.insert((sorted_arrays[arg_min][0], arg_min))
    #         # remove next element from the array
    #         sorted_arrays[arg_min].pop(0)
    #
    # return ans

    # using heapq library
    heap = []
    ans = []
    for i, sorted_array in enumerate(sorted_arrays):
        if sorted_array:
            heapq.heappush(heap, (sorted_array[0], i))
            sorted_array.pop(0)

    while heap:
        min_val, arg_min = heapq.heappop(heap)
        ans.append(min_val)
        if sorted_arrays[arg_min]:
            heapq.heappush(heap, (sorted_arrays[arg_min][0], arg_min))
            sorted_arrays[arg_min].pop(0)

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_arrays_merge.py",
                                       "sorted_arrays_merge.tsv",
                                       merge_sorted_arrays))
