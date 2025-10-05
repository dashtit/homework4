def validate_expression(expression):
    for char in expression:
        if not char.isdigit() and char not in '+-*/%(). ':
            return False, char
    return True, None


def evaluate_expression(expression):
    is_valid, invalid_char = validate_expression(expression)
    if not is_valid:
        return f'Invalid char --> {invalid_char}'
    try:
        return eval(expression)
    except ZeroDivisionError:
        return 'Division by zero.'
    except SyntaxError:
        return 'Syntax error in the expression.'
