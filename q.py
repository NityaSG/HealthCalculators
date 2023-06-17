def get_longest_distance(input1, input2):
    target_char = input2
    longest_distance = -1
    prev_index = -1
    distinct_chars = set()

    for i, char in enumerate(input1):
        if char == target_char:
            if prev_index != -1:
                distance = i - prev_index - 1
                if distance > longest_distance:
                    longest_distance = distance
            prev_index = i
            distinct_chars.clear()  # Clear distinct_chars set after each occurrence of the target character
        elif char != ' ':
            distinct_chars.add(char)

    if prev_index == -1 or longest_distance == -1 or len(distinct_chars) < 1:
        return -1

    distance = len(input1) - prev_index - 1
    if distance > longest_distance:
        longest_distance = distance

    return longest_distance

input1 = "my name is granar"
input2 = "a"

longest_distance = get_longest_distance(input1, input2)
print("Longest Distance:", longest_distance)
