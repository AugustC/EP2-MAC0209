#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

def grafico_gforce(filename, nome):
    dados = pd.read_csv(filename, sep=";")
    pend_resultante = dados["gforce"]
    tempo = dados["time"]
    plt.plot(tempo, pend_resultante)
    plt.title(nome)
    plt.ylabel(u"Força-G Resultante")
    plt.xlabel("Tempo")
    # plt.savefig(nome + ".png")
    # Descomente a linha abaixo para mostrar o grafico durante a execucao do programa
    plt.show()
    plt.close()

grafico_gforce("Dados/Pendulo/pend 1.csv", "Pêndulo A")
grafico_gforce("Dados/Pendulo/pend 2.csv", "Pêndulo B")
grafico_gforce("Dados/Pendulo/pend 3.csv", "Pêndulo C")
