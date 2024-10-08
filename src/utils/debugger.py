from io import TextIOWrapper


class Debugger:

    def __init__(self, stream: TextIOWrapper) -> None:
        self.__stream = stream

    def write(self, message: str):
        self.__stream.write(message + "\n")
        self.__stream.flush()
