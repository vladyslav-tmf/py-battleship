class Deck:
    def __init__(self, row: int, column: int) -> None:
        self.row = row
        self.column = column
        self.is_alive = True


class Ship:
    def __init__(self, start: tuple[int, int], end: tuple[int, int]) -> None:
        self.start = start
        self.end = end
        self.decks = self._create_decks()
        self.is_drowned = False

    def _create_decks(self) -> list[Deck]:
        decks = []

        if self.start[0] == self.end[0]:
            for column in range(self.start[1], self.end[1] + 1):
                decks.append(Deck(self.start[0], column))
        else:
            for row in range(self.start[0], self.end[0] + 1):
                decks.append(Deck(row, self.start[1]))

        return decks

    def get_deck(self, row: int, column: int) -> Deck | None:
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck

        return None

    def fire(self, row: int, column: int) -> str:
        deck = self.get_deck(row, column)

        if deck:
            deck.is_alive = False
            if all(not deck.is_alive for deck in self.decks):
                self.is_drowned = True
                return "Sunk!"
            return "Hit!"


class Battleship:
    def __init__(self, ships: list[tuple]) -> None:
        self.field = {}

        for ship_coords in ships:
            ship = Ship(ship_coords[0], ship_coords[1])
            self._add_ship_to_field(ship)

    def _add_ship_to_field(self, ship: Ship) -> None:
        for deck in ship.decks:
            self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple[int, int]) -> str:
        if location in self.field:
            ship = self.field[location]
            return ship.fire(*location)
        return "Miss!"
