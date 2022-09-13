length_of_circular_linked_list = int(input())
# Read space-separated integers that denote the elements of the list which is returned as the output of the algorithm
circular_linked_list = list(map(int,input().strip().split(" ")))
# Write your code here
correct_list = []

for i in circular_linked_list:
    if i not in correct_list:
        correct_list.append(i)

print(len(correct_list))

for i in correct_list:
    print(i,end=" ")
