class GameZiMu():
    def a(self):
        for i in range(4):
            for j in range(4 - i):
                print(" ", end="")
            for m in range(i + 1):
                if i == 3 and (m == 1 or m == 2):
                    print("  ", end="")
                else:
                    print("* ", end="")
            print()
    def d(self):
        for i in range(4):
            for j in range(3):
                if j == 0:
                    print(" * ", end="")
                elif i == 0 and j == 1:
                    print(" * ", end="")
                elif i == 3 and j == 1:
                    print(" * ", end="")
                elif j == 2 and (i == 1 or i == 2):
                    print("  *", end="")
                else:
                    print(" ", end="")
            print()
    def c(self):
        for i in range(4):
            for j in range(3):
                if j == 0 and (i == 1 or i == 2):
                    print("* ", end="")
                elif j == 1 and (i == 0 or i == 3):
                    print("* ", end="")
                elif j == 2 and (i == 0 or i == 3):
                    print(" * ", end="")
                else:
                    print("  ", end="")
            print()
    def g(self):
        for i in range(4):
            for j in range(4):
                if j == 0 and (i == 1 or i == 2):
                    print("* ", end="")
                elif j == 1 and (i == 0 or i == 3):
                    print("* ", end="")
                elif j == 2 and (i == 0 or i == 2 or i == 3):
                    print("* ", end="")
                elif j == 3 and (i == 0 or i == 2 or i == 3):
                    print("* ", end="")
                else:
                    print("  ", end="")
            print()
    def m(self):
        for i in range(4):
            for j in range(4 - i):
                print(" ", end="")
            for k in range(i + 1):
                if k == 0:
                    print("* ", end="")
                if k == 1 and i == 1:
                    print("* ", end="")
                if k == 2 and i == 2:
                    print(" * ", end="")
                if k == 3:
                    print("  * ", end="")
                else:
                    print(" ", end="")
            for j in range(3 - i):
                print("  ", end="")
            for k in range(i + 1):
                if k == 0:
                    print("  * ", end="")
                if k == 1 and i == 1:
                    print("* ", end="")
                if k == 2 and i == 2:
                    print("  * ", end="")
                if k == 3:
                    print("     * ", end="")
                else:
                    print("", end="")
            print()