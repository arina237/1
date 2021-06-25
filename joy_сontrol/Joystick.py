import pygame
import math

class Joystick:

    def __init__(self):
        self.joystick_count = pygame.joystick.get_count() # количество подключенных джойстиков
        self.joyInd = [None, None, None, None] # массив хранения индексов джойстиков. Порядок храннения: PS4, cobra, xBox

        # Выдача джойстикам соответствующих индексов
        for i in range(self.joystick_count):
            joystick = pygame.joystick.Joystick(i)
            print(joystick.get_name())
            if joystick.get_name() == "PS4 Controller":
                self.joyInd[0] = i
            if joystick.get_name() == "Defender COBRA M5 USB Joystick":
                self.joyInd[1] = i
            if joystick.get_name() == "Xbox 360 Controller":
                self.joyInd[2] = i
            if joystick.get_name() == "Controller (Rumble Gamepad F510)":
                self.joyInd[3] = i

        self.joystick = [None, None, None, None] # Массив хрнения джойстиков. Порядок храннения: PS4, cobra, xBox
        for i in range(4):
            if self.joyInd[i] is not None:
                self.joystick[i] = pygame.joystick.Joystick(self.joyInd[i])  # создаем объект джойстик
                self.joystick[i].init()  # инициализируем джойстик
                print('Джойстик подключен: ' + self.joystick[i].get_name())
                print(i)
                break
            else:
                print("Джойстик не найден")

        # скорость изменения координат
        self.increment_xy = float(0.1)
        self.increment_z = float(0.025)
        self.increment_deg = math.radians(float(8))
        self.new_command = False
        print(self.joyInd)
        print(self.joystick)

    def joyhandler(self, x, y, z, yaw):
        return self.__ps4_xbox(0.2, x, y, z, yaw)


    def __ps4_xbox(self, threshold, x, y, z, yaw):
        print(self.joyInd)
        for i in range(4):
            if self.joyInd[i] is not None:
                print(i)
                # считывание значения осей
                axis0 = self.joystick[i].get_axis(0)
                axis1 = self.joystick[i].get_axis(1)
                axis2 = self.joystick[i].get_axis(2)
                axis3 = self.joystick[i].get_axis(3)

                #  левый стик, движение влево вправо
                if (axis3 > threshold) or (axis3 < -threshold):
                    x += self.increment_xy * axis3 * math.sin(yaw)
                    y += self.increment_xy * -axis3 * math.cos(yaw)
                    self.new_command = True

                #  левый стик, движение  вверх вниз
                elif (axis2 > threshold) or (axis2 < -threshold):
                    x += self.increment_xy * axis2 * math.cos(yaw)
                    y += self.increment_xy * axis2 * math.sin(yaw)
                    self.new_command = True

                #  правый стик, движение влево вправо
                if (axis0 > threshold) or (axis0 < -threshold):
                    yaw -= self.increment_deg * axis0
                    self.new_command = True

                #  правый стик, движение вперед назад
                elif (axis1 > threshold) or (axis1 < -threshold):
                    z += self.increment_z * -axis1
                    self.new_command = True

        return x,y,z,yaw


