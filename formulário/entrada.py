'''
Programa de entrada de dados de alunos de universidade
'''
nome = input('Qual o seu nome?')
sobrenome = input('Qual o seu sobrenome?')
data_de_nascimento = input('Qual sua data de nascimento?')
Universidade = input('Qual sua Universidade?')

e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + Universidade + '.br'
senha = 'a' + str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))

print('O seu e-mail é: {}'.format(e_mail))
print('A sua senha é: {}'.format(senha))

print('A sua senha e e-mail são: {}:{}'.format(senha.e-mail))



