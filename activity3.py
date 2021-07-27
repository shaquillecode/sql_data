from pprint import pprint
# """
# write a program that prints the following
# ```
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * 
# * * * *
# * * *
# * *
# *
# ``
# 1) do it using a for loop 
# 2) do it using a list comp. 
# part 2:
# replace the middle of any odd numbered row with a smilie emoji "😊" in the middle
# """

    
def generate_pyramid_iterative(rows=7):
    pyramid_entries = []
    for row in range(1, rows + 1):
        pyramid_entries.append("*" * row)
    pyramid_entries.append("\n")

    for row in range(rows, 0,-1):
        pyramid_entries.append("*" * row)
    return pyramid_entries

def generate_pyramid_list_comp(rows=5):
    pyramid_one = ["*" * i for i in range(1, rows + 1) ]
    pyramid_two  = ["*" * i for i in range(rows, 0, -1) ]
    return pyramid_one + ['\n'] + pyramid_two 

def generate_pyramid_list_using_copy(rows=5):
    pyramid_one = ["*" * i for i in range(1, rows + 1) ]
    pyramid_two = pyramid_one[:]
    pyramid_two.reverse()
    return pyramid_one + ['\n'] + pyramid_two


def add_smilies(pyramid):
    print("adding smilies...")
    new_pyramid = []
    for row in pyramid:
        if len(row) % 2 != 0 and row != '\n':
            new_pyramid.append(row[:int(len(row)/2)] + '😊' + row[int(len(row)/2) + 1:])
        else:
            new_pyramid.append(row)
    return new_pyramid

def add_smiles(list_comp):
    return [row for row in pyramid if len(row) % 2 != 0]

if __name__ == '__main__':
    #pyramid = generate_pyramid_iterative()
    #pyramid = generate_pyramid_list_using_copy()
    pyramid = generate_pyramid_list_comp()
    pprint(pyramid)
    #pprint(pyramid)
    smilies = add_smilies(pyramid)
    for smile in smilies:
        print(smile)
    #pprint(generate_pyramid_list_comp())