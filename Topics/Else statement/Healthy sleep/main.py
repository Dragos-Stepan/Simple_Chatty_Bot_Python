recommended_sleep = int(input())
not_more_sleep = int(input())
ann_sleep = int(input())
if ann_sleep >= recommended_sleep:
    print("Normal")
elif ann_sleep < recommended_sleep:
    print("Deficiency")
elif ann_sleep > not_more_sleep:
    print("Excess")
