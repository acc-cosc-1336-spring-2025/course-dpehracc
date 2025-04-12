#
def get_p_distance(list1, list2):
    differences = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            differences += 1
    return differences / len(list1)

def get_p_distance_matrix(dna_list):
    size = len(dna_list)
    matrix = []

    for i in range(size):
        row = []
        for j in range(size):
            distance = get_p_distance(dna_list[i], dna_list[j])
            row.append(round(distance, 5))
        matrix.append(row)

    return matrix