def add(first, second):
    return first + second

def subtract(first, second):
    return first - second

def multiply(first, second):
    return first * second

def divide(first, second):
    return first / second    

def operate(operation, first_num, second_num):
    if operation == "+" or operation == "add":
        return add(first_num, second_num)
    elif operation == "-" or operation == "subtract":
        return subtract(first_num, second_num)
    elif operation == "*" or operation == "multiply":
        return multiply(first_num, second_num)
    elif operation == "/" or operation == "divide":
        return divide(first_num, second_num)
    
# [3, "*", 3, "-", 4, "-", 1, *, 5]
# [2, "+", 10, "/, 5"]
# [2, "+", 2]

def main():
    result = 0
    opr_val = []
    
    print("Dobrodošli u Katkulator")
    while True:
        operation = ''
        if result == 0:
            opr_val.append(int(input("Upišite broj: ")))
        else:
            opr_val.append(result)
        while operation != '=':
            operation = input("Koju operaciju želite obaviti?: ")
            if operation != '=':
                opr_val.append(operation)
                opr_val.append(int(input("Upišite broj: ")))
        while True:
            new_opr_val = []
            dirty_list = clean_list(opr_val, new_opr_val, False)
            opr_val = new_opr_val
            if not dirty_list:
                break
        # zbroji i/ili oduzmi sve elemente
        while True:
            new_opr_val = []
            calculate_result(opr_val, new_opr_val, False)
            opr_val = new_opr_val
            if len(opr_val) == 2:
                break
        result = opr_val[0]

        print(f"Rezultat operacije je {result}")

        choice = input("Da li želite još katkulirati?\nUnesite n za prekid\nUnesite CE za stavljanje rezultata na 0\n")

        if choice.lower() == "n":
            break   
        elif choice.lower() == "ce":
            result = 0
        else:
            opr_val = []

    
# [2, "+", 5, "*", 2, "/", 5]
# [2, "+", 10, "/, 5"]
# [2, "+", 2]

def clean_list(opr_val, new_opr_val, dirty_list):
    for val in opr_val:
        if not dirty_list:
            if val == '*' or val == '/':
                dirty_list = True
                idx = opr_val.index(val)
                val_before = opr_val[idx - 1]
                val_after = opr_val[idx + 1]
                new_opr_val.pop()
                new_opr_val.append(operate(val, val_before, val_after))
                opr_val.pop(idx + 1)
            else:
                new_opr_val.append(val)
        else:
            new_opr_val.append(val)

    return dirty_list

def calculate_result(opr_val, new_opr_val, again):
    for val in opr_val:
        if val == '+' or val == '-':
            again = True
            idx = opr_val.index(val)
            val_before = opr_val[idx - 1]
            val_after = opr_val[idx + 1]
            new_opr_val.pop()
            new_opr_val.append(operate(val, val_before, val_after))
            new_opr_val.append(opr_val[idx])
            opr_val.pop(idx)
            opr_val.pop(idx)
        else:
            new_opr_val.append(val)
    return again


if "__main__" == __name__:
    main()