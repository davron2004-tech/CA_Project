class Value:
    """Represents an individual element with its value and cumulative sum."""
    def __init__(self, value, cum_sum):
        self.value = value
        self.cum_sum = cum_sum


class CumulativeArray:
    """Implements a cumulative array data structure."""
    def __init__(self):
        self.array = [Value(0, 0)]  # Initialize with a dummy element to simplify calculations.

    def append(self, value):
        """Appends a new value to the array, updating the cumulative sum."""
        cum_sum = self.array[-1].cum_sum + value
        self.array.append(Value(value, cum_sum))

    def extend(self, values):
        """Appends multiple values to the array, updating cumulative sums."""
        for value in values:
            cum_sum = self.array[-1].cum_sum + value
            self.array.append(Value(value, cum_sum))

    def delete(self, index):
        """Deletes a value at the specified index, adjusting cumulative sums."""
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds.")
        del_value = self.array[index].value
        for i in range(index + 1, len(self.array)):
            self.array[i].cum_sum -= del_value
        self.array.pop(index)

    def range_sum(self, l, r):
        """Calculates the sum of values in the range [l, r]."""
        if l < 0 or r >= len(self.array):
            raise IndexError("Index out of bounds.")
        if l == 0:
            return self.array[r].cum_sum
        return self.array[r].cum_sum - self.array[l - 1].cum_sum

    def __str__(self):
        """Displays the cumulative array as a formatted table."""
        # Determine the maximum width of the numbers for alignment
        max_width = max(len(str(value.cum_sum)) for value in self.array)
        column_width = max(max_width, len("Value"), len("Cumulative Sum")) + 2  # Include padding
        separator = '-' * ((len(self.array) + 1) * (column_width + 3) + 1)

        # Build the table as a string
        result = [separator]

        # Index row
        result.append(f"| {'Index':^{column_width}} " + ''.join(
            f"| {i:^{column_width}} " for i in range(len(self.array))
        ) + "|")
        result.append(separator)

        # Value row
        result.append(f"| {'Value':^{column_width}} " + ''.join(
            f"| {value.value:^{column_width}} " for value in self.array
        ) + "|")
        result.append(separator)

        # Cumulative Sum row
        result.append(f"| {'Cumulative Sum':^{column_width}} " + ''.join(
            f"| {value.cum_sum:^{column_width}} " for value in self.array
        ) + "|")
        result.append(separator)

        return '\n'.join(result)


# Usage Example
if __name__ == "__main__":
    # Initialize the cumulative array
    cum_array = CumulativeArray()

    # Add values to the array
    cum_array.extend([5, 8, 9, 3, 4, 1])

    # Display the cumulative array
    print("Initial Cumulative Array:")
    print(cum_array)

    # Perform a range sum query
    print("\nSum of values from index 1 to 4:")
    print(cum_array.range_sum(1, 4))

    # Delete a value and display the updated array
    cum_array.delete(4)
    print("\nCumulative Array after deleting index 4:")
    print(cum_array)