# 0/1 Knapsack
# Global Variables
values = []
weights = []
capacity = 0

def _01knapsack(capacity, weights, values, arrLen):
    # Base Case
    if arrLen == 0 or capacity == 0:
        return 0
    
    if (weights[arrLen-1] > capacity):
        return _01knapsack(capacity, weights, values, arrLen-1)
 
    else:
        return max(
            values[arrLen-1] + _01knapsack(capacity-weights[arrLen-1], weights, values, arrLen-1), _01knapsack(capacity, weights, values, arrLen-1))

def setCapacity(value):
    global capacity
    capacity = value

while(True):
    print("""
Enter 1: Enter Weight Value pair,
Enter 2: Set Knapsack Capacity,
Enter 3: Run 0/1 Knapsack Algo,
Enter 4: Exit
""")
    choice = int(input(" => "))
    if choice == 1:
        weights.append(int(input("Enter the Weight: ")))
        values.append(int(input("Enter the Value: ")))
    elif choice == 2:
        setCapacity(int(input("Enter the capacity of knapsack: ")))
    elif choice == 3:
        if capacity == 0:
            setCapacity(int(input("Enter the capacity of knapsack: ")))
        print("Total Value:", _01knapsack(capacity, weights, values, len(values)))
    elif choice == 4:
        exit(0)
    else:
        print("Invalid Input!")