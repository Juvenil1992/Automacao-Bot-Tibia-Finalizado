🎥 Vídeo Demonstrativo
https://www.youtube.com/watch?v=di_D0YP4MHE


🤖 Sobre o Projeto
Este projeto é a versão atualizada do meu bot para o jogo Tibia, trazendo melhorias significativas em comparação ao Projeto 1. O foco desta versão é aumentar a eficiência, reduzir a necessidade de configurações manuais e automatizar mais aspectos do jogo.

🔄 Principais Melhorias
🧭 Waypoints Automáticos (CaveBot.py)
O personagem agora reconhece quando chega ao destino e para de clicar no ícone do mapa automaticamente.

Não é mais necessário definir quantas vezes ele deve clicar.

Isso melhora bastante a eficiência da movimentação e reduz o trabalho na configuração dos caminhos.

⚔️ Combate Inteligente com Magias (Battle.py)
Utiliza PyTesseract para contar a quantidade de monstros na tela.

Usa magias em área automaticamente com base na quantidade detectada.

Grande evolução em relação ao Projeto 1, que não fazia uso de magias inteligentes.

🧪 Checagem de Mana Potions (Qtd_Potions_Bp.py + CaveBot.py)
O bot conta quantas mana potions o personagem possui.

Se a quantidade estiver abaixo do limite configurado, ele retorna para a cidade, deposita os itens e compra novas potions automaticamente.

🧙‍♂️ Interação com NPCs (NPC_Potions.py)
O algoritmo calcula a quantidade necessária de potions.

Realiza o diálogo com o NPC automaticamente, comprando as potions configuradas.

Essa automação não existia na primeira versão do projeto.

🛠 Tecnologias Utilizadas
Python

PyAutoGUI

PyTesseract

OpenCV
