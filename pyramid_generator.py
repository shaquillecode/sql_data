"""
Write a program that prints the following

*
* *
* * *
* * * *
* * * * *
* * * * *
* * * *
* * *
* *
*

part 2:
replace the middle of any odd numbered row with a smilie emoji "😊" in the middle
"""

#1
def generate_pyramid(rows=5):
    '''Generates A pyramid'''
    pyramid_one = ["*" * i for i in range(1, rows + 1) ]
    pyramid_two  = ["*" * i for i in range(rows, 0, -1) ]
    return pyramid_one + pyramid_two

#2
def add_smile(_pyramid):
    '''Adds a Smile to odd numbered row'''
    new_pyramid = []
    for row in _pyramid:
        if len(row) % 2 != 0 and row != '\n':
            new_pyramid.append(row[:int(len(row)/2)] + '😊' + row[int(len(row)/2) + 1:])
        else:
            new_pyramid.append(row)
    return new_pyramid


if __name__ == '__main__':
    print(generate_pyramid())
    smiles = add_smile(generate_pyramid()) 
    print(smiles)
    for smile in smiles:
        print(smile)
