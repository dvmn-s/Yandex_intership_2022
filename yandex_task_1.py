import itertools


list1 = input().split(' ')[1:]
list2 = input().split(' ')[1:]
list3 = input().split(' ')[1:]


list_possib = list(itertools.permutations([list1, list2, list3]))


fin_otv = []


def merge(permutations):
    first_permutation = [*permutations[0]]
    flag = -1
    for permutation in permutations[1:]:
        first = 0
        second = 0
        while second <= len(permutation):
            if second == len(permutation):
                break
            if first >= len(first_permutation):
                first_permutation += permutation[second:]
                break
            if first_permutation[first] == permutation[second]:
                flag = first if flag == -1 else flag
                first += 1
                second += 1
            else:
                second = 0
                first += 1

    return first_permutation


for i in list_possib:
    fin_otv.append(merge(i))


finally_otv = sorted(fin_otv, key=len)[0]

print(len(finally_otv))
print(*finally_otv)















