k = int(input().split(' ')[1])
input_numbers = list(map(int, input().split(' ')))
count_of_even = len([int(i) for i in input_numbers if int(i) % 2 == 0])


def okno():
    windows_size = 0
    global k
    change_inx = []
    full_max = 0
    window_start_inx = 0
    for inx, val in enumerate(input_numbers):
        if full_max == count_of_even:
            return full_max
        if val % 2 == 0:
            windows_size += 1
        elif count_of_even - windows_size > 0 and k > 0:
            windows_size += 1
            k -= 1
            change_inx.append(inx)
        else:
            while not count_of_even - windows_size > 0 and not k > 0:
                window_start_inx += 1
                if input_numbers[window_start_inx-1] % 2 == 0:
                    windows_size -= 1
                if window_start_inx-1 in change_inx:
                    k += 1
                    change_inx.remove(window_start_inx-1)

        full_max = max(windows_size, full_max)

    return full_max


print(okno())