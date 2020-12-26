class BaseModel:

    def __repr__(self):
        return f'{self.__class__.__name__} {self.id}'

    def to_json(self):
        dictionary: dict = self.__dict__
        dictionary.pop('_sa_instance_state')
        return dictionary
