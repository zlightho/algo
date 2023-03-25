operations_history  = ['']
def BastShoe(command:str) -> str:
    operation_and_value = command.split(' ',1)
    operation, value = operation_and_value[0], operation_and_value[1]
    global operations_history
    if operation == '1':
        operations_history.append((operations_history[-1] + value))
    
    elif operation == '2':
        operations_history[-1] = operations_history[-1][:len(operations_history[-1])-(int(value))]
    elif operation == '3':
        if value >= len(operations_history[-1]):
            return ''
        return operations_history[-1][value]
    else:
        return ''
    return operations_history[-1]
print(BastShoe('1 Привет'))
print(BastShoe('1  , Мир!'))
print(BastShoe('1 ++'))
print(BastShoe('2 2'))
