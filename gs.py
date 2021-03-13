import random
import string

tamanho = int(input('DIGITE O TAMANHO DE SENHA QUE VOCÊ DESEJA: '))

chars = string.ascii_letters + string.digits + 'Ç!@#$%&*()-=+,;:/?'

rnd = random.SystemRandom()

print('' .join(rnd.choice(chars) for i in range(tamanho)))
