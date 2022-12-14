from pcb import PCB

def RoundRobinWhithPriority(processos): 
    global tempoDeExecucao 
    filaDeProntos = []
    FilaCompleta = []
    tempoDeExecucao = 0
    
    def Scheduling(p, processos):
        global tempoDeExecucao
        if(p.remainingBurstTime <= p.quantum):              
            tempoDeExecucao += p.remainingBurstTime         # Aumenta o valor do tempo de execução
            p.remainingBurstTime = 0                        
        else:
            p.remainingBurstTime -= p.quantum               # Diminui o tempo de burst do processo atual   
            tempoDeExecucao += p.quantum                    # Aumenta o valor do tempo de execução
        FilaCompleta.append(p)                              # Vai adicionando os processos na fila

        if(len(processos) > 0):                             # verifique se a fila de processos está vazia,
            remov = []                                      # se não tiver adiciona os processos na fila de prontos
            for i in processos:
                if(i.prioridade <= tempoDeExecucao):
                    filaDeProntos.append(i)
                    remov.append(i)
            for i in remov:
                processos.remove(i)
        if(p.remainingBurstTime > 0):
            filaDeProntos.append(p)
        else:
            p.tempoDeConclusao = tempoDeExecucao

    processos.sort(key=lambda x: x.prioridade)            # Quando processos tiverem o mesmo tempo de chegada           
    filaDeProntos.append(processos.pop(0))                # a prioridade vai decidir qual vai ser executado
    Scheduling(filaDeProntos.pop(0), processos)
    while len(filaDeProntos) > 0:
        Scheduling(filaDeProntos.pop(0), processos)

    return FilaCompleta