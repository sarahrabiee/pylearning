def linear_search(l, item):
    if item in l:
        return l.index(item)
    else:
        return -1

def linear_search_2(l, search_item):
    for index, item in enumerate(l):
        if item == search_item:
            return index
    return -1


if __name__ == '__main__':
    print(linear_search([], 1))
    print(linear_search([1, 2, 3], 3))
    print(linear_search([1, 2], 3))
    print(linear_search([1, -2, 1], 1))
    print(linear_search_2(["a", "b", "c"], "b"))