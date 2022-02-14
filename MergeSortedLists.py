# https://www.interviewquery.com/questions/merge-sorted-lists


list1 = [1, 2, 5]
list2 = [2, 4, 6]

"""
def merge_list(list1, list2):
    return sorted(list1 + list2)"""


def merge_list(list1: list, list2: list) -> list:
    if not list1:
        return list2
    if not list2:
        return list1

    i, j = 0, 0
    final_list = []

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list.append(list1[i])
            i += 1
        elif list2[j] < list1[i]:
            final_list.append(list2[j])
            j += 1
        else:
            final_list.extend([list1[i], list2[j]])
            j += 1
            i += 1
    return final_list


print(merge_list(list1, list2))
