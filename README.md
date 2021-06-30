# BOT_EAD
Com pyautogui e time
O algoritmo com base na localização dos ícones no desktop, abre o google chrome, faz login, e abre o link da aula (conforme o dia e horário da semana)

!!!!! O algoritmo pode não rodar corretamente em sua máquina pois ele foi feito para o tamanho de tela e localização dos links propria de meu desktop !!!!!


Primeiramente o algoritmo "localiza a hora atual" (Brasil-Brasília)
Depois lê o input do usuário para saber qual dia da semana é\
seg = segunda\
ter = terça\
qua = quarta\
qui = quinta\
sex = sexta

E para cada dia da semana há um horário \
Então é feito um condição de horários, se X hora e Y minutos estiverem dentro da condição, o
link é digitado na barra de pesquisa do navegador e te leva para a página de destino.
