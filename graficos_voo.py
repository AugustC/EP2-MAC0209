#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def grafico_aceleracao(filename, nome):
    dados = pd.read_csv(filename, sep=",")
    vooX = dados["x"]
    vooY = dados["y"]
    vooZ = dados["z"]
    voo_resultante = (vooX**2 + vooY**2 + vooZ**2)**(1/2)
    plt.plot(voo_resultante)
    plt.title(nome)
    plt.ylabel(u"Aceleração Resultante")
    plt.xlabel("Tempo")
    plt.savefig(nome + ".png")
    plt.close()

grafico_aceleracao("Dados/Foguete/vooA.csv", "Vôo A")
grafico_aceleracao("Dados/Foguete/vooB.csv", "Vôo B")
grafico_aceleracao("Dados/Foguete/vooC.csv", "Vôo C")
grafico_aceleracao("Dados/Foguete/vooD.csv", "Vôo D")
