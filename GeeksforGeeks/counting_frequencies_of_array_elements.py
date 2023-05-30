def frequency_number(arr, size):
    freq_map = {}

    for i in range(size):
        if arr[i] in freq_map:
            freq_map[arr[i]] += 1
        else:
            freq_map[arr[i]] = 1
    
    for key, value in freq_map.items():
        print(f"{key} {value}")

arr = [10, 20, 20, 10, 10, 20, 5, 20]
size = len(arr)
frequency_number(arr,size)