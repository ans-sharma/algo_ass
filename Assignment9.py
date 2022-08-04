# Global variables
values = [] # values: { weights, values }
capacity = 0

def fractionalKnapsack(values, capacity, unit = "kg"):
    # values: { weights, value }
    # capacity: capicity of knapsack
    knapsackCurrentCap = 0
    price = 0
    
    # calaculating the value weight ratio
    for i in range(len(values)):
        values[i].append(values[i][1]/values[i][0])   
    # print(values)
    # sorting in dec order wrt value weight ratio
    values = sorted(values, key=lambda x: x[2], reverse=True)
    
    for value in values:
        if (knapsackCurrentCap + value[0]) <= capacity:
            knapsackCurrentCap += value[0]
            price += value[1]
            print(str(value[0]) + unit + " weight added, of value "+ str(value[1]))
        elif knapsackCurrentCap < capacity:
            # print(2)
            temp = capacity - knapsackCurrentCap
            knapsackCurrentCap += temp
            price += (temp*value[2])
            print(str(temp) + unit + " weight added, of value "+ str(temp*value[2]))
    print("Total Value:", price)
      
def setCapacity(value):
    global capacity
    capacity = value      

# values = [[20, 60], [50, 100], [30, 120]]
# values = [[5, 30], [10, 40], [15, 45], [22, 77], [25, 90]]
# fractionalKnapsack(values, 60)

while(True):
    print("""
Enter 1: Enter Weight Value pair,
Enter 2: Set Knapsack Capacity,
Enter 3: Run Fractional Knapsack Algo,
Enter 4: Exit
""")
    choice = int(input(" => "))
    if choice == 1:
        temp = []
        temp.append(int(input("Enter the Weight: ")))
        temp.append(int(input("Enter the Value: ")))
        values.append(temp)
        # print(values)
    elif choice == 2:
        setCapacity(int(input("Enter the capacity of knapsack: ")))
    elif choice == 3:
        if capacity == 0:
            setCapacity(int(input("Enter the capacity of knapsack: ")))
        fractionalKnapsack(values, capacity)
    elif choice == 4:
        exit(0)
    else:
        print("Invalid Input!")
