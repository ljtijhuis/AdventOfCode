from src.file_utils import read_file

class CircuitBoard:
    def __init__(self) -> None:
        self.operations = dict[str, str]()
        self.values = dict[str, int]()

    def add_operation(self, operation: str) -> None:
        op, key = operation.split(" -> ")
        self.operations[key] = op
        self.values[key] = None

    def reset(self) -> None:
        for key in self.values.keys():
            self.values[key] = None

    def get_value(self, key: str) -> int:
        if key.isnumeric():
            return int(key)

        if self.values[key] != None:
            return self.values[key]
        
        op = self.operations[key]
        if op.isnumeric():
            self.values[key] = int(op)
            return int(op)
        
        value = None

        '''
        x AND y -> d
        '''    
        if "AND" in op:
            left, right = op.split(" AND ")
            value = self.get_value(left) & self.get_value(right)
        
        '''
        x OR y -> e
        '''
        if "OR" in op:
            left, right = op.split(" OR ")
            value = self.get_value(left) | self.get_value(right)

        '''
        x LSHIFT 2 -> f
        '''
        if "LSHIFT" in op:
            left, shift_value = op.split(" LSHIFT ")
            value = self.get_value(left) << int(shift_value)
        
        '''
        y RSHIFT 2 -> g
        '''
        if "RSHIFT" in op:
            left, shift_value = op.split(" RSHIFT ")
            value = self.get_value(left) >> int(shift_value)
        
        '''
        NOT x -> h
        '''
        if "NOT" in op:
            _, left = op.split(" ")
            value = 65535 + ~self.get_value(left) + 1
        
        if value == None:
            value = self.get_value(op)
        
        self.values[key] = value

        return value
        

if __name__ == "__main__":
    input = read_file('/../input/day_7.txt')
    lines = input.splitlines()

    circuit_board = CircuitBoard()
    for operation in lines:
    #     print(operation)
        circuit_board.add_operation(operation)

    val = circuit_board.get_value('a')
    print(val)

    circuit_board.add_operation(str(val) + ' -> b')
    circuit_board.reset()
    print(circuit_board.get_value('a'))