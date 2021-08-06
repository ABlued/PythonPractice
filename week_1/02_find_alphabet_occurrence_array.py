def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for v in string:
        if(v.isalpha()) :
            alphaIndex = ord(v) - ord('a')
            alphabet_occurrence_array[alphaIndex] += 1;

    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))