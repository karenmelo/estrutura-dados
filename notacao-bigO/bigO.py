#Implementacao1
import timeit


def soma1(n):
  soma = 0
  for i in range(n +1):
    soma += i

  return soma

print(soma1(10))


#implementacao2
def soma2(n):
  return (n*(n+1))/2



print(soma2(10)) 