class Content:
    """Clase que representa el contenido de algún objeto."""

    def __init__(
        self,
        date: str,
        mission: str,
        device_type: str,
        device_status: str,
        hash: str = None,
    ):
        """
        Constructor de la clase Content.

        :param date: Fecha del contenido.
        :type date: str
        :param mission: Misión asociada.
        :type mission: str
        :param device_type: Tipo de dispositivo.
        :type device_type: str
        :param device_status: Estado del dispositivo.
        :type device_status: str
        :param hash: Valor hash.
        :type hash: str

        """
        self.date = date
        self.mission = mission
        self.device_type = device_type
        self.device_status = device_status
        self.hash = hash
