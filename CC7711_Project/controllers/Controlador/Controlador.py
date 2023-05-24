from controller import Robot, Motor, DistanceSensor, Supervisor, LED

# Definição de constantes
PASSO_TEMPO = 256
VELOCIDADE_MAX = 6.28
LIMIAR_OBSTACULO = 100
QTD_LEDS = 10
TOLERANCIA = 1e-4

# Função para inicializar o robô e obter as referências os motores são parados e LEDs
def inicializar_robo():
    robo = Robot()
    motor_esquerdo = robo.getDevice("left wheel motor")
    motor_direito = robo.getDevice("right wheel motor")

    # Define a intensidade do LED para o máximo
    leds = [robo.getDevice("led0")]
    leds[0].set(-1)

    # Define a posição dos motores como infinito
    motor_esquerdo.setPosition(float('inf'))
    motor_direito.setPosition(float('inf'))

    # Define a velocidade inicial dos motores como zero
    motor_esquerdo.setVelocity(0.0)
    motor_direito.setVelocity(0.0)

    return robo, motor_esquerdo, motor_direito, leds

# Função para inicializar os sensores de proximidade do robô
def inicializar_sensores_proximidade(robo):
    nomes_sensores_proximidade = ["ps0", "ps1", "ps2", "ps3", "ps4", "ps5", "ps6", "ps7"]
    sensores_proximidade = [robo.getDevice(nome) for nome in nomes_sensores_proximidade]
    for sensor in sensores_proximidade:
        sensor.enable(PASSO_TEMPO)
    return sensores_proximidade

# Função para ajustar a velocidade dos motores com base nos valores dos sensores de proximidade
def ajustar_velocidade(valores_sensores):
    velocidade_esquerda = VELOCIDADE_MAX
    velocidade_direita = VELOCIDADE_MAX

    if valores_sensores[0] > LIMIAR_OBSTACULO or valores_sensores[7] > LIMIAR_OBSTACULO:
        # Se os sensores frontais (0 ou 7) detectarem um obstáculo acima do limiar,
        # o robô vira a esquerda até que não tenha um obstáculo.
        velocidade_esquerda = -min(velocidade_esquerda, VELOCIDADE_MAX)
        velocidade_direita = min(velocidade_direita, VELOCIDADE_MAX / 2)
    elif valores_sensores[6] > LIMIAR_OBSTACULO:
        # Se o sensor 6 (esquerda) detectar um obstáculo acima do limiar,
        # o robô vira a direita até que não tenha um obstáculo.
        velocidade_esquerda = min(velocidade_esquerda / 2, VELOCIDADE_MAX)
        velocidade_direita = -min(velocidade_direita, VELOCIDADE_MAX)
    elif valores_sensores[1] > LIMIAR_OBSTACULO:
        # Se o sensor 1 (direita) detectar um obstáculo acima do limiar,
        # o robô vira a esquerda até que não tenha um obstáculo.
        velocidade_esquerda = -min(velocidade_esquerda, VELOCIDADE_MAX)
        velocidade_direita *= min(velocidade_direita / 2, VELOCIDADE_MAX)

    # Limita as velocidades máximas dos motores
    velocidade_esquerda = max(min(velocidade_esquerda, VELOCIDADE_MAX), -VELOCIDADE_MAX)
    velocidade_direita = max(min(velocidade_direita, VELOCIDADE_MAX), -VELOCIDADE_MAX)

    return velocidade_esquerda, velocidade_direita

def main():
    robo, motor_esquerdo, motor_direito, leds = inicializar_robo()
    sensores_proximidade = inicializar_sensores_proximidade(robo)
    supervisor = Supervisor()
    objetoNode = supervisor.getFromDef("wooden-box")
    posicao = objetoNode.getPosition()
    xb, yb = posicao[0], posicao[1]
    x, y = xb, yb

    while robo.step(PASSO_TEMPO) != -1:
        valores_sensores = [sensor.getValue() for sensor in sensores_proximidade]
        caixa = objetoNode.getPosition()
        xb, yb = caixa[0], caixa[1]

        velocidade_esquerda, velocidade_direita = ajustar_velocidade(valores_sensores)

        if abs(xb - x) > TOLERANCIA or abs(yb - y) > TOLERANCIA:
            # Se a caixa foi movida além da tolerância definida, então a caixa leve foi encontrada.
            # Com isso, os motores são parados, inverte o LED e imprime uma mensagem.
            velocidade_esquerda = 0
            velocidade_direita = 0
            leds[0].set(leds[0].get() * -1)
            print("[+] Caixa leve encontrada!")

        motor_esquerdo.setVelocity(velocidade_esquerda)
        motor_direito.setVelocity(velocidade_direita)

if __name__ == "__main__":
    main()
