from random import randrange

questions = [
    "O que significa a sigla IA?",
    "Qual é o ramo da IA que estuda o raciocínio humano?",
    "Qual é o ramo da IA que se preocupa com a construção de algoritmos capazes de aprender?",
    "O que é uma rede neuronal?",
    "Qual é a diferença entre IA fraca e IA forte?",
    "Qual é a principal técnica usada em Aprendizagem Profunda?",
    "O que é o Aprendizagem por Reforço?",
    "O que é o Processamento de Linguagem Natural?",
    "Qual é o nome do robô que foi criado para simular emoções humanas?",
    "Qual é a empresa de tecnologia conhecida por seu assistente virtual, a Siri?"
]

answers = [
    ["Inteligência Artificial", "Instituto de Artes", "Instituto de Automação", "Instituto de Aprendizagem", "A"],
    ["Visão Computacional", "Processamento de Linguagem Natural", "Robótica", "Aprendizagem de Máquina", "B"],
    ["Aprendizagem por Reforço", "Aprendizagem de Máquina", "Visão Computacional", "Processamento de Linguagem Natural", "B"],
    ["Um algoritmo que simula o funcionamento do cérebro humano", "Um algoritmo que simula o sistema nervoso humano", "Um algoritmo que simula o funcionamento do corpo humano", "Um algoritmo que simula a estrutura do DNA humano", "A"],
    ["IA fraca é limitada a uma tarefa específica, enquanto IA forte é capaz de realizar qualquer tarefa que um ser humano pode fazer", "IA fraca é capaz de realizar qualquer tarefa que um ser humano pode fazer, enquanto IA forte é limitada a uma tarefa específica", "IA fraca é mais avançada do que IA forte", "IA forte é mais avançada do que IA fraca", "A"],
    ["Redes Neuronais Artificiais", "Regressão Linear", "Árvores de Decisão", "K-Means", "A"],
    ["Um tipo de Aprendizagem de Máquina que usa recompensas para guiar a aprendizagem", "Um tipo de Aprendizagem de Máquina que usa exemplos para guiar a aprendizagem", "Um tipo de Aprendizagem de Máquina que usa regras para guiar a aprendizagem", "Um tipo de Aprendizagem de Máquina que usa algoritmos para guiar a aprendizagem", "A"],
    ["Um ramo da IA que se preocupa com a interação entre humanos e computadores", "Um ramo da IA que se preocupa com a tradução de línguas estrangeiras", "Um ramo da IA que se preocupa com a detecção de spam", "Um ramo da IA que se preocupa com a simulação de seres humanos", "A"],
    ["ASIMO", "RoboCop", "Bender", "Pepper", "D"],
    ["Apple", "Google", "Amazon", "Microsoft", "A"]
]

lifelines = ["Saltar a pergunta", "50/50"]

def start_game():
    print("Bem-vindo ao Quem Quer Ser Milionário!")
    name = input("Qual é o seu nome? ")
    print(f"Olá {name}, vamos começar!")
    play()

def play():
    # completar código
    print(f"!TODO {randrange(0, 10)}")

start_game()