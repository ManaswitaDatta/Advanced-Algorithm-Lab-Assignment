import sys



def schedule(start, finish, res):
    index = list(range(len(start)))
    # sort according to finish times
    index.sort(key=lambda i: finish[i])
    print(index)

    prev_finish_time = 0
    for i in index:
        if start[i] >= prev_finish_time:
            res.append([start[i], finish[i]])
            prev_finish_time = finish[i]


def main():
    if len(sys.argv) != 2:
        return

    fname = sys.argv[1] #input2.txt
    file = open(fname, 'r')
    n = int(file.readline())
    start = []
    finish = []
    for i in range(n):
        line = file.readline().split(' ')
        start.append(int(line[0]))
        finish.append(int(line[1]))
    res = []
    schedule(start, finish, res)
    print(res)
    file.close()


if __name__ == '__main__':
    main()