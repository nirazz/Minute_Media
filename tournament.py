import hashlib


class Tournament:

    def __init__(self, name, unique_id=None):
        self.name = name
        if unique_id is None:
            self.unique_id = hashlib.sha1(name.encode('utf-8')).hexdigest()
        else:
            self.unique_id = unique_id
