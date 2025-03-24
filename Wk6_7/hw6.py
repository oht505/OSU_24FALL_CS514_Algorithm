############################################################
## Homework Assignment Week 6 and 7: Dynamic Programming
## Name: Hyuntaek Oh
## Email: ohhyun@oregonstate.edu
## Course: CS 514_400 Algorithms
## Due: Nov. 18, 2024
#############################################################
import string
import random
import matplotlib.pyplot as plt
import time

def generate_words(num_pairs, length):
    words_list = []
    for _ in range(num_pairs):
        char = ''
        for _ in range(length):
            char += random.choice(string.ascii_lowercase)
        words_list.append(char)

    return words_list

def generate_multiple_pairs(num_pairs, length):
    pairs = []
    words_list = generate_words(num_pairs, length)

    # Generate edit strings
    for word in words_list:
        edit_type = random.choices(["insert", "delete", "replace"], k=len(word)//2)
        edited_word = word

        for edit in edit_type:
            if edit == "insert":
                position = random.randint(0, len(word))
                char = random.choice(string.ascii_lowercase)
                edited_word = edited_word[:position] + char + edited_word[position:]
            elif edit_type == "delete":
                position = random.randint(0, len(word)-1)
                edited_word = edited_word[:position] + edited_word[position+1:]
            else:
                position = random.randint(0, len(word)-1)
                char = random.choice(string.ascii_lowercase)
                edited_word = edited_word[:position] + char + edited_word[position+1:]

        pairs.append([word, edited_word])

    return pairs

def editDistance(start, end):
    m = len(start)
    n = len(end)
    D = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        D[i][0] = i

    for j in range(n+1):
        D[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            if start[i-1] == end[j-1]:
                D[i][j] = D[i-1][j-1]
            else:
                insertion = 1 + D[i][j-1]
                deletion = 1 + D[i-1][j]
                replacement = 1 + D[i-1][j-1]
                D[i][j] = min(insertion, deletion, replacement)

    edit_distance = D[-1][-1]

    return edit_distance

def measure_time(num_pairs, length):

    words_list = generate_multiple_pairs(num_pairs, length)
    result = []
    time_taken = 0
    num_iteration = 10

    # Calculate average time
    for _ in range(num_iteration):
        for start_string, end_string in words_list:
            start_time = time.time()
            editDistance(start_string, end_string)
            end_time = time.time()
            time_taken += (end_time - start_time)

    average_time = (time_taken / num_iteration)

    # Record result
    for start_string, end_string in words_list:
        d = editDistance(start_string, end_string)
        result.append(d)

    return average_time, result


# if __name__=="__main__":
#     # start_string = "babble"
#     # end_string = "apple"
#     # start_string = "tatttacccaccacttctcccgttctcgaatcaggaatagactactgcaatcgacgtagggataggaaactccccgagtttccacagaccgcgcgcgatattgctcgccggcatacagcccttgcgggaaatcggcaaccagttgagtagttcattggcttaagacgctttaagtacttaggatggtcgcgtcgtgccaa"
#     # end_string = "atggtctccccgcaagataccctaattccttcactctctcacctagagcaccttaacgtgaaagatggctttaggatggcatagctatgccgtggtgctatgagatcaaacaccgctttctttttagaacgggtcctaatacgacgtgccgtgcacagcattgtaataacactggacgacgcgggctcggttagtaagtt"
#     #
#     # print(editDistance(start_string, end_string))
#
#     num_pairs = 10
#     set_length = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
#     set_avg_time = []
#     set_estimated_time = []
#     print(f"{'Length of words: ':<20}{'Estimated Time O(mn): ':<25}{'Average Time (s): ':<25}{'Result: ':<25}")
#     for length in set_length:
#         estimated_time = length**2
#         avg_time, result = measure_time(num_pairs, length)
#         set_avg_time.append(avg_time)
#         set_estimated_time.append(estimated_time)
#         print(f"{length:<20}{estimated_time:<25}{avg_time:<25}{result}")
#
#     # Estimated time
#     fig, ax1 = plt.subplots(figsize=(8, 6))
#     ax1.plot(set_length, set_estimated_time, label="Estimated Time O(mn)", color="blue", marker="o")
#     ax1.set_xlabel("Length of words")
#     ax1.set_ylabel("Estimated Time (O(mn))", color='blue')
#     ax1.tick_params(axis='y', labelcolor='blue')
#
#     # Average Time
#     ax2 = ax1.twinx()
#     ax2.plot(set_length, set_avg_time, label="Average Time (s)", color="orange", marker="s")
#     ax2.set_ylabel("Average Time (s)", color='orange')
#     ax2.tick_params(axis='y', labelcolor='orange')
#
#     fig.suptitle("Comparison of Estimated and Average Time by Word Length")
#     ax1.grid(True, which="both", linestyle='--', linewidth=0.5)
#     fig.legend(loc="upper left", bbox_to_anchor=(0.1, 0.9))
#     plt.show()
#
#     growth_ratios = []
#     estimated_growth_ratios = []
#     for i in range(1, len(set_length)):
#         ratio = set_avg_time[i] / set_avg_time[i-1]
#         estimated_growth_ratio = set_estimated_time[i] / set_estimated_time[i-1]
#         growth_ratios.append(ratio)
#         estimated_growth_ratios.append(estimated_growth_ratio)
#
#     print()
#     print(f"{'Input Size: ':<20}{'Estimated Growth Ratio: ':<25}{'Real Growth Ratio: ':<25}")
#     for i in range(1, len(set_length)):
#         print(f"{set_length[i]:<20}{estimated_growth_ratios[i-1]:<25}{growth_ratios[i-1]:<25}")


