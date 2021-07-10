def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        sub_string = ""
        for char in string[i:i+k]:
            sub_string += char if char not in sub_string else ""
        print(sub_string)

if __name__ == '__main__':
    merge_the_tools("AABCAAADAEF", 4)