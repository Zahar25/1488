def num(n, list):
    for i in list:
        if n == i:
            return True
        else:
            return False


list = input("Enter list: ").replace(" ", "").split(",")
n = input("Enter number: ")
print(num(n, list))
