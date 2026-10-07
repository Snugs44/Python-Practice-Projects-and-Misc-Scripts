"""Regression checks for the learning projects; standard library only."""

import collections
import contextlib
import importlib
import io
import math
from pathlib import Path
import random
import subprocess
import sys
import unittest
from unittest.mock import patch

from calculators import calories_burned
from exercises.dictionaries.month_lookup import MONTH_CONVERSIONS, get_month_name
from exercises.functions.exponentiation import raise_to_power
from exercises.strings.substring_check import contains
from exercises.strings.username_generator import username_generator
from games import animal_guessing_game, number_guessing_game, quiz_game, rock_paper_scissors
from prototypes import slot_machine

ROOT = Path(__file__).resolve().parents[1]


def run_main(module, inputs):
    """Capture one interactive session without requiring a terminal."""
    output = io.StringIO()
    with patch("builtins.input", side_effect=inputs) as reader, contextlib.redirect_stdout(output):
        module.main()
    return output.getvalue(), reader.call_count


class RockPaperScissorsTests(unittest.TestCase):
    def test_all_nine_matchups(self):
        expected = {
            ("rock", "rock"): "tie", ("rock", "paper"): "loss", ("rock", "scissors"): "win",
            ("paper", "rock"): "win", ("paper", "paper"): "tie", ("paper", "scissors"): "loss",
            ("scissors", "rock"): "loss", ("scissors", "paper"): "win", ("scissors", "scissors"): "tie",
        }
        for choices, outcome in expected.items():
            with self.subTest(choices=choices):
                self.assertEqual(rock_paper_scissors.determine_winner(*choices), outcome)

    def test_normalizes_case_and_whitespace(self):
        self.assertEqual(rock_paper_scissors.determine_winner(" ROCK ", " Scissors "), "win")

    def test_rejects_invalid_choices(self):
        for choices in [("lizard", "rock"), ("rock", "spock"), ("", "paper")]:
            with self.subTest(choices=choices), self.assertRaises(ValueError):
                rock_paper_scissors.determine_winner(*choices)

    def test_session_counts_wins_losses_ties_and_ignores_invalid_input(self):
        with patch.object(rock_paper_scissors.random, "choice", side_effect=["scissors", "rock", "paper"]) as chooser:
            output, _ = run_main(rock_paper_scissors, ["bad", "ROCK", "rock", "rock", "q"])
        self.assertEqual(chooser.call_count, 3)
        self.assertIn("Wins: 1 | Losses: 1 | Ties: 1", output)

    def test_eof_and_interrupt_print_summary(self):
        for error in [EOFError(), KeyboardInterrupt()]:
            with self.subTest(error=type(error).__name__):
                output, _ = run_main(rock_paper_scissors, [error])
                self.assertIn("Wins: 0 | Losses: 0 | Ties: 0", output)


class NumberGuessingTests(unittest.TestCase):
    def test_equal_bounds_include_zero_and_one_hundred(self):
        self.assertEqual(number_guessing_game.choose_number(0, 0), 0)
        self.assertEqual(number_guessing_game.choose_number(100, 100), 100)

    def test_invalid_ranges_are_rejected(self):
        for bounds in [(10, 1), (-1, 5), (0, 101), (1.5, 3), (False, 3)]:
            with self.subTest(bounds=bounds), self.assertRaises(ValueError):
                number_guessing_game.choose_number(*bounds)

    def test_read_int_retries_invalid_values(self):
        with patch("builtins.input", side_effect=["word", "1.5", "-1", "11", " 5 "]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(number_guessing_game.read_int("Number: ", 0, 10), 5)

    def test_read_int_rejects_inverted_bounds_before_prompting(self):
        with patch("builtins.input") as reader, self.assertRaises(ValueError):
            number_guessing_game.read_int("Number: ", 5, 1)
        reader.assert_not_called()

    def test_declining_stops_before_range_prompts(self):
        output, count = run_main(number_guessing_game, ["NO"])
        self.assertEqual(count, 1)
        self.assertIn("goodbye", output)

    def test_session_retries_inverted_minimum_and_invalid_guesses(self):
        with patch.object(number_guessing_game.random, "randint", return_value=5):
            output, _ = run_main(number_guessing_game, ["Y", "10", "11", "0", "bad", "-1", "3", "7", "5"])
        self.assertIn("higher", output)
        self.assertIn("lower", output)
        self.assertIn("3 guess(es)", output)


class AnimalGuessingTests(unittest.TestCase):
    def test_case_insensitive_answer(self):
        output, count = run_main(animal_guessing_game, ["  MONKEY  "])
        self.assertEqual(count, 1)
        self.assertIn("You got it!", output)

    def test_stops_after_five_wrong_answers(self):
        output, count = run_main(animal_guessing_game, ["cat"] * 5)
        self.assertEqual(count, 5)
        self.assertIn("Out of guesses", output)

    def test_final_guess_can_win(self):
        output, count = run_main(animal_guessing_game, ["cat"] * 4 + ["monkey"])
        self.assertEqual(count, 5)
        self.assertIn("You got it!", output)
        self.assertNotIn("Out of guesses", output)

    def test_quit(self):
        output, count = run_main(animal_guessing_game, ["q"])
        self.assertEqual(count, 1)
        self.assertIn("Goodbye", output)


class QuizTests(unittest.TestCase):
    def test_answer_normalization(self):
        self.assertTrue(quiz_game.is_correct_answer(" RANDOM   access Memory ", "random access memory"))
        self.assertFalse(quiz_game.is_correct_answer("yes", "no"))

    def test_declining_does_not_ask_questions(self):
        output, count = run_main(quiz_game, ["no"])
        self.assertEqual(count, 1)
        self.assertNotIn("Score:", output)

    def test_perfect_score(self):
        answers = [answer.upper() for _, answer in quiz_game.QUESTIONS]
        output, _ = run_main(quiz_game, ["yes"] + answers)
        self.assertIn("Score: 4/4 (100%)", output)

    def test_zero_score(self):
        output, _ = run_main(quiz_game, ["yes"] + ["wrong"] * 4)
        self.assertIn("Score: 0/4 (0%)", output)

    def test_partial_score(self):
        output, _ = run_main(quiz_game, ["yes", "random access memory", "wrong", "no", "wrong"])
        self.assertIn("Score: 2/4 (50%)", output)


class ExerciseTests(unittest.TestCase):
    def test_all_months(self):
        self.assertEqual(len(MONTH_CONVERSIONS), 12)
        for key, value in MONTH_CONVERSIONS.items():
            with self.subTest(month=key):
                self.assertEqual(get_month_name(f" {key.upper()} "), value)

    def test_unknown_months(self):
        for value in ["", "NotAMonth", "January"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                get_month_name(value)

    def test_exponentiation_values(self):
        for base, power, expected in [(5, 3, 125), (9, 0, 1), (0, 3, 0), (-2, 3, -8), (2.5, 2, 6.25)]:
            with self.subTest(base=base, power=power):
                self.assertEqual(raise_to_power(base, power), expected)

    def test_exponentiation_returns_without_printing(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = raise_to_power(5, 3)
        self.assertEqual(result, 125)
        self.assertEqual(output.getvalue(), "")

    def test_invalid_exponents(self):
        for value in [-1, 1.5, True, "3"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                raise_to_power(5, value)

    def test_username_slices_and_original_short_name_rule(self):
        self.assertEqual(username_generator(" Abe ", " Simpson "), "AbeSimp")
        self.assertEqual(username_generator("Al", "Simpson"), "AlSimpson")
        self.assertEqual(username_generator("Abraham", "Li"), "AbrahamLi")

    def test_blank_names_are_rejected(self):
        for first, last in [("", "Smith"), ("Abe", "   ")]:
            with self.subTest(first=first, last=last), self.assertRaises(ValueError):
                username_generator(first, last)

    def test_substring_membership(self):
        self.assertTrue(contains("watermelon", "melon"))
        self.assertFalse(contains("watermelon", "Melon"))
        self.assertFalse(contains("watermelon", "pear"))
        self.assertTrue(contains("watermelon", ""))
        self.assertTrue(contains("", ""))


class CalculatorTests(unittest.TestCase):
    def test_original_arithmetic_is_preserved(self):
        expected = 30 * 0.2757 + 180 * 0.03295 + (120 * 1.0781 - 75.4991) * (20 / 8.368)
        self.assertAlmostEqual(calories_burned.calculate_calories(30, 180, 120, 20), expected)

    def test_nonpositive_and_nonfinite_inputs(self):
        for position in range(4):
            for bad in [0, -1, math.nan, math.inf, -math.inf]:
                values = [30, 180, 120, 20]
                values[position] = bad
                with self.subTest(position=position, bad=bad), self.assertRaises(ValueError):
                    calories_burned.calculate_calories(*values)

    def test_overflow_is_rejected(self):
        with self.assertRaises(ValueError):
            calories_burned.calculate_calories(30, 180, 1e308, 1e308)

    def test_positive_float_reader_retries_bad_input(self):
        with patch("builtins.input", side_effect=["bad", "0", "-1", "nan", "inf", "12.5"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(calories_burned.read_positive_float("Value: "), 12.5)


class SlotPrototypeTests(unittest.TestCase):
    def test_shape_and_symbol_counts(self):
        rng = random.Random(42)
        with patch.object(slot_machine.random, "sample", side_effect=rng.sample):
            columns = slot_machine.get_slot_machine_spin(3, 4, {"A": 1, "B": 2})
        self.assertEqual(len(columns), 4)
        for column in columns:
            self.assertEqual(len(column), 3)
            self.assertEqual(collections.Counter(column), {"A": 1, "B": 2})
        self.assertIsNot(columns[0], columns[1])

    def test_partial_sampling_respects_multiplicities(self):
        rng = random.Random(42)
        with patch.object(slot_machine.random, "sample", side_effect=rng.sample):
            for _ in range(50):
                for column in slot_machine.get_slot_machine_spin(3, 3, slot_machine.SYMBOL_COUNTS):
                    counts = collections.Counter(column)
                    self.assertLessEqual(counts["A"], 2)
                    self.assertTrue(set(column).issubset(slot_machine.SYMBOL_COUNTS))

    def test_invalid_dimensions_and_counts(self):
        cases = [(0, 3, {"A": 1}), (3, -1, {"A": 3}), (1.5, 3, {"A": 3}),
                 (True, 3, {"A": 3}), (1, 1, {}), (1, 1, {"A": 0}),
                 (1, 1, {"A": -1}), (1, 1, {"A": 1.5}), (1, 1, {"A": True}),
                 (4, 3, {"A": 3})]
        for args in cases:
            with self.subTest(args=args), self.assertRaises(ValueError):
                slot_machine.get_slot_machine_spin(*args)

    def test_amount_reader_retries_invalid_values(self):
        with patch("builtins.input", side_effect=["oops", "1.5", "0", "101", "5"]), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(slot_machine.read_amount("Amount: ", 1, 100), 5)

    def test_amount_reader_rejects_impossible_bounds(self):
        with self.assertRaises(ValueError):
            slot_machine.read_amount("Amount: ", 2, 1)

    def test_one_credit_balance_cannot_get_stuck(self):
        output, _ = run_main(slot_machine, ["1", "3", "1", "2", "1"])
        self.assertIn("1 credits total", output)
        self.assertIn("Preview only", output)
        self.assertEqual(output.count(" | "), 6)

    def test_bet_cannot_exceed_balance(self):
        output, _ = run_main(slot_machine, ["5", "3", "2", "1"])
        self.assertIn("3 credits total", output)


class IntegrationTests(unittest.TestCase):
    def test_imports_are_silent_and_do_not_prompt(self):
        modules = ["games.animal_guessing_game", "games.number_guessing_game", "games.quiz_game",
                   "games.rock_paper_scissors", "calculators.calories_burned", "prototypes.slot_machine",
                   "exercises.dictionaries.month_lookup", "exercises.functions.exponentiation",
                   "exercises.strings.username_generator", "exercises.strings.substring_check"]
        output = io.StringIO()
        with patch("builtins.input", side_effect=AssertionError("Import prompted for input")), contextlib.redirect_stdout(output):
            for name in modules:
                importlib.reload(importlib.import_module(name))
        self.assertEqual(output.getvalue(), "")

    def test_all_ten_scripts_run_directly(self):
        cases = {
            "games/rock_paper_scissors.py": ("q\n", "Wins: 0"),
            "games/number_guessing_game.py": ("yes\n0\n0\n0\n", "You nailed it"),
            "games/animal_guessing_game.py": ("MONKEY\n", "You got it"),
            "games/quiz_game.py": ("yes\nrandom access memory\ngraphics processing unit\nno\ncentral processing unit\n", "Score: 4/4"),
            "calculators/calories_burned.py": ("30\n180\n120\n20\n", "unvalidated"),
            "prototypes/slot_machine.py": ("10\n3\n2\n", "Preview only"),
            "exercises/dictionaries/month_lookup.py": ("", "June"),
            "exercises/functions/exponentiation.py": ("", "125"),
            "exercises/strings/username_generator.py": ("", "AbeSimp"),
            "exercises/strings/substring_check.py": ("", "True"),
        }
        for path, (inputs, expected) in cases.items():
            with self.subTest(path=path):
                result = subprocess.run([sys.executable, str(ROOT / path)], input=inputs, text=True,
                                        capture_output=True, cwd=ROOT, timeout=5)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertIn(expected, result.stdout)
                self.assertEqual(result.stderr, "")

    def test_interactive_scripts_exit_cleanly_on_eof(self):
        paths = ["games/rock_paper_scissors.py", "games/number_guessing_game.py",
                 "games/animal_guessing_game.py", "games/quiz_game.py",
                 "calculators/calories_burned.py", "prototypes/slot_machine.py"]
        for path in paths:
            with self.subTest(path=path):
                result = subprocess.run([sys.executable, str(ROOT / path)], input="", text=True,
                                        capture_output=True, cwd=ROOT, timeout=5)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
