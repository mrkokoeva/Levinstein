import sys


def levinstein(a, b):
    n, m = len(a), len(b)
    cur_row = range(n + 1)
    for i in range(1, m + 1):
        old_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            add = old_row[j] + 1
            change = old_row[j - 1]
            delete = cur_row[j - 1] + 1
            if a[j - 1] != b[i - 1]:
                cur_row[j] = min(add, delete, change + 1)
            else:
                cur_row[j] = min(add, delete, change)
    return cur_row[n]


input_name = sys.argv[1]
output_name = sys.argv[2]
inp = open(input_name, 'r')
sc = open(output_name, 'w')
lst = inp.read().split('\n')
answers = []
for i in range(0, len(lst), 2):
    answers.append(str(levinstein(lst[i], lst[i + 1])))
new_ans = "\n".join(answers)
sc.write(new_ans)
