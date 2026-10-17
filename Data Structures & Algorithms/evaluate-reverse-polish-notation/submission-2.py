class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ["+", "-", "*", "/"]:
                second_operand = stack.pop()
                first_operand = stack.pop()

                if t == "+":
                    stack.append(first_operand + second_operand)
                elif t == "-":
                    stack.append(first_operand - second_operand)
                elif t == "/":
                    stack.append(int(first_operand / second_operand))
                elif t == "*":
                    stack.append(first_operand * second_operand)

            else:
                stack.append(int(t))
        
        return int(stack.pop())
        