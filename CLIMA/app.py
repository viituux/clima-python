from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy  # IMPORTANTE: Faltava importar isso
from datetime import datetime            # IMPORTANTE: Faltava importar isso
from previcao import PrevisaoOpenMeteo

app = Flask(__name__)

# Configuração do Banco de Dados
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///clima.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Modelo da Tabela (Removi a coluna 'dados' para não dar erro)
class Historico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(100), nullable=False)
    temperatura = db.Column(db.Float, nullable=False)
    data_hora = db.Column(db.DateTime, default=datetime.now) 

sistema = PrevisaoOpenMeteo()

@app.route("/", methods=["GET", "POST"])
def index():
    dados = None
    erro = None

    if request.method == "POST":
        cidade = request.form.get("cidade")
        resposta = sistema.buscar_cidade(cidade)  

        if "erro" in resposta:
            erro = resposta["erro"]
        else:
            dados = resposta
            
            # Salvando no Banco
            try:
                nova_busca = Historico(
                    cidade=dados["cidade"],
                    temperatura=dados["temperatura"]
                    # A data_hora é preenchida sozinha pelo default=datetime.now
                ) 
                db.session.add(nova_busca)
                db.session.commit()
            except Exception as e:
                print(f"Erro ao salvar no banco: {e}")

    # Recuperando as últimas 5 buscas para mostrar na lista
    historico = Historico.query.order_by(Historico.data_hora.desc()).limit(5).all()
    
    return render_template("index.html", dados=dados, erro=erro, historico=historico)

if __name__ == "__main__":
    # CRUCIAL: Cria o arquivo do banco se não existir
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)