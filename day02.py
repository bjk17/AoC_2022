from __future__ import annotations

from enum import Enum


class DuelOutcome(Enum):
    Win = 6
    Draw = 3
    Loose = 0

    @classmethod
    def from_symbol(cls, symbol: str) -> DuelOutcome:
        if symbol == 'X':
            return cls.Loose
        if symbol == 'Y':
            return cls.Draw
        if symbol == 'Z':
            return cls.Win

        raise ValueError(f"symbol '{symbol}' doesn't translate to an Outcome")


class Actions(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

    @classmethod
    def from_symbol(cls, symbol: str) -> Actions:
        if symbol in ('A', 'X'):
            return cls.Rock
        if symbol in ('B', 'Y'):
            return cls.Paper
        if symbol in ('C', 'Z'):
            return cls.Scissors

        raise ValueError(f"symbol '{symbol}' doesn't translate to an Action")

    @classmethod
    def beats(cls, hero: Actions, opponent: Actions) -> bool:
        return (hero, opponent) in (
            (Actions.Rock, Actions.Scissors),
            (Actions.Scissors, Actions.Paper),
            (Actions.Paper, Actions.Rock),
        )

    @classmethod
    def outcome(cls, hero: Actions, opponent: Actions) -> DuelOutcome:
        if cls.beats(hero, opponent):
            return DuelOutcome.Win
        elif cls.beats(opponent, hero):
            return DuelOutcome.Loose
        else:
            return DuelOutcome.Draw

    @classmethod
    def pick_action_to_reach_outcome(cls, outcome: DuelOutcome, opponent: Actions) -> Actions:
        if cls.outcome(cls.Rock, opponent) == outcome:
            return cls.Rock
        elif cls.outcome(cls.Paper, opponent) == outcome:
            return cls.Paper
        else:
            return cls.Scissors


def main():
    input_data = open("input/day02.txt").read().split('\n')

    part_1_score, part_2_score = 0, 0
    for line in input_data:
        opponent_symbol, my_symbol = line.split()
        opponent_action = Actions.from_symbol(opponent_symbol)

        my_decoded_action = Actions.from_symbol(my_symbol)
        outcome = Actions.outcome(my_decoded_action, opponent_action)
        part_1_score += my_decoded_action.value
        part_1_score += outcome.value

        desired_outcome = DuelOutcome.from_symbol(my_symbol)
        my_action_to_reach_desired_outcome = Actions.pick_action_to_reach_outcome(desired_outcome, opponent_action)
        part_2_score += my_action_to_reach_desired_outcome.value
        part_2_score += desired_outcome.value

    print(f"Part One: {part_1_score}")
    print(f"Part Two: {part_2_score}")


if __name__ == '__main__':
    main()
