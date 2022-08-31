def knapsack(capacity, weight, price):
    for i in range(len(weight)):
        for j in range(capacity + 1):
            if weight[i] <= j:
                knapsackMatrix[i][j] = max(price[i] + knapsackMatrix[i-1][j-weight[i]], knapsackMatrix[i-1][j])
            else:
                knapsackMatrix[i][j] = knapsackMatrix[i-1][j]
    return knapsackMatrix[-1][-1]

capacity = int(input("Capacity: "))
print("Input weights:")
weight = list(map(int, input().split()))
knapsackMatrix = [[0 for i in range(capacity + 1)] for i in range(len(weight))]
print("Input prices:")
price = list(map(int, input().split()))
print(f"Maximum possible value: {knapsack(capacity, weight, price)}")
ch = []
ch1 = []
i = len(weight) - 1
j = capacity
while i >= 0 and j > 0:
    if knapsackMatrix[i][j] == knapsackMatrix[i-1][j] and i-1 >= 0:
        i -= 1
    else:
        ch.insert(0, price[i])
        ch1.insert(0,weight[i])
        j -= weight[i]
        i -= 1
print(f'The choices are: price :{ch}, weight: {ch1}')