"""
start
get the numbers of sheets
sheets divided by 5
round answer to next number
output result to user
end
"""

import math

def calculate(sheet):
    answer = sheet / 5
    rounded = math.ceil(answer)
    print("sheet is: ", sheet)
    print("the answer is:", answer)
    print("rounded is:", rounded)
    print("========================================")
    return rounded

    output = calculate(16)
    print ("the answer of stamps needed is:", output)