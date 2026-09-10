class Agendamento:
     def __init__(self, cliente, telefone, servico, preco, barbeiro, data, horario, status):
        self.cliente = cliente
        self.telefone = telefone
        self.servico = servico
        self.preco = preco
        self.barbeiro = barbeiro
        self.data = data
        self.horario = horario
        self.status = status

def exibir(self):
    print(f"Cliente: {self.cliente}, Telefone: {self.telefone}, Serviço: {self.servico}, Preço: {self.preco}, Barbeiro: {self.barbeiro}, Data: {self.data}, Horário: {self.horario}, Status: {self.status}")

def converter_tupla(self):
    return self.cliente, self.telefone, self.servico, self.preco, self.barbeiro, self.data, self.horario, self.status

def reverte_tupla(tupla):
    agendamento = Agendamento(
        cliente=tupla[1],
        telefone=tupla[2],
        servico=tupla[3],
        preco=tupla[4],
        barbeiro=tupla[5],
        data=tupla[6],
        horario=tupla[7],
        status=tupla[8]
    )

    agendamento.id = tupla[0]
    return agendamento