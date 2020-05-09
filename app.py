#problem---Sum in Loop

def sum_in_loop():
    nun_data = int(input("How how many number you wants to add: "))
    my_li = list(map(int, input('Enter you number by space: ').split()))[:nun_data]
    print(my_li)
    sum = 0

    for i in my_li:
        sum = sum +i
    print(sum)
sum_in_loop()