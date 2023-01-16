class partido:

    def __init__(self, motivo, jug1, jug2, jug3, jug4):
        '''
        Entidad que representa a un partido y que se usará en la
        lógica de negocio para establecer los 2 equipos que habrá.
        '''
        self.__motivo = motivo
        self.__jugadores = [jug1, jug2, jug3, jug4]
        self.__equipo1 = []
        self.__equipo2 = []
