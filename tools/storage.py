def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Storage:
    def __init__(self):
        self.info = {}

    def store_info(self, name, key):
        self.info[name] = key

    def get_info(self, name):
        return self.info[name]

    def clear_info(self, name):
        del self.info[name]



