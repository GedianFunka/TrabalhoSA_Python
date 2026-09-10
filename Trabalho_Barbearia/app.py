from flask import Flask, render_template
from agendamentos import listar_agendamentos, buscar_agendamento_por_id, buscar_por_status

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendamentos')
def agendamentos():
    agendamentos = listar_agendamentos()
    return render_template('agendamentos.html', agendamentos=agendamentos)

@app.route('/agendamentos/status/<status>')
def agendamentos_por_status(status):
    buscar_status = buscar_por_status(status)
    return render_template('agendamentos.html', agendamentos=buscar_status, status=status)

@app.route('/agendamentos/<int:id>')
def detalhes_agendamento(id):
    buscar_id = buscar_agendamento_por_id(id)
    return render_template('detalhe.html', agendamento=buscar_id, id=id)


if __name__ == '__main__':
    app.run(debug=True)
