class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                stack.append(i)
            
                  
            else:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if i == "+":
                    stack.append(str(val1 + val2))
                elif i == "-":
                    stack.append(str(val2 - val1))
                elif i == "*":
                    stack.append(str(val1 * val2))
                else:
                    stack.append(str(int(val2 / val1)))
        return int(stack[0])