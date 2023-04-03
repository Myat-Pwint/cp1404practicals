import random

LENGTH_QUICK_PICK = 6
MIN_NUM = 1
MAX_NUM = 45


def generate_quick_pick():
    quick_pick = []
    while len(quick_pick) < LENGTH_QUICK_PICK:
        num = random.randint(MIN_NUM, MAX_NUM)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()
    return quick_pick


total_quick_picks = int(input("How many quick picks? "))
for i in range(total_quick_picks):
    quick_pick = generate_quick_pick()
    print(" ".join("{:2}".format(num) for num in quick_pick))
