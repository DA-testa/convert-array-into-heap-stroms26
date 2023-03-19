# python3
def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(n // 2, -1, -1):
        min_heapify(i, data, swaps)

    return swaps


def min_heapify(i, arr, swaps):
    n = len(arr)

    left = 2 * i + 1
    right = 2 * i + 2

    smallest = i

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        swaps.append((i, smallest))
        min_heapify(smallest, arr, swaps)


def main():
    input_type = input()
    if "I" in input_type:
        n = int(input())
        arr = list(map(int, input().split()))
    elif "F" in input_type:
        file_name = input()
        if "a" not in file_name:
            with open('./tests/'+file_name, 'r') as f:
                n = int(f.readline())
                arr = list(map(int, f.readline().split()))

    assert len(arr) == n

    swaps = build_heap(arr)

    assert len(swaps) <= 4 * n
    print(len(swaps))

    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

