#!/usr/bin/python
##################################################
# This programs included in this file are as follows
# 1) Unique value list from list with duplicates
# 2)
# 3)
# 4)
# 5)
# 6)
# 7)
##################################################
# Author: Tanyaradzwa Matasva
# Course: CPSC-442-11
# Instructor: Dr Abdelshakour Abuzneid
# School: University of Bridgeport
##################################################
import collections

print("Question 1: Remove duplicates from list")


def remove_duplicates(list_with_duplicates):
    unique_vals_set = set(list_with_duplicates)  # convert list to set
    return list(unique_vals_set)  # convert set back to list


input_vals = [1, 3, 2, 5, 1, 3, 7, 6, 3, 2]
print("Input : "+str(input_vals))
print("Out put: "+str(remove_duplicates(input_vals)))

# Reverse and Invert matrices
print("\n\nQuestion 2: Reverse and Invert matrices\n")


def reverse_and_invert(input_matrix):
    for i in range(len(input_matrix)):
        input_matrix[i].reverse()  # reverse the order of the current row
        for j in range(len(input_matrix[i])):  # go through each column in the row and invert the digits
            if input_matrix[i][j] == 1:
                input_matrix[i][j] = 0
            elif input_matrix[i][j] == 0:
                input_matrix[i][j] = 1

    print("Output : "+str(input_matrix))


input_matrix = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print("Input : "+str(input_matrix))
reverse_and_invert(input_matrix)

print("\n\nQuestion 3 : Finding uncommon words")


def find_uncommon_words(input_string_a,input_string_b):
    print("\n\nInput : "+str(input_string_a)+"\n\t\t"+str(input_string_b))
    list_of_a = input_string_a.split(" ")
    list_of_b = input_string_b.split(" ")
    list_of_uncommons = []
    for i in list_of_b:
        if i not in input_string_a:
            if list_of_b.count(i) == 1:
                list_of_uncommons.append(i)
    if len(list_of_uncommons) == 0:
        for i in list_of_a:
            if i not in input_string_b:
                if list_of_a.count(i) == 1:
                    list_of_uncommons.append(i)

    print(str(list_of_uncommons))


input_string_a = "this apple is sweet"
input_string_b = "this apple is sour"
find_uncommon_words(input_string_a, input_string_b)
input_string_a2 = "apple apple"
input_string_b2 = "banana"
find_uncommon_words(input_string_a2,input_string_b2)


print("\n\nQuestion 4 : How many times a sub-domain is visited ")


def domain_visited(domain_list):
    print("\n\nInput : " + str(domain_list)+"\n")
    hit_list = []

    for domain in domain_list:
        s = domain.find(' ')
        hit = domain[0:s]
        hit_list.append(domain)
        for i in range(len(domain)):
            if domain[i] == '.':
                hit_list.append(hit + " " + domain[(i+1):])

    print("\n\nOutput : "+str(hit_list))


domain_visited(["100 www.facebook.com"])

print("\n\nQuestion 5 : Maximum possible heights of buildings")


def column(a, i):  # get column values for maximum building height method
    return [r[i] for r in a]


def max_building_height(matrix):
    print("Input : "+str(matrix))
    left_to_right = []
    top_to_bottom = []
    s = 0  # sum of height changes
    for i in matrix:  # get the highest from left to right
        left_to_right = left_to_right+[max(i)]

    for i in range(len(matrix[0])):  # find the highest from top to bottom
        top_to_bottom = top_to_bottom+[max(column(matrix, i))]

    for i in range(len(matrix)):  # increase heights of buildings
        for j in range(len(matrix[0])):
            if left_to_right[i] < top_to_bottom[j]:
                s = s+left_to_right[i]-matrix[i][j]  # update sum
                matrix[i][j] = left_to_right[i]
            else:
                s = s+top_to_bottom[j] - matrix[i][j]  # update sum
                matrix[i][j] = top_to_bottom[j]
    print("\n\nOutput : "+str(matrix))
    print("Sum : "+str(s)+"\n")


max_building_height([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])

print("\n\nQuestion 6 : Grouping anagrams\n")


def group_anagrams(word_list):
    _list = word_list
    result = []
    print("Input : "+str(_list))

    ans = collections.defaultdict(list)
    for s in word_list:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    result = list(ans.values())

    print("Output : "+str(result))


anagram_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
group_anagrams(anagram_list)

print("\n\nQuestion 7 : Print single int")


def find_single_int(sorted_list):
    print("Input : " + str(sorted_list))
    for i in sorted_list:
        if sorted_list.count(i) == 1:
            print("Output : " + str(i))


input_sorted_ints = [1, 1, 2, 3, 3, 4, 4, 8, 8]
find_single_int(input_sorted_ints)