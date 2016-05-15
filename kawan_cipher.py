letras = {
  "A":"N",
  "B":"O",
  "C":"P",
  "D":"Q",
  "E":"R",
  "F":"S",
  "G":"T",
  "H":"U",
  "I":"V",
  "J":"W",
  "K":"X",
  "L":"Y",
  "M":"Z",
  "N":"A",
  "O":"B",
  "P":"C",
  "Q":"D",
  "R":"E",
  "S":"F",
  "T":"G",
  "U":"H",
  "V":"I",
  "W":"J",
  "X":"K",
  "Y":"L",
  "Z":"M",
}

class KawanCipher:

  def cifrar(self, mensagem):
    texto_cifrado = ""
    for letra in mensagem:
      achei = False
      for chave, valor in letras.items():
        if chave == letra.upper(): 
          texto_cifrado += letras[letra.upper()]
          achei = True
      if not achei:
        texto_cifrado += letra.upper()
    return texto_cifrado
      
  def decifrar(self, mensagem):
    texto_decifrado = ""
    for letra in mensagem:
      achei = False
      for chave,valor in letras.items():
          if letra.upper() == valor:
            texto_decifrado += chave
            achei = True
      if not achei:
        texto_decifrado += letra
    return texto_decifrado


cipher = KawanCipher()
option = int(input("\nEscolha uma opção: \n1 - Cifrar mensagem \n2 - Decifrar mensagem \n3 - Sair \n"))

while(option < 3):
  if option == 1:
    texto_cifrado = cipher.cifrar(input("\nDigite a mensagem que você deseja cifrar: "))
    print(texto_cifrado)
  elif(option == 2):
    texto_decifrado = cipher.decifrar(input("\nDigite a mensagem que você deseja decifrar: "))
    print(texto_decifrado)
  else:
    exit()
  option = int(input("\nEscolha uma opção: \n1 - Cifrar mensagem \n2 - Decifrar mensagem \n3 - Sair \n" ))

