from flask import Flask, render_template
from flask.globals import request


#criando site
app = Flask(__name__)

#criando a primeira página do site
@app.route("/")
def homepage():
    return (render_template("homepage.html"))

#criando o calculo e utilizando método get e post para mostrar resultados   
@app.route("/resultado", methods= ['GET'])
def resultado():
    renda = int(request.args.get("renda"))
    valor = int(request.args.get("valor"))
    t = int(request.args.get("tempo"))
    i = 1.5097
    if renda < 1320:
        resultado = "Negado"
        return render_template("resultado.html", resultado = resultado)
    else:
        M = valor*(1+i)**t
        if (M/t*12) < (0.20 * renda):
            resultado = "Aprovado"
            return render_template("resultado.html", resultado = resultado)
        else:
            resultado = "Negado"
            return render_template("resultado.html", resultado = resultado)
   


#colocando o site para rodar
app.run(debug=True)
