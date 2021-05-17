import re
from TelefonesBr import TelefonesBr

telefone = "556126481234"

telefone_objeto = TelefonesBr(telefone)
# padrao = "([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})"
# resposta = re.findall(padrao, telefone)
# print(resposta)

print(telefone_objeto)