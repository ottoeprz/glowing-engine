class jugador:

    def __init__(self, username, nombre, nivel, experiencia):
        '''
        Entidad que representa a un jugador y cuyos atributos se usarán
        en la lógica de negocio para establecer los 2 equipos que habrá.
        '''
        self.__username = username
        self.__nombre = nombre
        self.__nivel = nivel
        self.__experiencia = experiencia
