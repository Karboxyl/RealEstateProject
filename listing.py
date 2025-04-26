class lst:
    def __init__(self, name: str = "", location: str = "",price: float = 0.0, sqm: float = 0.0) -> None:
        self.name = name
        self.location = location
        self.price = price
        self.sqm = sqm
    def __str__(self):
        return f"name:{self.name},location{self.location},price:{self.price},sqm:{self.sqm}"