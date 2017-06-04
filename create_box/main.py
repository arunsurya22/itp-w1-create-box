"""This is the entry point of the program."""

def create_box(height, width, character):
    final_answer = ''
    for row in range(height):

        for col in range(width):
            final_answer += character
        final_answer += '\n'
    return final_answer


def empty_box(height, width, character):
    gap = " "
    final_answer = ''
    for row in range(height):
        if row == 0 or row == height-1:
           final_answer += width * character + '\n'
        else:
           final_answer += (character + (gap*(width-2)) + character + '\n')
    return final_answer


if __name__ == '__main__':
    create_box(3, 4, '*')
