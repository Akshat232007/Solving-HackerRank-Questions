if __name__ == "__main__":
    height, width = map(int, input().split())

    for i in range(1, height, 2):
        pattern = ".|." * i
        print(pattern.center(width, "-"))

    print("WELCOME".center(width, "-"))

    for i in range(height - 2, 0, -2):
        pattern = ".|." * i
        print(pattern.center(width, "-"))