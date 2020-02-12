def calc_error(value_n):

    pi = 0.0
    true_pi = 3.1415926535897932384626433
    for i in range(1,value_n + 1):
        x = 1/(1 + ((i-0.5)/value_n)**2)
        pi = pi + x
    estimate = 4/value_n * pi
    error =  4*pi/value_n - true_pi

    return error


def bounds(target_error):
    power = 0
    error = target_error + 1
    while error > target_error:

        y = 10**power
        error = calc_error(y)
        power += 1

    upper_bound = y
    lower_bound = int(y/10)
    return lower_bound, upper_bound

def binary_search(begin_index, end_index, target_error):

    smallest_n_checked_smaller = end_index + 1
    smallest_n_checked_smaller_error = -1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        error = calc_error(midpoint)

        if error <= target_error:
            if midpoint < smallest_n_checked_smaller:
                smallest_n_checked_smaller = midpoint
                smallest_n_checked_smaller_error = error
            end_index = midpoint - 1

        elif target_error < error:
            begin_index = midpoint + 1

    return smallest_n_checked_smaller, smallest_n_checked_smaller_error


target_error = 10**(-6)
lower_bound, upper_bound = bounds(target_error)
#print(lower_bound, upper_bound)
n_val, error = binary_search(lower_bound, upper_bound, target_error)
print(n_val, error)
#print(n_val-1, calc_error(n_val-1))
