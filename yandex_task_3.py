cellMap = dict()
result = []

cells = []

triedCells = []


for i in range(int(input())):
    cells.append(input())


def getResults(cells):
    for i in range(len(cells)):
        cellValue = getResult(cells[i], i)
        if type(cellValue) != int:
            return -1

        result.append(cellValue)
        cellMap[f"C{i+1}"] = cellValue

    return result


def getResult(cell, indx):
    cellType, cellValue = cell.split(' ')

    if cellType == '1':
        return int(cellValue)

    if indx in triedCells:
        return ArithmeticError()

    triedCells.append(indx)

    operands = cellValue.replace('+', ' ').replace('-', ' ').replace('*', ' ').split()
    operators = [i for i in cellValue if i in "+-*"]

    for i in range(len(operands)):
        if cellMap.get(operands[i]):
            operands[i] = cellMap[operands[i]]
        else:
            operand_num = getResult(cells[int(operands[i][1:]) - 1], int(operands[i][1]) - 1)
            if type(operand_num) != int:
                return ArithmeticError()
            operands[i] = getResult(cells[int(operands[i][1:]) - 1], int(operands[i][1]) - 1)

    deletedNum = 0

    for i in range(len(operators)):
        operator = operators[i]
        if operator == '*':
            operands[i - deletedNum] = operands[i - deletedNum] * operands[i - deletedNum + 1]
            del operands[i - deletedNum + 1]
            deletedNum += 1

    operators = list(filter(lambda x: x != "*", operators))

    deletedNum = 0

    for i in range(len(operators)):
        operator = operators[i]
        if operator == '+':
            operands[i - deletedNum] = operands[i - deletedNum] + operands[i - deletedNum + 1]
            del operands[i - deletedNum + 1]
            deletedNum += 1

        if operator == '-':
            operands[i - deletedNum] = operands[i - deletedNum] - operands[i - deletedNum + 1]
            del operands[i - deletedNum + 1]
            deletedNum += 1

    return operands[0]


result = getResults(cells)

if result == -1:
    print(-1)
else:
    print(*result, sep='\n')