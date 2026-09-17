class TimeMap:

    def __init__(self):
        self.map_items = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map_items:
            self.map_items[key] = {}

        self.map_items[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map_items:
            return ""

        valid = []

        for t in self.map_items[key]:
            if t <= timestamp:
                valid.append(t)

        if not valid:
            return ""

        return self.map_items[key][max(valid)]
