import collections

from test_framework import generic_test

PairedTasks = collections.namedtuple('PairedTasks', ('task_1', 'task_2'))


def optimum_task_assignment(task_durations):
    # Time complexity = O(n log n)
    # Space complexity = O(n)
    task_durations.sort()
    i, j = 0, len(task_durations) - 1
    ans = []
    while i < j:
        ans.append((task_durations[i], task_durations[j]))
        i += 1
        j -= 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("task_pairing.py", 'task_pairing.tsv',
                                       optimum_task_assignment))
