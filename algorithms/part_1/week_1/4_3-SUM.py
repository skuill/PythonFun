
def partition(data, low, hight):
    value = data[int((low+hight)/2)]
    i = low
    j = hight
    while (i <= j):
        while data[i] < value:
            i+=1
        while data[j] > value:
            j-=1
        if (i <= j):
            data[i], data[j] = data[j], data[i]
            i+=1
            j-=1
    return i

def quick_sort(data, low, hight):
    if (low < hight):
        q = partition (data, low, hight)
        quick_sort(data, low, q-1)
        quick_sort(data, q, hight)


input_data = [30, -40, -20, -10, 40, 0, 10, 5]
interesting_sum = 30
array_length = len(input_data)-1
quick_sort(input_data, 0, array_length)

result=[]

for i in range (0, array_length):
    low = i+1
    hight = array_length
    while (low < hight):
        tmp = input_data[low] + input_data[hight] + input_data[i]
        if tmp > interesting_sum:
            hight-=1
        elif tmp < interesting_sum:
            low+=1
        else:
            result.append((input_data[low], input_data[hight], input_data[i]))
            low+=1
            hight-=1