class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return "Config(" + ",".join(f"{name}={val}" for name, val in self.__dict__.items()) + ")"
