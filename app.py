from flask import Flask, render_template
from conexao import conectar

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template("index.html",clientes=clientes)

        #return f'conexão realizada com sucesso: {resultado}'
    except Exception as e:
        return f'Erro ao conectar {e}'
    
if __name__ == '__main__':
    app.run(debug=True)