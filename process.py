import psutil as pt  # psutil - взаимодействие с ядрами


class CpuBar:

    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    @staticmethod
    def cpu_percent_return():
        return pt.cpu_percent(percpu=True)

    @staticmethod
    def cpu_one_return():
        return pt.cpu_percent()

    @staticmethod
    def ram_usage():
        return pt.virtual_memory()

