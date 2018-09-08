from collections import defaultdict


all_codes = set([l.strip() for l in open('p079_keylog.txt').readlines()])
all_pos = defaultdict(list)

for code in all_codes:
    all_pos[code[0]].append(0)
    all_pos[code[1]].append(1)
    all_pos[code[2]].append(2)

avg_pos = [(dig, sum(all_pos[dig]) / len(all_pos[dig])) for dig in all_pos]

avg_pos.sort(key=lambda x: x[1])
print(''.join([x[0] for x in avg_pos]))