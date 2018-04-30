
# solution 1
# def chessboard(n = 8):
    # for n in range(1, n):
    #     if n % 2 == 0:
    #         print(" # # # #")
    #     else:
    #         print('# # # # ')

# solution 2
from itertools import cycle
# ''.join(fig for fig, _ in zip (cycle(#['##', '  ']), range(8))])

# solution 3
def chessboard(n=8):
    for i in range(n):
        # ''.join([fig for fig, _ in zip(cycle(['##', '  ']), range(8))])
        for j in range(n):
            if (j + i % 2) % 2:
                print('##', end='')
            else:
                print('  ', end='')
        print()

chessboard()
print()
chessboard(10)
print()
chessboard(11)