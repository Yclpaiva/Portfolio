import subprocess
import sys
import time

nome_sessão = sys.argv[1]
pasta_robo = f'~/{sys.argv[2]}'
qnt_abas =  int(sys.argv[3])
tela = int(sys.argv[4]) if len(sys.argv) > 4 else 1
window = int(sys.argv[5]) if len(sys.argv) > 5 else 1
def execute_tmux_commands():
    if window == "1":
        valorpane = 1
    else:
        valorpane = 0
    
    comandos = [
        f"tmux new-session -d -s {nome_sessão}",
        f"tmux split-window -h -t {nome_sessão}:{tela}.{valorpane}",
        f"tmux split-window -h -t {nome_sessão}:{tela}.{valorpane+1}",
        f"tmux split-window -h -t {nome_sessão}:{tela}.{valorpane}",
    ]
    i = 0
    valorpanefor = 1 if i == 0 and window == 1 else 2
    valorpanefor = 0 if i == 0 and window == 0 else 2
    
    for _ in range(4):
        comandos.append(f"tmux split-window -v -t {nome_sessão}:{tela}.{i+(valorpanefor)}")
        i += 1 if i == 0 else 2
    
    for _ in range(qnt_abas) if qnt_abas <= 8 else print("quantidade de abas maior que 8"):

        comandos.append(f"tmux select-pane -t :1.{_+1}")
        #comandos.append(f"cd {pasta_robo}/{_+1}")
        comandos.append(f"tmux send-keys -t {nome_sessão}:{tela}.{_+valorpane} 'cd {pasta_robo}/{_+valorpane}' C-m")
        comandos.append(f"tmux send-keys -t {nome_sessão}:{tela}.{_+valorpane} 'xvfb-run -a ./abas' C-m")
        
    for comando in comandos:
        subprocess.run(comando, shell=True)
    subprocess.run(f"tmux attach-session -t {nome_sessão}", shell=True)

if __name__ == "__main__":
    execute_tmux_commands()

