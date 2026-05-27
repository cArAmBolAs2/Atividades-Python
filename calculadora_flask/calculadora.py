import math
from flask import render_template, request

def calcular():
    num1 = float(request.form["num1"])
    operacao = request.form["operacao"]

    # Operações de apenas 1 número
    if operacao == "sqrt":
        if num1 < 0:
            resultado = "Erro"
            etapas = f"Erro: Não existe raiz real de número negativo ({num1})."
        else:
            resultado = math.sqrt(num1)
            etapas = f"√{num1} = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    if operacao == "log":
        if num1 <= 0:
            resultado = "Erro"
            etapas = f"Erro: Logaritmo exige número maior que zero (informado: {num1})."
        else:
            resultado = math.log10(num1)
            etapas = f"log10({num1}) = {resultado}"
        return render_template("calculadora.html", etapas=etapas, resultados=resultado)

    # Operações que exigem o segundo número
    num2_valor = request.form.get("num2", "").strip()
    if not num2_valor:
        return render_template(
            "calculadora.html",
            etapas="Informe o segundo número para esta operação.",
            resultados="Erro",
        )
    
    num2 = float(num2_valor)

    if operacao == "+":
        resultado = num1 + num2
        etapas = f"{num1} + {num2} = {resultado}"
    elif operacao == "-":
        resultado = num1 - num2
        etapas = f"{num1} - {num2} = {resultado}"
    elif operacao == "*":
        resultado = num1 * num2
        etapas = f"{num1} × {num2} = {resultado}"
    elif operacao == "/":
        if num2 == 0:
            resultado = "Erro"
            etapas = "Erro: Divisão por zero não é permitida."
        else:
            resultado = num1 / num2
            etapas = f"{num1} ÷ {num2} = {resultado}"
    elif operacao == "**":
        resultado = math.pow(num1, num2)
        etapas = f"{num1} ^ {num2} = {resultado}"
    else:
        resultado = "Erro"
        etapas = "Operação inválida."

    return render_template("calculadora.html", etapas=etapas, resultados=resultado)