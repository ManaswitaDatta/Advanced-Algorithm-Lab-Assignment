import sys
import heapq


# This is our priority queue implementation
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, resource, finish):
        heapq.heappush(self._queue, (finish, self._index, resource)) # sort by the first element of the tuple
        self._index += 1

    def pop(self):
        if self._index == 0:
            return None
        return heapq.heappop(self._queue)[-1]


class Resource:
    def __init__(self, number, finish):
        self.number = number
        self.finish = finish


def find_num_resources(time):
    time.sort(key=lambda x: x[0])
    num_resources = 0
    priority_queue = PriorityQueue()
    list_resources = []
    for x in time:
        # we have job here, now pop the classroom with least finishing time
        resource = priority_queue.pop()
        if resource is None:
            # allocate a new class
            num_resources += 1
            new_resource = Resource(num_resources, x[1])
            list_resources.append([num_resources, x])
            priority_queue.push(new_resource, x[1])

        else:
            # check if finish time of current classroom is
            # less than start time of this lecture
            if resource.finish <= x[0]:
                resource.finish = x[1]
                list_resources.append([resource.number, x])
                priority_queue.push(resource, x[1])
            else:
                num_resources += 1
                # Since last classroom needs to be compared again, push it back
                priority_queue.push(resource, x[1])
                # Push the new classroom in list
                new_resource = Resource(num_resources, x[1])
                list_resources.append([num_resources, x])
                priority_queue.push(new_resource, x[1])
    return num_resources, list_resources


def main():
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1] #input3.txt
    file = open(fname, 'r')
    n = int(file.readline())
    time = []
    for i in range(n):
        line = file.readline().split(' ')
        time.append([int(line[0]), int(line[1])])
    total_resources, list_resources = find_num_resources(time)
    print("Minimum number of resources: ", total_resources)
    res = []*total_resources
    for i in range(total_resources):
        res.append([])
    for x in list_resources:
        res[x[0] - 1].append(x[1])
    i = 1
    for x in res:
        print("Resource ", i, " jobs: ", x)
        i += 1
    file.close()


if __name__ == '__main__':
    main()