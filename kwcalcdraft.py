def get_user_input() -> (float, str, float):
    print("Enter the first number, or (x) to exit: ")
    input_num_one = input()
    if input_num_one.upper() == "X":
        quit()

    print("Enter the operation you want (+, -, *, /), or (x) to exit: ")
    operator_input = input()
    if operator_input.upper() == "X":
        quit()

    print("Enter the second number, or (x) to exit: ")
    input_num_two = input()
    if input_num_two.upper() == "X":
        quit()

    return float(input_num_one), operator_input, float(input_num_two)


def next_get_user_input() -> (str, float):
    print("Enter the operation you want (+, -, *, /), or (x) to exit: ")
    next_operator_input = input()
    if next_operator_input.upper() == "X":
        quit()

    print("Enter another number, or (x) to exit: ")
    input_num_two = input()
    if input_num_two.upper() == "X":
        quit()

    return next_operator_input, float(input_num_two)


def process_user_input(process_num_one: float, operator: str, process_num_two: float) -> float:
    if "+" == operator:
        return process_num_one + process_num_two
    if "-" == operator:
        return process_num_one - process_num_two
    if "*" == operator:
        return process_num_one * process_num_two
    if "/" == operator:
        return process_num_one / process_num_two


first_op_completed = False
stored_number = ()
while True:
    if first_op_completed is False:
        user_input = get_user_input()
        num_one = user_input[0]
        op = user_input[1]
        num_two = user_input[2]
        result = process_user_input(num_one, op, num_two)
        stored_number = result
        first_op_completed = True
        print(result)

    else:
        next_user_input = next_get_user_input()
        next_num_one = stored_number
        op = next_user_input[0]
        next_num_two = next_user_input[1]
        result = process_user_input(next_num_one, op, next_num_two)
        stored_number = result
        print(result)
