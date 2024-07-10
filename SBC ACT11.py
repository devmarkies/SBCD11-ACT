def bubble_sort(elements):
    n = len(elements)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
                swapped = True
        if not swapped:
            break

elements = ['D', 'S', 'M', 'R', 'A', 'E']
print("Initial elements:", elements)
bubble_sort(elements)
print("Sorted elements:", elements)
