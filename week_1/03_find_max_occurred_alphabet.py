input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for v in string:
        if (v.isalpha()):
            alphaIndex = ord(v) - ord('a')
            alphabet_occurrence_array[alphaIndex] += 1;

    max_occurrence = 0;
    max = alphabet_occurrence_array[0]

    for index in range(len(alphabet_occurrence_array)):
        if max < alphabet_occurrence_array[index] :
            max = alphabet_occurrence_array[index]
            max_occurrence = index


    return chr(ord('a') + max_occurrence)


result = find_max_occurred_alphabet(input)
print(result)