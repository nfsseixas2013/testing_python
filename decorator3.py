def decorador(func):
    def multiplica(a,b):
        return(a*b)
    return multiplica

@decorador
def soma(a,b):
    return a+b

print(soma(10,2))