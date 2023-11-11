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
    D = int(request.args.get("valor"))
    t = int(request.args.get("tempo"))
    j = 0.07
    parcela = round((D*(((1+j)**t)*j/(((1+j)**t)-1))), 2)
    if renda < 1320:
        resultado = "Negado"
        return render_template("resultado1.html", resultado = resultado)
    elif (parcela) < (0.20 * renda):
        resultado = "Aprovado"
        total = round((t * parcela), 2)
        juros = round((total - D), 2)
        return render_template("resultado.html", resultado = resultado, parcela = parcela, total = total, juros = juros)                 
    else:
         resultado = "Negado"
         return render_template("resultado1.html", resultado = resultado)


#colocando o site para rodar
app.run(debug=True)
