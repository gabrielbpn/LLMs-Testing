def max_points(sequence):
    # Create a frequency dictionary to count the occurrences of each number
    freq = {}
    for num in sequence:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize the maximum points
    max_points = 0

    # Iterate over the frequency dictionary
    for num, count in freq.items():
        # Calculate the points for the current number and its neighbors
        points = count
        if num - 1 in freq:
            points += freq[num - 1]
        if num + 1 in freq:
            points += freq[num + 1]

        # Update the maximum points
        max_points = max(max_points, points)

    return max_points

# Get the input
n = int(input())
sequence = list(map(int, input().split()))

# Calculate and print the maximum points
print(max_points(sequence))