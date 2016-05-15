letras = {"A":"N","B":"O","C":"P","D":"Q","E":"R","F":"S",
"G":"T","H":"U","I":"V","J":"W","K":"X","L":"Y","M":"Z"}

class KawanCipher:

  def __int__():

  def cifrar(mensagem):
    texto_cifrado = ""
    for letra in mensagem:
      if letra == " ":
        texto_cifrado += " "
      else:
        texto_cifrado += letras[letra.upper()]
    return texto_cifrado
      
  def decifrar(mensagem):
    texto_decifrado = ""
    for letra in mensagem:
      if letra == " ":
        texto_decifrado += " "
      else:
        for chave,valor in letras.items():
          if letra == valor:
            texto_decifrado += chave
    return texto_decifrado

cipher = KawanCipher
print(texto_cifrado = cipher.cifrar(input("\nDigite a mensagem que você deseja cifrar: ")))
print(texto_decifrado = cipher.decifrar(input("\nDigite a mensagem que você deseja decifrar: ")))

    
