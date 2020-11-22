class profitData:
    __slots__ = ['min_idx', 'max_idx', 'profit']

    def __init__(self, min_idx=0, max_idx=0, profit=0):
        self.min_idx = min_idx
        self.max_idx = max_idx
        self.profit = profit


def optTrans1(buy, sell, c):
    profit = 0
    for i in range(0, len(buy)):
        for j in range(i, n):
            profit = max(profit, c*(sell[j] - buy[i])/buy[i])
    return profit


def both_part(buy, sell, l, m, h, c):
    min_ind = m
    for i in range(l, m):
        if buy[min_ind] > buy[i]:
            min_ind = i

    max_ind = m
    for i in range(m+1, h+1):
        if sell[max_ind] < sell[i]:
            max_ind = i

    return c*(sell[max_ind] - buy[min_ind])/buy[min_ind]


def optTrans2(buy, sell, l, h, c):
    if l == h:
        return c*(sell[l] - buy[l])/buy[l]
    mid = int((l + h) // 2)
    lopt = optTrans2(buy, sell, l, mid, c)
    ropt = optTrans2(buy, sell, mid + 1, h, c)
    mid_part = both_part(buy, sell, l, mid + 1, h, c)
    return max(max(lopt, ropt), mid_part)


def optTrans3(buy, sell, l, h, c):

    if l == h:
        opt = profitData(l, l, (c / buy[l]) * (sell[l] - buy[l]))
        return opt

    mid = int((l + h) // 2)
    lopt = optTrans3(buy, sell, l, mid, c)
    ropt = optTrans3(buy, sell, mid + 1, h, c)
    lrprofit = (c / buy[lopt.min_idx]) * (sell[ropt.max_idx] - buy[lopt.min_idx])
    opt = profitData()
    if (lrprofit > lopt.profit) and (lrprofit > ropt.profit):
        opt.profit = lrprofit
    elif lopt.profit > ropt.profit:
        opt.profit = lopt.profit
    else:
        opt.profit = ropt.profit

    #Take the minimum of two mins and maximum of two maxs. This recurssive computation changes O(n) to O(1)
    opt.min_idx = lopt.min_idx if buy[lopt.min_idx] <= buy[ropt.min_idx] else ropt.min_idx
    opt.max_idx = lopt.max_idx if sell[lopt.max_idx] >= sell[ropt.max_idx] else ropt.max_idx
    return opt


def optTrans4(buy, sell, c): #kadane algorithm O(n)
    profit = 0
    min = buy[0]
    for i in range(0, len(buy)):
        if min > buy[i]:
            min = buy[i]
        profit = max(profit,  c*(sell[i] - min)/min)
    return profit


n = 10 #int(input("Enter size of the matrix: "))
buy = [10, 15, 16, 9, 25, 6, 5, 18, 5, 21]
sell = [24, 13, 8, 12, 9, 21, 7, 21, 6, 14]

# print("Enter buying prices: ")
# for i in range(0, n):
#    buy.append(int(input()))

# print("Enter selling prices: ")
# for i in range(0, n):
#    sell.append(int(input()))

print("Enter capital: ")
c = 1000 #int(input())

print("Buying price: ")
for x in buy:
    print(x, end=" ")
print("\n")

print("Selling price: ")
for x in sell:
    print(x, end=" ")
print("\n")

print(optTrans1(buy, sell, c))  # method 1
print("\n")

print(optTrans2(buy, sell, 0, len(buy) - 1, c))  # method 2
print("\n")

print(optTrans3(buy, sell, 0, len(buy) - 1, c).profit)  # method 3
print("\n")

print(optTrans4(buy, sell, c))  # method 4 in O(n)
print("\n")