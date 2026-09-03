def f(N):
    count = 0
    for i in range(N):
        print("i:" + str(i))
        for j in range(i):
            print("   j:" + str(j))
            count += 1
    print("--------")
    print(N, count)
    print("----------------")

f(1)
f(2)
f(3)
f(4)