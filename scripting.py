class Scripts:
    def __init__(self, path: str):
        self.path = path

    def unpack(self, list: list):
        with open(self.path, encoding="UTF8") as txt:
            list_data = txt.readlines()
        for item in list_data:
            item = item.strip()
            list.append(item)
