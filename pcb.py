import random
from random import randint as ran
from datetime import datetime
from tabulate import tabulate

class PCB:
    processos = []

    def __init__(self, pid, tempoDeChegada, tempoDeBurst, prioridade, quantum):
        self.nomes = nomes[random.randint(0,len(nomes)-1)]
        self.pid = "P" + str(pid) 
        self.tempoDeChegada = tempoDeChegada
        self.tempoDeBurst = tempoDeBurst
        self.remainingBurstTime = tempoDeBurst
        self.prioridade = prioridade
        self.quantum = quantum
        self.data_e_hora = datetime.today().strftime('%B %d, %H:%M:%S')
        self.endereco_inicial = random.randint(500, 1000)
        self.endereco_final = random.randint(500, 1000)

def createRandomProcesses(self):
    self.qtd_processos = ran(1,9)
    while self.qtd_processos:
        tc = ran(0, self.qtd_processos) #Tempo de chegada
        bt = ran(1, 20)                 #Tempo de Burst
        self.prioridade = ran(0,9)
        self.quantum = ran(1,8) 
        if tc < bt:
            PCB.processos.append(PCB(self.qtd_processos, tc, bt, self.prioridade, self.quantum))
            self.qtd_processos -= 1

def createProcesses(self):
    createRandomProcesses(self)    

def printData(queue, fila_processos):

    head = [
        "Nome","PID","Prioridade","tempo De Chegada", "Tempo De Burst",
        "Data e Hora","Endereco Inicial", "Endereco Final"]

    data = []

    for i in range(len(queue)):
        j = []
        j.append(queue[i].nomes)
        j.append(queue[i].pid)
        j.append(queue[i].prioridade)
        j.append(queue[i].tempoDeChegada)
        j.append(queue[i].tempoDeBurst)
        j.append(queue[i].data_e_hora)
        j.append(queue[i].endereco_inicial)
        j.append(queue[i].endereco_final)
        data.append(j)

    data.sort(key=lambda x: x[0])
    print(tabulate(data, headers=head, tablefmt="firstrow"))
    print("\n Fila de processos: \n\t")
    for i in fila_processos:
        print(f"{i.pid}", end="--")
    print()

nomes = [ 
    'Chrome.exe',
    'Spotify',
    'Discord',
    'Firefox',
    'Visual Studio Code',
    'Steam',
    'League of Legends',
    'Dropbox',
    'Microsoft Outlook',
    'AMD Software',
    'CCleaner',
    'Opera',
    'PostgreSQL'
]
