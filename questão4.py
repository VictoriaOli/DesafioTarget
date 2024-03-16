# Questão 4

"""
    4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. 
    Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. 
    Seu objetivo é descobrir qual interruptor controla qual lâmpada.

    Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

"""

"""
Resposta:
    Na sala de interruptores:
    - Ligue o primeiro interruptor e deixe-o ligado por um período curto de tempo
    - Deixe os outros dois interruptores desligados
    1ª ida a sala das lâmpadas:
    - A lâmpada que estiver acesa é controlada pelo primeiro interruptor
    - A lâmpada que estiver apagada e estiver fria é controlada pelo segundo interruptor
    - A lâmpada que estiver apagada, mas estiver quente, é controlada pelo terceiro interruptor

    Novamente na sala de interruptores:
    - Desligue o primeiro interruptor desligado
    - Ligue o segundo interruptor 
    - Mantenha o terceiro interruptor desligado
    2ª ida a sala das lâmpadas:
    - A lâmpada que ligar é controlada pelo segundo interruptor
    - A lâmpada que permanecer apagada é controlada pelo terceiro interruptor

"""