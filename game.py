import numpy as np
import time


class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'wait'

    def run(self):
        while True:
            self.vision.refresh_frame()
            if self.state == 'wait' and self.can_start():
                self.log('Comando START SPAM detectado')
                self.state = 'not started'
            elif self.state == 'not started' and self.mejorar_trigo():
                self.log('Buscando trigo')
                self.click_mejoratrigo()
                self.state = 'started'
            elif self.state == 'started' and self.posible_mejora():
                self.log('Trigo encontrado, mejorando')
                self.click_mejorar()
                self.state = 'mejoraposible'
            elif self.state == 'mejoraposible' and self.puede_mejorar():
                self.log('Mejora Realizada')
                self.click_to_mejora2()
                self.state = 'ready for help'
            elif self.state == 'ready for help' and self.posible_ayuda():
                self.log('Presionando ayuda')
                self.click_ayuda()
                self.state = 'ready to cancel'
            elif self.state == 'ready to cancel' and self.puede_cancelar():
                self.log('Abriendo construccion')
                self.click_cancelar()
                self.state = 'ready to cancel2'
            elif self.state == 'ready to cancel2' and self.puede_cancelar2():
                self.log('Cancelando construccion')
                self.click_cancelar2()
                self.state = 'confirmar'
            elif self.state == 'confirmar' and self.puede_confirmar():
                self.log('Confirmando')
                self.click_confirmar()
                self.state = 'not started'
                if self.can_stop():
                    self.state = 'wait'
                    self.log('Deteniendo SPAM comando detectado')
            elif self.state == 'wait' and self.puede_manitas():
                self.log('Entrado a ayudas')
                self.click_manitas()
                self.state = 'manitas'
            elif self.puede_ayudar():
                self.log('Ayudar a todos')
                self.click_ayudartodos()
                self.state = 'ayudo'
                if self.state == 'ayudo' and self.puede_salir():
                    self.log('Saliendo de las ayudas')
                    self.click_salir()
                    self.state = 'wait'
            elif self.state == 'wait' and self.posible_barco():
                self.log('Entrando al barco')
                self.click_barco()
                self.state = 'enbarco'
                if self.state == 'enbarco' and self.puede_intercambiar():
                    self.log('Realizando intercambio..')

            else:
                self.log('Esperando para realizar accion')
            time.sleep(1)

   # verificar si hay solicitd
    # def can_solicitud(self):
    #     matches = self.vision.find_template('solicitud')
    #     return np.shape(matches)[1] >= 1

    # ENVIAR MENSAJE

    def can_start(self):
        matches = self.vision.find_template('start')
        return np.shape(matches)[1] >= 1

    def can_stop(self):
        matches = self.vision.find_template('stop')
        return np.shape(matches)[1] >= 1

    def mejorar_trigo(self):
        matches = self.vision.find_template('trigo_subir')
        return np.shape(matches)[1] >= 1

    def click_mejoratrigo(self):

        matches = self.vision.find_template('trigo_subir')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x+5, y)
        self.controller.left_mouse_click()

    # Verificar si existe la imagen del barco

    def posible_barco(self):
        matches = self.vision.find_template('barco_carga')
        return np.shape(matches)[1] >= 1

    def click_barco(self):
        matches = self.vision.find_template('barco_carga')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()
# Verificar si existe la imagen del intercambio

    def posible_barco(self):
        matches = self.vision.find_template('intercambio_barco')
        return np.shape(matches)[1] >= 1

    def click_barco(self):
        matches = self.vision.find_template('intercambio_barco')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

    # verificar si el boton ayuda esta disponible y presionar
    def posible_ayuda(self):
        matches = self.vision.find_template('ayudar')
        return np.shape(matches)[1] >= 1

    def click_ayuda(self):

        matches = self.vision.find_template('ayudar')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

    # verificar si el boton cancelar
    def puede_cancelar(self):
        matches = self.vision.find_template('mejorando2')
        return np.shape(matches)[1] >= 1

    def click_cancelar(self):

        matches = self.vision.find_template('mejorando2')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()
 # verificar si el boton cancelar2

    def puede_cancelar2(self):
        matches = self.vision.find_template('cancelar')
        return np.shape(matches)[1] >= 1

    def click_cancelar2(self):

        matches = self.vision.find_template('cancelar')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        # verificar si el boton confirmar

    def puede_confirmar(self):
        matches = self.vision.find_template('si')
        return np.shape(matches)[1] >= 1

    def click_confirmar(self):

        matches = self.vision.find_template('si')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

    def puede_mejorar(self):
        matches = self.vision.find_template('mejorar2')
        return np.shape(matches)[1] >= 1

    def click_to_mejora2(self):
        matches = self.vision.find_template('mejorar2')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x+50, y+30)
        self.controller.left_mouse_click()

        time.sleep(0.5)

     #  PUEDEMANITAS
    def puede_manitas(self):
        matches = self.vision.find_template('boton_ayudar')
        return np.shape(matches)[1] >= 1

    def click_manitas(self):

        matches = self.vision.find_template('boton_ayudar')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

    # PUEDE AYUDARA TODOS
    def puede_ayudar(self):
        matches = self.vision.find_template('ayudar_todos')
        return np.shape(matches)[1] >= 1

    def click_ayudartodos(self):

        matches = self.vision.find_template('ayudar_todos')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        # salir
    def puede_salir(self):
        matches = self.vision.find_template('salir')
        return np.shape(matches)[1] >= 1

    def click_salir(self):

        matches = self.vision.find_template('salir')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

    def can_start_round(self):
        matches = self.vision.find_template('next-button')
        return np.shape(matches)[1] >= 1

    def start_round(self):
        matches = self.vision.find_template('next-button')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x+100, y+30)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def has_full_rocket(self):
        matches = self.vision.find_template('full-rocket', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def use_full_rocket(self):
        matches = self.vision.find_template('full-rocket')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def posible_mejora(self):
        matches = self.vision.find_template(
            'mejorar', threshold=0.9)
        return np.shape(matches)[1] >= 1

    def click_mejorar(self):
        matches = self.vision.find_template('mejorar')

        x = matches[1][0]
        y = matches[0][0]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def log(self, text):
        print('[%s] %s' % (time.strftime('%H:%M:%S'), text))
