def custom_range(start, end, step=1):
    while start < end:
        yield start
        start += step

for num in custom_range(1, 5):
    print(num)
