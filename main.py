from pcb import PCB as p
from queue import Queue
from time import sleep
from pcb import createProcesses, printData
from rr import RoundRobinWhithPriority

class Principal: 

    def inicio(self):
        queues = []
        for i in range(4):
            sleep(1)
            queues.append(Queue(i)) 
            createProcesses(self)
            pro = RoundRobinWhithPriority(p.processos)
            queues = list(set(pro))
            queues.sort(key=lambda x: x.pid)
            print(f"\nFila: {i+1} | Processos: {self.qtd_processos} | Quantum: {self.quantum}" )
            printData(queues,pro)

Principal().inicio()