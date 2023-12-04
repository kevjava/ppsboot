from ppsboot.utils.solution import Solution


class BingoCard:

    def __init__(self, numbers: list[int, 2]) -> None:
        self._numbers = numbers

    def __repr__(self) -> str:
        ret = ''
        for row in self._numbers:
            for num in row:
                ret += f"{num:2} "
            ret += '\n'
        return ret

    def __diagonals(self) -> list[list[int]]:
        return [[self._numbers[i][i] for i in range(5)],
                [self._numbers[i][4-i] for i in range(5)]]

    def __rows(self) -> list[list[int]]:
        return self._numbers

    def __columns(self) -> list[list[int]]:
        return [[self._numbers[i][j] for i in range(5)] for j in range(5)]

    def all_lines(self) -> list[list[int]]:
        return self.__rows() + self.__columns()  # + self.__diagonals()

    def score(self, called_numbers: list[int]) -> int:
        """ Returns the score of the card. """
        all_numbers = [num for row in self._numbers for num in row]
        unmarked_numbers = [num for num in all_numbers if num not in called_numbers]
        return sum(unmarked_numbers * called_numbers[-1])

    def is_winner(self, called_numbers: list[int]) -> bool:
        """ Returns true if the card is a winner. """
        for line in self.all_lines():
            if all([num in called_numbers for num in line]):
                return True
        return False


class BingoGame:

    def __init__(self, called_numbers: list[int], bingo_cards: list[BingoCard]) -> None:
        self.__called_numbers = called_numbers
        self.__bingo_cards = bingo_cards

    @property
    def called_numbers(self) -> list[int]:
        return self.__called_numbers

    @property
    def cards(self) -> list[BingoCard]:
        return self.__bingo_cards

    def __repr__(self) -> str:
        ret = ''
        ret += "Called numbers\n"
        ret += f"{self.__called_numbers}\n"
        ret += "Cards\n"
        for card in self.__bingo_cards:
            ret += f"{card}\n"
        return ret


class Day4(Solution):
    """ Day 4's solution. """

    def __init__(self):
        super().__init__(4, 'ppsboot/days/d04/input.txt')

    def load_input(self, filename: str) -> BingoGame:
        with open(self._filename) as f:
            called_numbers = [int(num) for num in f.readline().strip().split(',')]
            f.readline()

            bingo_cards = []
            bingo_card_lines = [line.strip() for line in f.readlines()]
            line_no = 0
            for line_no in range(0, len(bingo_card_lines), 6):
                bingo_cards.append(BingoCard([[int(x) for x in line.strip().split()]
                                              for line in bingo_card_lines[line_no:line_no+5]]))

            return BingoGame(called_numbers, bingo_cards)

    def score_first_winner(self, game: BingoGame) -> int:
        """ Returns the score of the first winner. """
        for i in range(len(game.called_numbers)):
            called_numbers = game.called_numbers[:i+1]
            for card in game.cards:
                if card.is_winner(called_numbers):
                    return card.score(called_numbers)
        return 0

    def score_last_winner(self, game: BingoGame) -> int:
        """ Returns the score of the last winner.

        Loop through called numbers. If we have multiple cards left,
        remove the winners. If there's one left, return that score.
        """
        cards = game.cards
        for i in range(len(game.called_numbers)):
            called_numbers = game.called_numbers[:i+1]
            if (len(cards) > 1):
                winning_cards = [card for card in cards if card.is_winner(called_numbers)]
                cards = [card for card in cards if card not in winning_cards]
            else:
                if (cards[0].is_winner(called_numbers)):
                    return cards[0].score(called_numbers)

    def part1(self, input: BingoGame) -> int:
        """ Part 1 solver. """
        return self.score_first_winner(input)

    def part2(self, input: BingoGame) -> int:
        """ Part 2 solver. """
        return self.score_last_winner(input)
