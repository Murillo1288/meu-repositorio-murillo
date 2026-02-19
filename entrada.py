entrada = input()

print(entrada)

nome = input('Qual o seu nome? ')
senha = input('Qual a sua senha? ')
dominio = input('Qual o seu dominio? ')
print('ola ',nome, ', seja bem vindo ao meu mundo') 
print('Sua senha é: ',  senha)
print('o seu dominio é: ', dominio)


email = nome + '@' + dominio
print('seu e-mail é :', email)

palavra = 'maça'
#colocar a string como toda maiuscúla
print('colocando o texto em maiuscúla: ', palavra.upper())

PALAVRA = 'MAÇA'
#colocar a string como toda minuscula
print('colocando o texto em minuscula: ', PALAVRA.lower())  

#contar caracter da string 
palavra_contar = 'banana'
print('contar a letra b', palavra_contar.count('b') )
print('contar a letra a', palavra_contar.count('a') )
print('contar a letra n', palavra_contar.count('n') )

x = palavra_contar.count('x')
print('a palavra x foi contada ', x)

print(email)
a_c = email.count('a')
e_c = email.count('e')
i_c = email.count('i')
o_c = email.count('o')
u_c = email.count('u')
nova_senha = 'a' + str(a_c) + 'e' + str(e_c) + 'i' + str(i_c) + 'o' + str(o_c) + 'u' + str(u_c)
print(nova_senha)


