from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Recebe as respostas do formulário
        respostas = {
            'desatencao': request.form.get('desatencao'),
            'hiperatividade': request.form.get('hiperatividade'),
            'impulsividade': request.form.get('impulsividade'),
            'organizacao': request.form.get('organizacao'),
            'distracao': request.form.get('distracao')
        }

        # Contar quantas respostas "Sim"
        sim_count = sum(1 for r in respostas.values() if r == 'Sim')

        # Avaliar as respostas
        if sim_count >= 3:
            resultado = "Há indícios de que você pode apresentar sintomas de TDAH. Procure um profissional para um diagnóstico mais preciso."
        else:
            resultado = "Com base em suas respostas, é improvável que você tenha TDAH. No entanto, se tiver preocupações, consulte um especialista."

        return render_template('resultado.html', resultado=resultado)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
