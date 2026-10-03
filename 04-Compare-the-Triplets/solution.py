def compareTriplets(a, b):
    alice = sum(1 for i in range(3) if a[i] > b[i])
    bob = sum(1 for i in range(3) if a[i] < b[i])
    return [alice, bob]
