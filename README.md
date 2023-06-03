# 🤖 E-Puck Robot Control 🤖

Este repositório contém um script Python para controlar um robô E-Puck em uma simulação Webots. O robô é capaz de detectar e evitar obstáculos, bem como monitorar um objeto específico chamado "caixa leve".Projeto elaborado para a disciplina de CC7711 - INTELIGENCIA ARTIFICIAL E ROBOTICA do Centro Universitário FEI.

## Descrição 💻

O código utiliza a plataforma Webots para simular o robô E-Puck. O robô possui sensores de proximidade para detectar obstáculos e ajustar seu movimento de acordo, evitando colisões.

Um objeto específico, chamado "caixa leve", é constantemente monitorado pelo robô. Se o robô detecta que a "caixa leve" se moveu além de um limite de tolerância definido, ele para, alterna o estado de um de seus LEDs e imprime uma mensagem de alerta.

Uma demonstração em forma de vídeo encontra-se disponível no link a seguir (Realize o Download): [Vídeo de Demonstração](https://github.com/akajhon/E-Puck-Robot-Control/blob/main/video-simulacao.mp4)

## Instruções de configuração 📖

1. Certifique-se de ter a plataforma Webots instalada e configurada em seu sistema.
2. Faça o download do código do repositório ou clone o repositório em seu sistema local.
3. No Webots, certifique-se de que o robô E-Puck tem a propriedade "Supervisor" definida como TRUE.
4. Defina o nome do NODE da "caixa leve" como "wooden-box".
5. Carregue o código no Webots e execute a simulação.

## Autores 👨‍💻
| <img src="https://avatars.githubusercontent.com/u/63318165?v=4" alt="Thales" width="150"/> | <img src="https://avatars.githubusercontent.com/u/69048604?v=4" alt="Joao" width="150"/> | <img src="https://avatars.githubusercontent.com/u/65295232?v=4" alt="Vitor" width="150"/> | <img src="https://avatars.githubusercontent.com/u/72151253?v=4" alt="Hugo" width="150"/> |
|:-------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------:|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [Thales Oliveira Lacerda](https://github.com/LacThales)                                 | [João Pedro Rosa Cezarino](https://github.com/akajhon)                                      | [Vitor Martins Oliveira](https://github.com/vihmar)                                         | [Hugo Linhares Oliveira](https://github.com/hugolinhareso)                                       |
| R.A: 22.120.056-1                                                                          | R.A: 22.120.021-5                                                                           | R.A: 22.120.067-8                                                                           | R.A: 22.120.046-2                                                                          |
***

## Licença

Este projeto é de código aberto e está disponível sob os termos da [MIT License](https://opensource.org/licenses/MIT).
