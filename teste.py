#3
def is_in_fibonacci(number): 
  a, b = 0, 1 while b < number: a, b = b, a + b 
  return b == number or number == 0

input_number = int(input("Informe um número: "))

if is_in_fibonacci(input_number): 
  print(f"O número {input_number} pertence à sequência de Fibonacci.")   
else: 
  print(f"O número {input_number} não pertence à sequência de Fibonacci.")

#5
def reverse_string(string): 
  return ''.join(string[i] for i in range(len(string) - 1, -1, -1))

string_original = input("Insira uma string: ") 
string_reversed = reverse_string(string_original) 
print("String original:", string_original) 
print("String reversa:", string_reversed)
