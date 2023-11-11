from flask import Flask, render_template
from flask.globals import request


#criando site
app = Flask(__name__)

#criando a primeira página do site
@app.route("/")
def homepage():
    return (render_template("homepage.html"))

#criando o calculo e utilizando método get para mostrar resultados   
@app.route("/resultado", methods= ['GET'])
def resultado():
    #Solicitação de renda, valor de empréstimo(D), número de parcelas(t) e juros. 
    renda = int(request.args.get("renda"))
    D = int(request.args.get("valor"))
    t = int(request.args.get("tempo"))
    j = 0.07
    #Equação para o cálculo de valor de parcela utilizado pela tabela price retirado da seguinte fonte https://mundoeducacao.uol.com.br/matematica/tabela-price.htm
    #Utiliza-se do D(valor do empréstimo), t(parcelas ou numero de meses), j(juros mensal) e arredondando para duas casas decimais
    parcela = round((D*(((1+j)**t)*j/(((1+j)**t)-1))), 2)
    #validação de renda: se ela for menor que um salário mínimo, o resultado é negado
    if renda < 1320:
        resultado = "Negado"
        return render_template("resultado1.html", resultado = resultado)
    #Segunda validação: a parcela deve ser menor que 20% da renda    
    elif (parcela) < (0.20 * renda):
        resultado = "Aprovado"
    #O total pago será dado pelo tempo de meses, multiplicando pela parcela e arredondando para duas casas    
        total = round((t * parcela), 2)
    #O quanto pago de juros é o total pago menos o que foi emprestado    
        juros = round((total - D), 2)
        return render_template("resultado.html", resultado = resultado, parcela = parcela, total = total, juros = juros) 
    #Caso a parcela for maior que 20% do salário, entra no else negando o empréstimo.                    
    else:
         resultado = "Negado"
         return render_template("resultado1.html", resultado = resultado)


#colocando o site para rodar
app.run(debug=True)
