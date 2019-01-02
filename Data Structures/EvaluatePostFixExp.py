class stack:
    def __init__(self):
        self.values = list()
    
    def push(self,element):
        self.values.append(element)
    
    def isEmpty(self):
        return len(self.values) == 0
    
    def pop(self):
        if not ( self.isEmpty() ):
            return self.values.pop()
        else:
            print('Stack Underflow')
            return none
    
    def top(self):
        if not ( self.isEmpty() ):
            return self.values[-1]
        else:
            print('Stack Underflow')
            return none
    
    def size(self):
        return len(self.values)
    
    def __str__(self):
        stringrep = ''
        for i in reversed(self.values):
            stringrep += str(i) + '\t'
        return stringrep
            

        
def EvaluatePostFixExp(exp):
    stk = stack()
    operators = ['+','-','*','/']
    for symbol in exp:
        if symbol in operators:
            operator2 = stk.pop()
            operator1 = stk.pop()
            result = str(eval(operator1 + symbol + operator2))
            stk.push(result)
        else:
            stk.push(symbol)
    result = int(stk.pop())
    return result
    
        
def main():
    """Limitation is that only one digit Intergers can 
      be calculated and Postfix expression needs to be fed"""
    
    exp = input('Please enter the expression in the Postfix style with only single digit operands')
    print(EvaluatePostFixExp(exp))
        

if __name__ == '__main__':
    main()
            
