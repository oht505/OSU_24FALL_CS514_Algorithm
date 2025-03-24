
def find_longest_common_substring(str1, str2):
    m, n = len(str1), len(str2)
    c = [[0 for _ in range(n+1)] for _ in range(m+1)]

    max_length = 0
    end_idx = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                if c[i][j] > max_length:
                    max_length = c[i][j]
                    end_idx = i
            else:
                c[i][j] = 0

    longest_substring = str1[end_idx - max_length : end_idx]

    return longest_substring


if __name__=="__main__":
    str1, str2 = "maga", "megazine"
    # str1, str2 = "Philanthropic", "Misanthropist"
    print(find_longest_common_substring(str1, str2))

