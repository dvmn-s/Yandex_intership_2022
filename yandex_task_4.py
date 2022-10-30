n = int(input())
array = []

for i in range(n):
    array.append(input())

m = len(array[0])

def pair_count(d):
    return sum((i * (i - 1)) // 2 for i in d.values())


def Difference(array, m):
    changed, same = {}, {}
    for s in array:
        same[s] = same.get(s, 0) + 1
        for i in range(m):
            t = s[:i] + '#' + s[i + 1:]
            changed[t] = changed.get(t, 0) + 1

    return pair_count(changed) - pair_count(same) * m


print(Difference(array, m))