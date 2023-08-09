def max_and_min(arr1,arr2):
    diffs = [abs(x-y) for x in arr1 for y in arr2]
    print(diffs)
    return [max(diffs), min(diffs)]

max_and_min([3,10,5],[20,7,15,8])