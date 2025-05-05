from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
app.secret_key = 'archie'

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.getenv("EMAIL"),
    "MAIL_PASSWORD": os.getenv("SENHA")
}

app.config.update(mail_settings)

mail = Mail(app)

class Contato:
    def __init__(self, nome, email, numero, mensagem):
        self.nome = nome
        self.email = email
        self.numero = numero
        self.mensagem = mensagem


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projetos/<path:filename>')
def serve_projetos(filename):
    return send_from_directory("projetos", filename)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['numero'],
            request.form['mensagem']
        )

        msg = Message(
            subject = f'{formContato.nome} te enviou uma mensagem no portifolio',
            sender = app.config.get("MAIL_USERNAME"), 
            recipients= ['brenocolaco@gmail.com', app.config.get("MAIL_USERNAME")],
            body = f'''
            
            {formContato.nome} com e-mail {formContato.email} e telefone para contato {formContato.numero}, te enviou a seguinte mensagem:

            {formContato.mensagem}

            ''' 
        )

        mail.send(msg)
        flash('Mensagem enviada com sucesso!')

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

