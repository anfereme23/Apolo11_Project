class Content:
    """Clase que representa el contenido de algún objeto."""

    def __init__(
        self, date: str, device_status: str, device_type: str, hash: int, mission: str
    ):
        """
        Constructor de la clase Content.

        :param date: Fecha del contenido.
        :type date: str
        :param device_status: Estado del dispositivo.
        :type device_status: str
        :param device_type: Tipo de dispositivo.
        :type device_type: str
        :param hash: Valor hash.
        :type hash: int
        :param mission: Misión asociada.
        :type mission: str
        """
        self.date = date
        self.device_status = device_status
        self.device_type = device_type
        self.hash = hash
        self.mission = mission
