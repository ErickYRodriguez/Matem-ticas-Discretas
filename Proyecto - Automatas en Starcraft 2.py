#!/usr/bin/env python
# coding: utf-8

# ![](https://bnetcmsus-a.akamaihd.net/cms/blog_header/ci/CIGT53U8ZP6M1509744317189.jpg)

# # AUTOMATAS DE UNIDADES EN STARCRAFT 2

# ## Introducción
# 
# Starcraft 2 es un videojuego de estrategia en tiempo real de ciencia ficción militar desarrollado por Blizzard Entertainment. Perteneciente al género RTS fue lanzado el 27 de febrero de 2010 siendo el sucesor de Starcraft y el segundo juego de la saga. En su momento se convertiría en el fenómeno mundial de los esports sobretodo en corea del sur donde sigue siendo ampliamente jugado hasta día de hoy.
# 
# Esencialmente el juego se popularizo por su innovación a la hora de incluir 3 razas distintas pero equilibradas entre sí, lo que ampliaba la posibilidad de juego y diversificaba la estrategia, además estuvo acompañado de un multijugador realmente divertido y competitivo gracias al servicio de Battle.net.

# ## Motivo
# 
# Como todos los juegos RTS starcraft se centra en la gestión y el manejo de unidades, siendo estas la piedra angular del juego y de cada partida, para este proyecto desarrollare los autómatas que describen el comportamiento de estas unidades.
# 
# Esencialmente existen 2 tipos de unidades:

# <li>Ejercito
# <li>Obrero

# Como veremos la principal diferencia entre las unidades es su función, siendo que las unidades de ejercito se centran en la defensa y el ataque lo que se traduce a infligir daño, las unidades Obrero se encargan de la recolección y la infraestructura lo que se traduce a que posibilitan la creación de ejército.

# ---

# ## Diagrama de unidades
# 
# Aqui un diagrama que ejemplifica los tipos de unidades en el videojuego.

# ![](https://i.postimg.cc/nLj3Cm0L/1.jpg)

# ## Autómata para unidad de Trabajo
# 
# Independientemente de la raza, la unidad de trabajo es una sola en las tres, que sería:

# <li>Terran: VCE
# <li>Protoss: Sonda
# <li>Zerg: Zángano 

# ![](https://bnetcmsus-a.akamaihd.net/cms/content_entry_media/ms/MSIGJA6VN30C1437704141929.gif)

# ---

# El autómata del VCE es el siguiente:
# 
# **Estados**
# <li>Idle (I): El VCE no está realizando ninguna acción.
# <li>Moving (M): El VCE se está moviendo a un destino.
# <li>Gathering Resources (G): El VCE está recolectando minerales o gas.
# <li>Building (B): El VCE está construyendo un edificio.
# <li>Repairing (R): El VCE está reparando una estructura o unidad.
# <li>Under Attack (U): El VCE está siendo atacado.

# **Transiciones**
# <li>Move Command (move): Comando para que el VCE se mueva a una ubicación específica.
# <li>Gather Command (gather): Comando para que el VCE comience a recolectar recursos.
# <li>Build Command (build): Comando para que el VCE comience a construir un edificio.
# <li>Repair Command (repair): Comando para que el VCE repare una estructura o unidad.
# <li>Stop Command (stop): Comando para que el VCE detenga su acción actual.
# <li>Under Attack (attacked): Transición automática cuando el VCE es atacado.
# <li>Return to Idle (idle): Transición automática cuando el VCE termina una tarea y no tiene ninguna otra tarea asignada.

# ![](https://i.postimg.cc/vm790W48/T.jpg)

# A=
# <ul>
# <li>Q= {I,U,G,M,B,D,R}
# <li>Σ= {attacked, repair, move, build, gather, stop}
# <li>ð= -
# <li>q0= I
# <li>F= {D}

# ![](https://i.postimg.cc/4d50R7Ss/DT.jpg)

# De las tres razas los obreros terran denominados como VCE son los que tienen el set de habilidades más completo, puesto que al igual que sus equivalentes en las otras razas tienen la capacidad de recolectar recursos, pero además pueden realizar reparaciones sobre edificios o unidades mecánicas y tienen la peculiaridad de que al construir un edificio lo hacen manualmente, por lo que hay que esperar un periodo de tiempo dependiendo la estructura en cuestión.

# ---

# El autómata de la sonda es el siguiente:
# 
# **Estados**
# <li>Idle (I): La Sonda no está realizando ninguna acción.
# <li>Moving (M): La Sonda se está moviendo a un destino.
# <li>Gathering Resources (G): La Sonda está recolectando minerales o gas.
# <li>Under Attack (U): La Sonda está siendo atacada.

# **Transiciones**
# <li>Move Command (move): Comando para que la Sonda se mueva a una ubicación específica.
# <li>Gather Command (gather): Comando para que la Sonda comience a recolectar recursos.
# <li>Build Command (build): Comando para que la Sonda inicie la construcción de un edificio.
# <li>Stop Command (stop): Comando para que la Sonda detenga su acción actual.
# <li>Under Attack (attacked): Transición automática cuando la Sonda es atacada.
# <li>Return to Idle (idle): Transición automática cuando la Sonda termina una tarea y no tiene ninguna otra tarea asignada.

# ![](https://i.postimg.cc/pLFKFNxF/P.jpg)

# A=
# <ul>
# <li>Q= {I,U,G,M,IB,D}
# <li>Σ= {attacked, move, iniatilize building, gather, stop}
# <li>ð= -
# <li>q0= I
# <li>F= {D}

# ![](https://i.postimg.cc/Y0Csrr5g/DP.jpg)

# Nótese que a diferencia del obrero terran, la sonda protoss no se detiene a construir un edificio, sino que simplemente inicializa la construcción pasando directamente al estado "idle", además la sondas protoss no realizan ningún tipo de reparación.

# ---

# El autómata del zángano es el siguiente:
# 
# **Estados**
# <li>Idle (I): El Zángano no está realizando ninguna acción.
# <li>Moving (M): El Zángano se está moviendo a un destino.
# <li>Gathering Resources (G): El Zángano está recolectando minerales o gas.
# <li>Transforming into Building (T): El Zángano se está transformando en un edificio.
# <li>Under Attack (U): El Zángano está siendo atacado.

# **Transiciones**
# <li>Move Command (move): Comando para que el Zángano se mueva a una ubicación específica.
# <li>Gather Command (gather): Comando para que el Zángano comience a recolectar recursos.
# <li>Build Command (build): Comando para que el Zángano se transforme en un edificio.
# <li>Stop Command (stop): Comando para que el Zángano detenga su acción actual.
# <li>Under Attack (attacked): Transición automática cuando el Zángano es atacado.
# <li>Return to Idle (idle): Transición automática cuando el Zángano termina una tarea y no tiene ninguna otra tarea asignada.
# 

# ![](https://i.postimg.cc/MGJV0sKr/Z.jpg)

# A=
# <ul>
# <li>Q= {I,U,G,M,B,D}
# <li>Σ= {attacked, gather, move, build, stop}
# <li>ð= -
# <li>q0= I
# <li>F= {D}

# ![](https://i.postimg.cc/d3NSLMFf/DZ.jpg)

# Finalmente, nótese que él automata del zerg llega a su estado final al ser atacado (igual que los demás) o bien al construir algún edificio, ya que una característica de los zerg es que el obrero se convierte directamente en el edificio.

# ---

# ## Autómata para unidad de Ejercito
# 
# Por otra parte, dentro de las unidades del ejercitoexisten dos tipos de unidades diferentes pero que de igual forma son iguales en las tres razas con aspecto y características propias pero equivalentes.

# Estos dos tipos de unidades dentro del ejercito son:

# <li>Utilidad
# <li>Ataque

# ![](https://bnetcmsus-a.akamaihd.net/cms/page_media/NVVHYQPXAEG41462324653220.gif)

# La principal diferencia es que las unidades de Utilidad no hacen daño directo o no poseen ataques básicos, en su lugar hace uso de habilidades especificas o cumple con funciones propias que pueden afectar tanto positiva como negativamente a unidades aliadas o enemigas, por su parte las unidades del ejercito que son de ataque se centran totalmente en infligir daño.

# ---

# De esta forma el autómata de una unidad de Ataque es el siguiente:
#     
# **Estados**
# <li>Idle (I): La unidad no está realizando ninguna acción.
# <li>Moving (M): La unidad se está moviendo a un destino.
# <li>Attacking (A): La unidad está atacando a un enemigo.
# <li>Under Attack (U): La unidad está siendo atacada.
# <li>Dead (D): La unidad ha sido destruida.

# **Transiciones**
# <li>Move Command (move): Comando para que la unidad se mueva a una ubicación específica.
# <li>Attack Command (attack): Comando para que la unidad ataque a un enemigo.
# <li>Stop Command (stop): Comando para que la unidad detenga su acción actual.
# <li>Under Attack (attacked): Transición automática cuando la unidad es atacada.
# <li>Unit Dies (die): Transición automática cuando la unidad es destruida.
# <li>Return to Idle (idle): Transición automática cuando la unidad termina una tarea y no tiene ninguna otra tarea asignada.
# 

# ![](https://i.postimg.cc/wMMwKWNQ/UA.jpg)

# A=
# <ul>
# <li>Q= {I,U,M,D}
# <li>Σ= {attacked, attack, move, die, stop}
# <li>ð= -
# <li>q0= I
# <li>F= {D}

# ![](https://i.postimg.cc/JnmFFcKp/DA.jpg)

# ---

# De esta forma el autómata de una unidad de Utilidad es el siguiente:
#     
# **Estados**
# <li>Idle (I): La unidad no está realizando ninguna acción.
# <li>Moving (M): La unidad se está moviendo a un destino.
# <li>Using Ability (A): La unidad está usando una habilidad especial.
# <li>Under Attack (U): La unidad está siendo atacada.
# <li>Dead (D): La unidad ha sido destruida.

# **Transiciones**
# <li>Move Command (move): Comando para que la unidad se mueva a una ubicación específica.
# <li>Use Ability Command (use_ability): Comando para que la unidad use una habilidad especial.
# <li>Stop Command (stop): Comando para que la unidad detenga su acción actual.
# <li>Under Attack (attacked): Transición automática cuando la unidad es atacada.
# <li>Unit Dies (die): Transición automática cuando la unidad es destruida.
# <li>Return to Idle (idle): Transición automática cuando la unidad termina una tarea y no tiene ninguna otra tarea asignada.
# 

# ![](https://i.postimg.cc/2620Kp15/UU.jpg)

# A=
# <ul>
# <li>Q= {I,U,UA,M,D}
# <li>Σ= {attacked, use ability, move, die, stop}
# <li>ð= -
# <li>q0= I
# <li>F= {D}

# ![](https://i.postimg.cc/9fyS1NP4/DU.jpg)

# ---

# ## Ejemplo en codigo

# **Ejemplo simple en codigo de la ejecución de un VCE**
# <ul>
#     Por ultimo un ejemplo basico de como responderia un VCE a ciertos comandos por ejemplo: {Gather, Gather, Build, Attacked, Died}, que seria una representación de una vida util promedio para una unidad de este tipo.

# In[ ]:


class VCEAutomaton:
    def __init__(self):
        self.state = 'Idle'
        self.attacked_count = 0  # Contador

    def move(self):
        if self.state in ['Idle', 'Moving', 'Gathering', 'Repairing']:
            self.state = 'Moving'
            print(f"Transitioned to: {self.state}")

    def gather(self):
        if self.state in ['Idle', 'Moving']:
            self.state = 'Gathering'
            print(f"Transitioned to: {self.state}")

    def build(self):
        if self.state in ['Idle', 'Moving']:
            self.state = 'Building'
            print(f"Transitioned to: {self.state}")

    def repair(self):
        if self.state in ['Idle', 'Moving']:
            self.state = 'Repairing'
            print(f"Transitioned to: {self.state}")

    def stop(self):
        if self.state in ['Moving', 'Gathering', 'Building', 'Repairing']:
            self.state = 'Idle'
            print(f"Transitioned to: {self.state}")

    def attacked(self):
        self.attacked_count += 1
        if self.attacked_count >= 2:
            self.state = 'Dead'
            print(f"Transitioned to: {self.state}")
        else:
            self.state = 'Under Attack'
            print(f"Transitioned to: {self.state}")

    def die(self):
        self.state = 'Dead'
        print(f"Transitioned to: {self.state}")

    def idle(self):
        if self.state in ['Gathering', 'Building', 'Repairing', 'Under Attack']:
            self.state = 'Idle'
            print(f"Transitioned to: {self.state}")

    def get_state(self):
        return self.state

vce = VCEAutomaton()
print(f"Estado inicial: {vce.get_state()}")

commands = {
    "move": vce.move,
    "gather": vce.gather,
    "build": vce.build,
    "repair": vce.repair,
    "stop": vce.stop,
    "attacked": vce.attacked,
    "die": vce.die,
    "idle": vce.idle
}

while True:
    command = input("Ingresa un comando (move, gather, build, repair, stop, attacked, die, idle) o 'exit' para salir: ").strip().lower()
    if command == 'exit':
        break
    elif command in commands:
        commands[command]()
        print(f"Estado actual: {vce.get_state()}")
    else:
        print("Comando no válido. Inténtalo de nuevo.")


# In[6]:


import pygame
import sys

pygame.init()

#Pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Automata de un VCE:")


# Imágenes (estados)
image_initial = pygame.image.load('imagenes/2.1.jpg')
image_alternative_1 = pygame.image.load('imagenes/1.png')
image_alternative_2 = pygame.image.load('imagenes/3.png')
image_alternative_3 = pygame.image.load('imagenes/4.png')
image_alternative_4 = pygame.image.load('imagenes/5.png')
image_alternative_5 = pygame.image.load('imagenes/6.png')
image_alternative_6 = pygame.image.load('imagenes/7.png')


# Estado actual de la tecla presionada
current_key = None
next_key = None
color_start_time = None
color_duration = 2000  # 2 segundos de espera entre estados


#Funciones para mostrar los estados
def mostrar_imagen_temporal_move():
    screen.blit(image_alternative_1, (0, 0))

def mostrar_imagen_temporal_gather():
    screen.blit(image_alternative_2, (0, 0))

def mostrar_imagen_temporal_build():
    screen.blit(image_alternative_3, (0, 0))

def mostrar_imagen_temporal_repair():
    screen.blit(image_alternative_4, (0, 0))

def mostrar_imagen_temporal_attacked():
    screen.blit(image_alternative_5, (0, 0))

def mostrar_imagen_temporal_dead():
    screen.blit(image_alternative_6, (0, 0))

def mostrar_imagen_temporal_idle():
    screen.blit(image_initial, (0, 0))


#Función para la detección de teclas presionadas (Transiciones)
def handle_events():
    global current_key, next_key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5):
                if current_key is None:
                    current_key = event.key
                    start_event(current_key)
                    return True  # Iniciar el temporizador
                else:
                    next_key = event.key  # Guardar la siguiente tecla a usar
            elif event.key == pygame.K_i:
                current_key = None
                next_key = None
                print("Acción interrumpida")
                return False  # Interrumpir y resetear el temporizador
    return False

#Función encargada de imprimir un aviso de inicio dependiendo el estado
def start_event(key):
    if key == pygame.K_1:
        print("Moviendo al VCE...")
    elif key == pygame.K_2:
        print("El VCE está minando...")
    elif key == pygame.K_3:
        print("El VCE está construyendo...")
    elif key == pygame.K_4:
        print("El VCE está reparando...")
    elif key == pygame.K_5:
        print("El VCE está siendo atacado...")

#Función encargada de imprimir un aviso de finalización dependiendo el estado
def end_event(key):
    if key == pygame.K_1:
        print("El VCE llegó a su destino")
    elif key == pygame.K_2:
        print("+5 de mineral...")
    elif key == pygame.K_3:
        print("Estructura finalizada")
    elif key == pygame.K_4:
        print("Reparación finalizada")
    elif key == pygame.K_5:
        print("El VCE murió...")

#Bucle principal
def main():
    global current_key, next_key, screen_start_time
    while True:
        reset_timer = handle_events()

        if reset_timer:
            screen_start_time = pygame.time.get_ticks()

        if current_key is not None and screen_start_time is not None:
            elapsed_time = pygame.time.get_ticks() - screen_start_time
            if elapsed_time > color_duration:
                if current_key == pygame.K_5:
                    end_event(current_key)
                    # Mostrar 2 segundos del estado dead después de Key_5
                    screen_start_time = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - screen_start_time < 2000:
                        mostrar_imagen_temporal_dead()
                        pygame.display.flip()
                    pygame.quit()
                    sys.exit()
                else:
                    end_event(current_key)
                    current_key = next_key
                    next_key = None
                    screen_start_time = None if current_key is None else pygame.time.get_ticks()
                    if current_key is not None:
                        start_event(current_key)
        #Detección de teclas
        if current_key == pygame.K_1:
            mostrar_imagen_temporal_move()
        elif current_key == pygame.K_2:
            mostrar_imagen_temporal_gather()
        elif current_key == pygame.K_3:
            mostrar_imagen_temporal_build()
        elif current_key == pygame.K_4:
            mostrar_imagen_temporal_repair()
        elif current_key == pygame.K_5:
            mostrar_imagen_temporal_attacked()
        else:
            mostrar_imagen_temporal_idle()

        pygame.display.flip()

if __name__ == "__main__":
    main()


# ---

# **Notas:**
# <ul>
# <li>Los diagramas son originales, la decisión de utilizar palabras en ingles es para respetar los comandos originales del juego.
# <li>El estado inicial de todas las unidades es "idle" ya que es el estado primero y basico de todas las unidades desde que son creadas en sus respectivos edificios.
# <li>El estado final o de aceptación de todas las unidades no es idle sino "dead", puesto que por la naturaleza del juego el objetivo esperado de todas las unidades es finalmente morir.

# **LINKS A DIAGRAMAS:**
# 
# [Recursos de imagen](https://www.canva.com/design/DAGHlu6hulw/GQDxD5Bg82OVpkTVxF7O8A/edit?utm_content=DAGHlu6hulw&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

# **Referencias:**
# <ul>
# <li>StarCraft II. (s. f.). https://starcraft2.blizzard.com/es-es/
# 
# <li>colaboradores de Wikipedia. (2024e, enero 22). StarCraft II: Wings of Liberty. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty
# 
# <li>StarCraftWiki, C. T. (s. f.). StarCraft II. StarCraftWiki. https://starcraft.fandom.com/es/wiki/StarCraft_II
# 
# <li>Joe Llerena. (2010, 25 julio). Teoría de autómatas [Vídeo]. YouTube. https://www.youtube.com/watch?v=pfJSqvQFOxI
#     
# <li> OpenAI. (2024). Descripción del autómata para una unidades en Starcraft 2. Asistencia proporcionada por ChatGPT. OpenAI.
#     
# <li>SC2 p — Postimages. (s. f.). https://postimg.cc/gallery/HrpVWY1
