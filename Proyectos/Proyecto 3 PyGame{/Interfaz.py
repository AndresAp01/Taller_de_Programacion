# interfaz_pygame.py
import pygame
import sys
import proyecto_3 as proj  # Asegúrate de que proyecto_3.py esté en el mismo directorio

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interfaz de Restaurante")
FONT = pygame.font.SysFont(None, 32)
CLOCK = pygame.time.Clock()

class Button:
    def __init__(self, rect, text, callback, color=(200,200,200), hover_color=(170,170,170)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.color = color
        self.hover_color = hover_color

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        is_hover = self.rect.collidepoint(mouse)
        pygame.draw.rect(surface, self.hover_color if is_hover else self.color, self.rect)
        txt_surf = FONT.render(self.text, True, (0,0,0))
        txt_rect = txt_surf.get_rect(center=self.rect.center)
        surface.blit(txt_surf, txt_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.callback()


def admin_screen():
    # Aquí puedes agregar la lógica para administradores (reportes, modificaciones, etc.)
    print("Vista de Administrador activada")


def client_screen():
    cedula = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    cedula = cedula[:-1]
                else:
                    cedula += event.unicode
        screen.fill((255,255,255))
        prompt = FONT.render("Ingrese cédula:", True, (0,0,0))
        screen.blit(prompt, (50, 150))
        input_surf = FONT.render(cedula, True, (0,0,0))
        screen.blit(input_surf, (50, 200))
        pygame.display.flip()
        CLOCK.tick(30)

    # Validación de cliente
    valid = proj.validar_cliente_existe(proj.cli, cedula)
    if valid is True:
        print(f"Cliente válido: {cedula}")
        # Por ahora llamamos la función de consola; luego podrás migrar totalmente al GUI
        proj.registrar_compra_menu(proj.dic, proj.cli, lambda prompt="": cedula)
    else:
        print(f"Cliente no encontrado: {cedula}")


def main():
    admin_btn=Button((WIDTH//4 -75, HEIGHT//2 -25,150,50), "Administrador", admin_screen)
    client_btn=Button((3*WIDTH//4 -75, HEIGHT//2 -25,150,50), "Cliente", client_screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            admin_btn.handle_event(event)
            client_btn.handle_event(event)
        screen.fill((255,255,255))
        admin_btn.draw(screen)
        client_btn.draw(screen)
        pygame.display.flip()
        CLOCK.tick(30)

if __name__ == "__main__":
    main()
