from pilha.Node import Node

class Pilha:
    def __init__(self):
        self.top = None  

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def push(self, value):
        new_node = Node(value)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None  
        removed_node = self.top
        self.top = self.top.next
        return removed_node.value 

    def is_empty(self):        
        return self.top is None
    
    def exibir(self):
        currentNode = self.top
        while currentNode is not None:
            print(currentNode.value)
            currentNode = currentNode.next
    
    def validarParenteses(self,strPar):
       
        pilha = Pilha()

        for c in strPar:
            if c == '(':
                pilha.push(c)
            elif c == ')':
               if pilha.is_empty():
                   return False
               pilha.pop()
        return pilha.is_empty()
    
    def inverteString(self,palavraInverter):
        pilha = Pilha()

        for aux in palavraInverter:
            pilha.push(aux)

        strInver = ""

        while not pilha.is_empty():
            strInver += pilha.pop()

        return strInver
    
    def expressaoPosFixa(self,sequencia):
        pilha = Pilha()

        for aux in sequencia:
            if aux.isdigit() or (aux[0] == "-" and aux[1:].isdigit()):
                pilha.push(int(aux))
            else:
                num2 = pilha.pop()
                num1 = pilha.pop()
                if aux == '+':
                    resultado = num1 + num2
                elif aux == '-':
                    resultado = num1 - num2
                elif aux == '*':
                    resultado = num1 * num2
                elif aux == '/':
                    resultado = num1 / num2
            
                pilha.push(resultado)
        
        return pilha.pop()

