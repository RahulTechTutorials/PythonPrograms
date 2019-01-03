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
            return None
    
    def top(self):
        if not ( self.isEmpty() ):
            return self.values[-1]
        else:
            print('Top not available')
            return None
            
    
    def size(self):
        return len(self.values)
    
    def __str__(self):
        stringrep = ''
        for i in reversed(self.values):
            stringrep += str(i) + '\t'
        return stringrep
            

def InfixToPostfix(exp):
    '''((7-5)*6+4)'''
    precedence = {'+':1,'-':1,'*':2,'/':2}
    operand    = '0123456789'
    stk = stack()
    result = ''
    
    for symbol in exp:
        if symbol =='(' :
            stk.push(symbol)
        elif symbol == ')':
            val = stk.pop()
            while val != '(':
                result += str(val)
                val = stk.pop()
        elif symbol in operand:
            result += symbol
        elif symbol in precedence:
            if not(stk.isEmpty()):
                stkTop = stk.top()
            while not(stk.isEmpty()) and stkTop != '(' and precedence[symbol] <= precedence[stkTop]:
                result += stkTop
                stk.pop()
                if not(stk.isEmpty()) : stkTop = stk.top()
            stk.push(symbol)
    while not(stk.isEmpty()):
        result += stk.pop()
    return result

        
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
    
    ##exp = input('Please enter the expression in the Postfix style with only single digit operands')
    ##print(EvaluatePostFixExp(exp))
    
    exp = input('Please enter the expression in the infix style with only single digit operands')
    result = InfixToPostfix(exp)
    print('The infix expression is: ',exp)
    print('The Postfix expression is: ',result)
    print('The result is: ',EvaluatePostFixExp(result))
    

if __name__ == '__main__':
    main()
            
