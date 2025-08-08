import turtle
import time
import colorsys
import os

a1 = r"""
                                             ,----,                                                       
                                           ,/   .`|                 ,----..       ,----..                 
           .---.    ,---,.  .--.--.      ,`   .'  :        .---.   /   /   \     /   /   \      ,---,     
          /. ./|  ,'  .' | /  /    '.  ;    ;     /       /. ./|  /   .     :   /   .     :   .'  .' `\   
      .--'.  ' ;,---.'   ||  :  /`. /.'___,/    ,'    .--'.  ' ; .   /   ;.  \ .   /   ;.  \,---.'     \  
     /__./ \ : ||   |   .';  |  |--` |    :     |    /__./ \ : |.   ;   /  ` ;.   ;   /  ` ;|   |  .`\  | 
 .--'.  '   \' .:   :  |-,|  :  ;_   ;    |.';  ;.--'.  '   \' .;   |  ; \ ; |;   |  ; \ ; |:   : |  '  | 
/___/ \ |    ' ':   |  ;/| \  \    `.`----'  |  /___/ \ |    ' '|   :  | ; | '|   :  | ; | '|   ' '  ;  : 
;   \  \;      :|   :   .'  `----.   \   '   :  ;   \  \;      :.   |  ' ' ' :.   |  ' ' ' :'   | ;  .  | 
 \   ;  `      ||   |  |-,  __ \  \  |   |   |  '\   ;  `      |'   ;  \; /  |'   ;  \; /  ||   | :  |  ' 
  .   \    .\  ;'   :  ;/| /  /`--'  /   '   :  | .   \    .\  ; \   \  ',  /  \   \  ',  / '   : | /  ;  
   \   \   ' \ ||   |    \'--'.     /    ;   |.'   \   \   ' \ |  ;   :    /    ;   :    /  |   | '` ,/   
    :   '  |--" |   :   .'  `--'---'     '---'      :   '  |--"    \   \ .'      \   \ .'   ;   :  .'     
     \   \ ;    |   | ,'                             \   \ ;        `---`         `---`     |   ,.'       
      '---"     `----'                                '---"                                 '---'         
                                                                         ,----,                     
               ,----..             ____  ,-.----.                      ,/   .`|                     
  ,----..     /   /   \          ,'  , `.\    /  \                   ,`   .'  :   ,---,.,-.----.    
 /   /   \   /   .     :      ,-+-,.' _ ||   :    \          ,--,  ;    ;     / ,'  .' |\    /  \   
|   :     : .   /   ;.  \  ,-+-. ;   , |||   |  .\ :       ,'_ /|.'___,/    ,',---.'   |;   :    \  
.   |  ;. /.   ;   /  ` ; ,--.'|'   |  ;|.   :  |: |  .--. |  | :|    :     | |   |   .'|   | .\ :  
.   ; /--` ;   |  ; \ ; ||   |  ,', |  ':|   |   \ :,'_ /| :  . |;    |.';  ; :   :  |-,.   : |: |  
;   | ;    |   :  | ; | '|   | /  | |  |||   : .   /|  ' | |  . .`----'  |  | :   |  ;/||   |  \ :  
|   : |    .   |  ' ' ' :'   | :  | :  |,;   | |`-' |  | ' |  | |    '   :  ; |   :   .'|   : .  /  
.   | '___ '   ;  \; /  |;   . |  ; |--' |   | ;    :  | | :  ' ;    |   |  ' |   |  |-,;   | |  \  
'   ; : .'| \   \  ',  / |   : |  | ,    :   ' |    |  ; ' |  | '    '   :  | '   :  ;/||   | ;\  \ 
'   | '/  :  ;   :    /  |   : '  |/     :   : :    :  | : ;  ; |    ;   |.'  |   |    \:   ' | \.' 
|   :    /    \   \ .'   ;   | |`-'      |   | :    '  :  `--'   \   '---'    |   :   .':   : :-'   
 \   \ .'      `---`     |   ;/          `---'.|    :  ,      .-./            |   | ,'  |   |.'     
  `---`                  '---'             `---`     `--`----'                `----'    `---'       
                                                                                                    
                                                                                                          
                                                                            
                                                  ,--.                      
  .--.--.     ,----..     ,---,    ,---,.       ,--.'|  ,----..      ,---,. 
 /  /    '.  /   /   \ ,`--.' |  ,'  .' |   ,--,:  : | /   /   \   ,'  .' | 
|  :  /`. / |   :     :|   :  :,---.'   |,`--.'`|  ' :|   :     :,---.'   | 
;  |  |--`  .   |  ;. /:   |  '|   |   .'|   :  :  | |.   |  ;. /|   |   .' 
|  :  ;_    .   ; /--` |   :  |:   :  |-,:   |   \ | :.   ; /--` :   :  |-, 
 \  \    `. ;   | ;    '   '  ;:   |  ;/||   : '  '; |;   | ;    :   |  ;/| 
  `----.   \|   : |    |   |  ||   :   .''   ' ;.    ;|   : |    |   :   .' 
  __ \  \  |.   | '___ '   :  ;|   |  |-,|   | | \   |.   | '___ |   |  |-, 
 /  /`--'  /'   ; : .'||   |  ''   :  ;/|'   : |  ; .''   ; : .'|'   :  ;/| 
'--'.     / '   | '/  :'   :  ||   |    \|   | '`--'  '   | '/  :|   |    \ 
  `--'---'  |   :    / ;   |.' |   :   .''   : |      |   :    / |   :   .' 
             \   \ .'  '---'   |   | ,'  ;   |.'       \   \ .'  |   | ,'   
              `---`            `----'    '---'          `---`    `----'     
                                                                            
  """

a2 = r"""
                               ░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░                       
                               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                               ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                         ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░                      
                                                                                            
                                                                                            
 ░▒▓██████▓▒░ ░▒▓███████▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░       ░▒▓██████▓▒░       ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       
 ░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓████████▓▒░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░ 
                                                                                            
                                                                                            
"""

a3 = r"""
              )  (        )                    
           ( /(  )\ )  ( /(                    
       (   )\())(()/(  )\())                   
       )\ ((_)\  /(_))((_)\                    
      ((_)  ((_)(_))   _((_)                   
     _ | | / _ \|_ _| | \| |                   
    | || || (_) || |  | .` |                   
     \__(  \___/|___| (_|\_|              ____ 
   (    )\ )     (    )\ )          (    |   / 
   )\  (()/(     )\  (()/(    (   ( )\   |  /  
 (((_)  /(_))  (((_)  /(_))   )\  )((_)  | /   
 )\___ (_))    )\___ (_))  _ ((_)((_)_   |/    
((/ __|/ __|  ((/ __|| |  | | | | | _ ) (      
 | (__ \__ \   | (__ | |__| |_| | | _ \ )\     
  \___||___/    \___||____|\___/  |___/((_)    
                                               
"""

a4 = r"""
 _       ____________________       ______  ____  ____ 
| |     / / ____/ ___/_  __/ |     / / __ \/ __ \/ __ \
| | /| / / __/  \__ \ / /  | | /| / / / / / / / / / / /
| |/ |/ / /___ ___/ // /   | |/ |/ / /_/ / /_/ / /_/ / 
|__/|__/_____//____//_/___ |__/|__/\____/\____/_____/  
  / ____/ ___/   / ____/ /   / / / / __ )              
 / /    \__ \   / /   / /   / / / / __  |              
/ /___ ___/ /  / /___/ /___/ /_/ / /_/ /               
\____//____/   \____/_____/\____/_____/                
                                                       """

a5 = r"""
  ░██████    ░██████   ░███     ░███ ░█████████       ░██████     ░██████  ░██████
 ░██   ░██  ░██   ░██  ░████   ░████ ░██     ░██     ░██   ░██   ░██   ░██   ░██  
░██        ░██     ░██ ░██░██ ░██░██ ░██     ░██    ░██         ░██          ░██  
░██        ░██     ░██ ░██ ░████ ░██ ░█████████      ░████████  ░██          ░██  
░██        ░██     ░██ ░██  ░██  ░██ ░██                    ░██ ░██          ░██  
 ░██   ░██  ░██   ░██  ░██       ░██ ░██             ░██   ░██   ░██   ░██   ░██  
  ░██████    ░██████   ░██       ░██ ░██              ░██████     ░██████  ░██████
                                                                                  
                                                                                  
                                                                                  
           ░██████  ░██         ░██     ░██ ░████████   ░██ ░██ ░██               
          ░██   ░██ ░██         ░██     ░██ ░██    ░██  ░██ ░██ ░██               
         ░██        ░██         ░██     ░██ ░██    ░██  ░██ ░██ ░██               
         ░██        ░██         ░██     ░██ ░████████   ░██ ░██ ░██               
         ░██        ░██         ░██     ░██ ░██     ░██ ░██ ░██ ░██               
          ░██   ░██ ░██          ░██   ░██  ░██     ░██                           
           ░██████  ░██████████   ░██████   ░█████████  ░██ ░██ ░██               
                                                                                  
                                                                                  
                                                                                  
"""

a6 = r"""      _  ___ ___ _   _                                    
     | |/ _ \_ _| \ | |                                   
  _  | | | | | ||  \| |                                   
 | |_| | |_| | || |\  |                                   
 _\___/ \___/___|_|_\_| _______        _____   ___  ____  
 \ \      / / ____/ ___|_   _\ \      / / _ \ / _ \|  _ \ 
  \ \ /\ / /|  _| \___ \ | |  \ \ /\ / / | | | | | | | | |
   \ V  V / | |___ ___) || |   \ V  V /| |_| | |_| | |_| |
   _\_/\_/_ |_____|____/ |_|  _ \_/\_/__\___/_\___/|____/ 
  / ___/ _ \|  \/  |  _ \| | | |_   _| ____|  _ \         
 | |  | | | | |\/| | |_) | | | | | | |  _| | |_) |        
 | |__| |_| | |  | |  __/| |_| | | | | |___|  _ <         
  \____\___/|_|__|_|_|_ _ \___/__|_|_|_____|_| \_\        
 / ___| / ___|_ _| ____| \ | |/ ___| ____|                
 \___ \| |    | ||  _| |  \| | |   |  _|                  
  ___) | |___ | || |___| |\  | |___| |___                 
 |____/ \____|___|_____|_| \_|\____|_____|                
  / ___| |  | | | | __ )| |                               
 | |   | |  | | | |  _ \| |                               
 | |___| |__| |_| | |_) |_|                               
  \____|_____\___/|____/(_)                               
                                                          """

spacer1 = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
spacer2="\n\n\n\n\n\n\n\n\n\n"

time.sleep(2)

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Join Westwood Computer Science Club!")
turtle.colormode(255)

pen = turtle.Turtle()
pen.speed(0)
pen.width(2)


def clear_screen():
    pen.reset()
    pen.speed(0)
    pen.width(2)
    pen.clear()
    pen.pendown()
    pen.penup()
    pen.pencolor("white")
    pen.fillcolor("white")
    pen.begin_fill()
    pen.goto(-370,375)
    pen.forward(740)
    pen.right(90)
    pen.forward(80)
    pen.right(90)
    pen.forward(740)
    pen.right(90)
    pen.forward(80)
    pen.end_fill()
    pen.goto(0, 300)
    pen.pencolor(189,97,46)
    pen.write("Westwood CS Club", align="center", font=("Verdana", 64, "bold"))
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

def spirograph(duration=10):
    print(spacer1)
    print(a1)
    clear_screen()
    pen.goto(0,0)
    hue_steps = 72
    colors = [colorsys.hsv_to_rgb(i / hue_steps, 1, 1) for i in range(hue_steps)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    start_time = time.time()
    angle = 0
    while time.time() - start_time < duration:
        pen.pencolor(colors[angle % hue_steps])
        pen.circle(100)
        pen.left(10)
        pen.forward(1)
        angle += 1
    time.sleep(2)

def starburst(duration=10):
    print(spacer1)
    print(a3)
    print(spacer2)
    clear_screen()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()

    hue_steps = 100
    colors = [colorsys.hsv_to_rgb(i / hue_steps, 1, 1) for i in range(hue_steps)]
    colors = [(int(r * 255), int(g * 255), int(b * 255)) for r, g, b in colors]

    start_time = time.time()
    angle = 0
    while time.time() - start_time < duration:
        pen.pencolor(colors[angle % hue_steps])
        pen.forward(200)
        pen.backward(200)
        pen.left(6)
        angle += 1
    time.sleep(2)

def sgiri():
    print(spacer1)
    print(a4)
    print(spacer2)
    clear_screen()
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.right(45)
    for i in range(8):
        r2 = 105
        g2 = 195
        b2 = 156
        for i in range(15):
            pen.pencolor(int(r2),int(g2),int(b2))
            r2 = 105-i*105/15
            g2 = 195-i*195/15
            b2 = 156-i*156/15
            pen.circle(5+i*5)
            pen.left(90)
            pen.forward(10)
            pen.right(90)
        pen.right(45)
        pen.penup()
        pen.goto(0, -50)
        pen.pendown()
    time.sleep(2)

def triangle():
    print(spacer1)
    print(a5)
    print(spacer2)
    clear_screen()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    r = 189
    g = 97
    b = 46
    for i in range(100):
     pen.pencolor(int(r),int(g), int(b))
     r = 189-i*189/100
     g = 97-i*97/100
     b = 46-i*46/100
     pen.forward(10+i*5)
     pen.left(120)
    time.sleep(3)

def rose():
    print(spacer1)
    print(a6)
    print(spacer2)
    pen.reset()
    clear_screen()
    pen.speed(0)
    pen.width(2)
    pen.penup()
    pen.goto(100, 0)
    pen.pendown()
    pen.pencolor(255, 0, 163)
    for i in range(200):
     pen.pencolor(255, i, 163)
     pen.circle(100, 60-i)
     pen.left(i)
    time.sleep(3)

def hexagon():
    pen.reset()
    clear_screen()
    pen.width(2)
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    print(spacer1)
    print(a2)
    print(spacer2)
    things = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
    for x in range(200):
        pen.pencolor(things[x%6])
        pen.width(x/100 + 1)
        pen.forward(x)
        pen.left(59)
    time.sleep(2)


designs = [spirograph, triangle, hexagon, sgiri, starburst, rose]

while True:
    for design in designs:
        design()

    pen.clear()
    pen.penup()
    pen.goto(0, 80)
    pen.color("light gray")
    pen.write("Join Westwood", align="center", font=("Courier", 48, "bold"))
    pen.goto(0, 20)
    pen.write("Computer Science Club!", align="center", font=("Courier", 48, "bold"))
    pen.goto(0, -100)
    pen.color("white")
    pen.write("Fill out the interest form!", align="center", font=("Courier", 36))
    pen.hideturtle()
    time.sleep(5)
    pen.showturtle()

turtle.done()
