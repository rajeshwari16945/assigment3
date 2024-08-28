def evaluate(expression):
    expression = expression.replace(" ", "")  # Remove spaces for easier parsing

    # Base case: if the expression is a single number, return it as a float
    if expression.isdigit() or (expression.startswith('-') and expression[1:].isdigit()):
        return float(expression)
    
    # Recursive case: parse and evaluate the expression
    for operator in ['+', '-', '*', '/']:
        parts = split_expression(expression, operator)
        if parts:
            left, right = parts
            if operator == '+':
                return evaluate(left) + evaluate(right)
            elif operator == '-':
                return evaluate(left) - evaluate(right)
            elif operator == '*':
                return evaluate(left) * evaluate(right)
            elif operator == '/':
                return evaluate(left) / evaluate(right)

    raise ValueError("Invalid expression")

def split_expression(expression, operator):
    depth = 0  # To track parentheses depth
    for i in range(len(expression) - 1, -1, -1):  # Traverse the expression from right to left
        if expression[i] == ')':
            depth += 1
        elif expression[i] == '(':
            depth -= 1
        elif expression[i] == operator and depth == 0:
            return expression[:i], expression[i+1:]
    return None

# Example usage
if __name__ == "__main__":
    while True:
        expr = input("Enter an arithmetic expression (or type 'exit' to quit): ")
        if expr.lower() == 'exit':
            break
        try:
            result = evaluate(expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")
