def calculate_n50(lengths):
    sorted_lengths = sorted(lengths, reverse=True)
    total_length = sum(sorted_lengths)
    half_length = total_length / 2

    cumulative_length = 0
    for length in sorted_lengths:
        cumulative_length += length
        if cumulative_length >= half_length:
            return length

    return None  # N50 not found


# Example usage
contig_lengths = [756,100,800,1000]
n50 = calculate_n50(contig_lengths)
print("N50 value:", n50)
