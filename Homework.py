def odd_even_finder(num1, num2):

    odd = []
    even = []

    for num in range(num1, num2 + 1):

        square = num**2

        if square % 2 == 0:

            even.append(square)
        else:
            odd.append(square)

    print(f"\n The even numbers in your list were the following:\n{even}")
    print(f"\n The odd numbers in your list were the following:\n{odd}")



num1 = int(input("Please put a numerical value: "))
num2 = int(input("\nPlease put another numerical value: "))


odd_even_finder(num1, num2)