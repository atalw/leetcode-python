class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets = ["(", "[", "{"]
        close_brackets = [")", "]", "}"]
        order = []

        for char in s:

            if char in open_brackets:
                order.append(char)

            if len(order) != 0:
                if char in close_brackets:
                    bracket = order[-1]
                    index = open_brackets.index(bracket)

                    if char != close_brackets[index]:
                        return False
                    else:
                        order.pop(-1)
            else:
                return False

        if len(order) == 0:
            return True
        else:
            return False
