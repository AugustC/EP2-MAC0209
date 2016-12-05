#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime
from datetime import timedelta
fmt = '%H:%M:%S:%f'

def fixMicroseconds(timestamp):
    # Quick hack para arrumar os microsegundos dos dados
    parts = timestamp.split(':')
    return ':'.join(
        parts[:-1] + ['{:03d}'.format(int(parts[-1]))]
    )

def convert_time(timeseries):
    initial = datetime.strptime(timeseries[0], fmt)
    for i in range(len(timeseries)):
        ti = datetime.strptime(fixMicroseconds(timeseries[i]), fmt)
        diff = ti - initial
        timeseries[i] = diff.total_seconds()
    return timeseries

def grafico_aceleracao(filename, nome):
    dados = pd.read_csv(filename, sep=",")
    vooX = dados["x"]
    vooY = dados["y"]
    vooZ = dados["z"]
    voo_resultante = (vooX**2 + vooY**2 + vooZ**2)**(1/2)
    tempo = dados["time"].values
    tempo = convert_time(tempo)
    plt.plot(tempo,vooY)
    plt.title(nome)
    plt.ylabel(u"Aceleração Resultante")
    plt.xlabel("Tempo")
#    plt.savefig(nome + ".png")
    plt.show()
    plt.close()

grafico_aceleracao("Dados/Foguete/vooA.csv", "Vôo A")
grafico_aceleracao("Dados/Foguete/vooB.csv", "Vôo B")
grafico_aceleracao("Dados/Foguete/vooC.csv", "Vôo C")
grafico_aceleracao("Dados/Foguete/vooD.csv", "Vôo D")
