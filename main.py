import sys

def levin(a, b):
    n, m = len(a), len(b)
    cur_row = range(n + 1)
    for i in range(1, m + 1):
        old_row, cur_row = cur_row, [i] + [0] * n
        for j in range(1, n + 1):
            if a[j - 1] != b[i - 1]:
                cur_row[j] = min(old_row[j] + 1, cur_row[j - 1] + 1, old_row[j - 1] + 1)
            else:
                cur_row[j] = min(old_row[j] + 1, cur_row[j - 1] + 1, old_row[j - 1])
    return cur_row[n]


input_name = sys.argv[1]
output_name = sys.argv[2]
inp = open(input_name, 'r')
sc = open(output_name, 'w')
sp = inp.read().split('\n')
answers = []
for i in range(0, len(sp), 2):
    answers.append(str(levin(sp[i], sp[i + 1])))
new_ans = "\n".join(answers)
sc.write(new_ans)





