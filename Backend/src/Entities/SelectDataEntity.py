class SelectDataEntity:
    def __init__(self,label:str,value:str) -> None:
        self.label = label
        self.value = value

    label:str
    value:str
    def to_dict(self):
        return{
            "label": self.label,
            "value": self.value
        }