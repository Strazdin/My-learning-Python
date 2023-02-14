class GroundTransport:
    def __init__(self):
        self.properties_ground_transport = {'move': False, 'speed': 0, 'color': '', 'plate_number': '', 'serial_number': ''}
        self.experiment = 'GroundTransport'
    
    def switch_moving(self, command):
        if command == 'go':
            self.properties_ground_transport['move'] = True
            speed = int(input('Установите скорость: '))
            self.properties_ground_transport['speed'] = speed
        elif command == 'stop':
            self.properties_ground_transport['move'] = False
            self.properties_ground_transport['speed'] = 0

    #Вопрос 1: а методы set/getattr уже не будут работать если св-во словарь? 

    def set_color(self, color):
        self.properties_ground_transport['color'] = color

    def set_plate_number(self, plate_number):
        self.properties_ground_transport['plate_number'] = plate_number

    def set_serial_number(self, serial_number):
        self.properties_ground_transport['serial_number'] = serial_number

    def for_experiment(self):
        return 'experiment GroundTransport'

class WheeledTransport(GroundTransport):
    def __init__(self, wheels: int, type: 'str', color: 'str', plate_number: 'str'):
        GroundTransport.__init__(self)
        self.properties_wheel_transport = {'wheels': wheels, 'type': type}
        self.properties_ground_transport['color'] = color
        self.properties_ground_transport['plate_number'] = plate_number
        self.experiment = 'WheeledTransport'
        #Вопрос 2. А как сделать так чтобы объект не создавался, когда в св-во wheels будет передано значение 0

    def for_experiment(self):
        return 'experiment WheeledTransport'

# остальные два класса просто демонстрируют дальнейшую иерархию с наследованием св-св у родителя 
class CaterpillarTransport(GroundTransport):
    def __init__(self, type: 'str'):
        GroundTransport.__init__(self)
        self.caterpillar_transport = {'type': type}

class Hovercraft(GroundTransport):
    def __init__(self, type: 'str'):
        GroundTransport.__init__(self)
        self.hovercraft = {'type': type}

my_transport = WheeledTransport(wheels := 2, type := 'bike', color := 'grey', plate_number := '')
my_transport.switch_moving('go')
print(my_transport.__dict__)

print(my_transport.for_experiment())
# Вопрос 3: как достучаться до переопределенного св-ва/методы родительского класса? Или этим не пользуются?
print(my_transport.experiment)