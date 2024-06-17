import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configura la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Eventos con Temporizador y Colores")


# Carga imágenes
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
color_duration = 2000  # 2 segundos en milisegundos

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

def main():
    global current_key, next_key, color_start_time
    while True:
        reset_timer = handle_events()

        if reset_timer:
            color_start_time = pygame.time.get_ticks()

        if current_key is not None and color_start_time is not None:
            elapsed_time = pygame.time.get_ticks() - color_start_time
            if elapsed_time > color_duration:
                if current_key == pygame.K_5:
                    end_event(current_key)
                    # Mostrar 2 segundos de color naranja después de Key_5
                    color_start_time = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - color_start_time < 2000:
                        mostrar_imagen_temporal_dead()
                        pygame.display.flip()
                    pygame.quit()
                    sys.exit()
                else:
                    end_event(current_key)
                    current_key = next_key
                    next_key = None
                    color_start_time = None if current_key is None else pygame.time.get_ticks()
                    if current_key is not None:
                        start_event(current_key)

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
