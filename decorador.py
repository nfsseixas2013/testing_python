
def decora_soma(func):
    def operacao(a,b):
        print(f"O resultado da impressão é: {func(a,b)}")
    return operacao
    

@decora_soma
def soma(a,b):
    return a+b

@decora_soma
def sub(a,b):
    return a-b

soma(5,6)
sub(10,1)