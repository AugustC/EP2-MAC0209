import matplotlib.pyplot as plt

g = 10

def euler_pendulo_semresistencia(theta0, v0, L, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler, sem resistencia
    resultTheta = []
    resultV = []
    thetaN = theta = theta0
    v = v0
    resultTheta.append((0, theta))
    resultV.append((0, v))
    for i in range(n):
        theta = thetaN + v*step/L
        v = v - thetaN*step*g/(L**2)
        thetaN = theta
        resultTheta.append((step*i, theta))
        resultV.append((step*i, v))
    return resultTheta, resultV

def euler_cromer_pendulo_semresistencia(theta0, v0, L, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler-Cromer, sem resistencia
    resultTheta = []
    resultV = []
    theta = theta0
    v = v0
    resultTheta.append((0, theta))
    resultV.append((0, v))    
    for i in range(n):
        v = v - theta*step*g/(L**2)
        theta = theta+ v*step/L
        resultTheta.append((step*i, theta))
        resultV.append((step*i, v))
    return resultTheta, resultV

def euler_pendulo_comresistencia(theta0, v0, L, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler, com resistencia
    delta = 0.5
    resultTheta = []
    resultV = []   
    thetaN = theta = theta0
    v = v0
    resultTheta.append((0, theta))
    resultV.append((0, v))    
    for i in range(n):
        theta = thetaN + v*step/L
        v = v - (thetaN * g/(L**2) + delta * v / L) * step
        thetaN = theta
        resultTheta.append((step*i, theta))
        resultV.append((step*i, v))
    return resultTheta, resultV
        
def euler_cromer_pendulo_comresistencia(theta0, v0, L, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler-Cromer, com resistenci
    delta = 0.5
    resultTheta = []
    resultV = []    
    theta = theta0
    v = v0
    resultTheta.append((0, theta))
    resultV.append((0, v))    
    for i in range(n):
        v = v - (theta * g/(L**2) + delta * v / L) * step
        theta = theta + v*step/L
        resultTheta.append((step*i, theta))
        resultV.append((step*i, v))
    return resultTheta, resultV

def plots(titulo, var, coord):
    xs = [x[0] for x in coord]
    ys = [x[1] for x in coord]
    plt.plot(xs, ys)
    plt.title(titulo)
    plt.ylabel(var)
    plt.xlabel("Tempo")
    plt.show()
    plt.close()
    
Euler_semRT, Euler_semRV = euler_pendulo_semresistencia(60, 0, 1.40, 0.1, 181)
Euler_Cromer_semRT, Euler_Cromer_semRV = euler_cromer_pendulo_semresistencia(60, 0, 1.40, 0.1, 181)
Euler_comRT, Euler_comRV = euler_pendulo_comresistencia(60, 0, 1.40, 0.1, 181)
Euler_Cromer_comRT, Euler_Cromer_comRV = euler_cromer_pendulo_comresistencia(60, 0, 1.40, 0.1, 181)

# Sem Resistencia
plots("Euler Sem Resistencia", "Theta", Euler_semRT)
plots("Euler-Cromer Sem Resistencia", "Theta", Euler_Cromer_semRT)
plots("Euler Sem Resistencia", "V", Euler_semRV)
plots("Euler-Cromer Sem Resistencia", "V", Euler_Cromer_semRV)

# Com resistencia
plots("Euler Com Resistencia", "Theta", Euler_comRT)
plots("Euler-Cromer Com Resistencia", "Theta", Euler_Cromer_comRT)
plots("Euler Com Resistencia", "V", Euler_comRV)
plots("Euler-Cromer Com Resistencia", "V", Euler_Cromer_comRV)

