
def get_sequence_differences(sequence):
    d = []
    for i in range(len(sequence)-1):
        d.append(sequence[i+1]-sequence[i])

    return d

def sequence_is_all_number(sequence,number):
    for i in sequence:
        if i is not number:
            return False

    return True

def get_difference_lists(sequence):
    difference_lists = []
    difference_lists.append(sequence)

    current_sequence = sequence
    while not sequence_is_all_number(current_sequence,0):
        result_differences = get_sequence_differences(current_sequence)
        difference_lists.append(result_differences)
        current_sequence = result_differences

    # Extrapolate next value for sequence.
    difference_lists[-1].append(0)
    for i in reversed(range(len(difference_lists))):
        if i == 0:
            break

        difference_lists[i-1].append(difference_lists[i-1][-1]+difference_lists[i][-1])

    # Extrapolate previous value for sequence.
    difference_lists[-1].append(0)
    for i in reversed(range(len(difference_lists))):
        if i == 0:
            break

        difference_lists[i-1].insert(0,difference_lists[i-1][0]-difference_lists[i][0])


    return difference_lists

def print_sequence(sequences):
    number_of_rows = len(sequences)
    current_row = 0

    for seq in sequences:
        for i in seq:
            print(str(i) + ' '*2,end='')

        current_row += 1
        print('')

def read_file(filename):
    sequences = []
    with open(filename) as f:
        for line in f:
            sequences.append([])
            splitline = line.split(' ')

            sequence = []
            for number in splitline:
                sequence.append(int(number))

            sequences.append(sequence)

    return sequences

def get_total(which, difference_lists):
    total = 0
    if which is 'back':
        for seq in difference_lists:
            total+= seq[0][-1]
    elif which is 'front':
        for seq in difference_lists:
            total+= seq[0][0]

    return total

def main():
    sequences = read_file('input.txt')
    difference_lists = []
    for seq in sequences:
        difference_lists.append(get_difference_lists(seq))

    print_sequence(get_difference_lists([10, 13, 16, 21, 30, 45]))
    print('Extrapolate forwards total: ' +str(get_total('back', difference_lists)))
    print('Extrapolate backwards total: '+str(get_total('front', difference_lists)))

if __name__ == '__main__':
    main()
