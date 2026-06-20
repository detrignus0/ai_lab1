for i in range(3):
    print(f"Итерация {i}")

!python test_script.py
%%time
total = 0
for i in range(10**8):
    total += i

%timeit sum(range(1000))
