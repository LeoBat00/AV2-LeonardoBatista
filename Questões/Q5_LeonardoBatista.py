#/ Trabalho AV2 - Programação Funcional - Questão 2
#/ Nome: Leonardo Mendonça Teixeira Batista 
#/ Matrícula: 2210392
#/ Professor: Samuel Lincoln 

#/ Por conta dos inputs que fiz na primeira questão, assim que o usuario consegue sucesso ao logar 
#/ a página vai ficar carregando, pois estara esperando as respostas no terminal para continuar o processo

#/ É preciso, também, comentar o testar_codigo() na primeira questão para que não ocorra duplicidade.

from flask import Flask, request, render_template
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Q1_LeonardoBatista import *

app = Flask(__name__, template_folder='templates_folder')

welcome = lambda: f'WELCOME {request.form["username"]}!{testar_codigo()}'
wrong = lambda: 'Senha errada! ' + print_crypt_info()
invalid = lambda: 'Usuário não cadastrado! '
print_crypt_info = lambda: f'\n Apenas para verificação\nSenha inserida: {encrypt_password(request.form["password"])}, Senha no banco: {users.get(request.form["username"])}\n '
password_matches = lambda dic: decrypt_password(dic.get(request.form["username"])) == request.form["password"]
check_password = lambda: welcome() if password_matches(users) else wrong()
check_if_user_exists = lambda: check_password() if request.form["username"] in users else invalid()
reqresp = lambda: check_if_user_exists() if request.method == 'POST' else render_template('index.html')


# Criptografia Simétrica utilizando o algoritmo de AES
key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_password(password):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_password = pad(password.encode(), 16)  
    ciphertext = cipher.encrypt(padded_password)
    return ciphertext.hex()
users = {
    "leonardo": encrypt_password("123"),  
    "samuel": encrypt_password("123")    
}
def decrypt_password(ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_password = cipher.decrypt(bytes.fromhex(ciphertext))
    return unpad(decrypted_password, 16).decode()  

# Professor, tentei fazer como o senhor fez no vídeo, porém não sei o motivo mas não estava achando o index.html, então fiz dessa forma.

@app.route('/', methods=['GET', 'POST'])
def index():
    return reqresp()
@app.route('/index/', methods=['GET', 'POST'])
def index_page():
    return reqresp()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
