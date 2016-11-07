import matplotlib.pyplot as plt
import math

g = 10

def euler_foguete_semresistencia(vx0, vy0, angle, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler, sem resistencia
    result = []
    vx = vx0
    vy = vy0
    x = y = 0
    result.append((x,y))
    for i in range(n):
        x = x + vx * step
        y = y + vy * step
        vx = vx #Forca de resistencia e zero
        vy = vy - g * step
        result.append((x,y))
    return result

def euler_cromer_foguete_semresistencia(vx0, vy0, angle, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler, sem resistencia
    result = []
    vx = vx0
    vy = vy0
    x = y = 0
    result.append((x,y))
    for i in range(n):
        vx = vx #Forca de resistencia e zero
        vy = vy - g * step
        x = x + vx * step
        y = y + vy * step
        result.append((x,y))
    return result

def euler_foguete_comresistencia(vx0, vy0, angle, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler, com resistencia
    delta = 0.5
    result = []
    vx = vx0
    vy = vy0
    x = y = 0
    result.append((x,y))
    for i in range(n):
        x = x + vx * step
        y = y + vy * step
        vx = vx - delta*(vx**2 + vy**2) * math.cos(angle)*step
        if (vy > 0):
            vy = vy - g * step - delta * (vy**2 + vx**2) * math.sin(angle)*step
        else:
            vy = vy - g * step + delta * (vy**2 + vx**2) * math.sin(angle)*step
        result.append((x,y))
    return result
        
def euler_cromer_foguete_comresistencia(vx0, vy0, angle, step, n):
    # Funcao que devolve o vetor dos valores calculados pelo metodo de Euler-Cromer, com resistenci
    delta = 0.5
    result = []
    vx = vx0
    vy = vy0
    x = y = 0
    result.append((x,y))
    for i in range(n):
        vx = vx - delta*(vx**2 + vy**2)*math.cos(angle)*step
        if (vy > 0):
            vy = vy - g * step - delta * (vy**2 + vx**2) * math.sin(angle)*step
        else:
            vy = vy - g * step + delta * (vy**2 + vx**2) * math.sin(angle)*step
        x = x + vx * step
        y = y + vy * step
        result.append((x,y))
    return result
        
def plots(titulo, coord):
    xs = [x[0] for x in coord]
    ys = [x[1] for x in coord]
    plt.plot(xs, ys)
    plt.title(titulo)
    plt.ylabel("Y")
    plt.xlabel("X")
    plt.show()
    plt.close()
    
Euler_semR = euler_foguete_semresistencia(2.4 * math.cos(70), 2.4 * math.sin(70), 70, 0.01, 55)
Euler_Cromer_semR = euler_cromer_foguete_semresistencia(2.4 * math.cos(70), 2.4 * math.sin(70), 70, 0.01, 55)
Euler_comR = euler_foguete_comresistencia(2.4 * math.cos(70), 2.4 * math.sin(70), 70, 0.01, 55)
Euler_Cromer_comR = euler_cromer_foguete_comresistencia(2.4 * math.cos(70), 2.4 * math.sin(70), 70, 0.01, 55)

# Sem Resistencia
plots("Euler Sem Resistencia", Euler_semR)
plots("Euler-Cromer Sem Resistencia", Euler_Cromer_semR)

# Com resistencia
plots("Euler Com Resistencia", Euler_comR)
plots("Euler-Cromer Com Resistencia", Euler_Cromer_comR)

