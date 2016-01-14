import json
import os
import re
from Levenshtein import distance

DIGITS_ONLY_RE = "[^0-9]"
BASE_DIR = os.path.dirname(__file__)
EDITIONS_DIR = os.path.join(BASE_DIR, "sets")
SUPPORTED_EDITIONS = (
    "bfz",
    "dtk",
    "frf",
    "m15",
    "ori",
    "ktk",
)


def match_card(name=None, number=None, edition=None):
    # Validate parameters
    if edition and edition.lower() not in SUPPORTED_EDITIONS:
        edition = None

    # No parameters specified
    if number is None and name is None:
        return None

    if number is not None:
        number = int(number)

    result = None

    # First Attempt an exact match
    if edition:
        result = _exact_match_card_in_set(name, number, edition)
    else:
        # If no edition was specified, iterate through the editions
        for supported_edition in SUPPORTED_EDITIONS:
            result = _exact_match_card_in_set(name, number, supported_edition)

            if result is not None:
                break

    # If we have a match, return it
    if result:
        return result

    # Collect candidates for inexact match
    if edition:
        score, result = _inexact_match_card_in_set(name, number, edition)
    else:
        best_score = 99999
        best_result = None

        # If no edition was specified, iterate through the editions
        for supported_edition in SUPPORTED_EDITIONS:
            score, result = _inexact_match_card_in_set(name, number, supported_edition)

            if score < best_score:
                best_score = score
                best_result = result

        result = best_result

    return result


def _exact_match_card_in_set(name, number, edition):
    edition_json = _get_edition_json(edition)

    # First, let's try a perfect match
    for card in edition_json["cards"]:
        card_match = name is None or card["name"] == name
        number_match = number is None or int(re.sub(DIGITS_ONLY_RE, "", card["number"])) == number

        if card_match and number_match:
            return card

    return None


def _inexact_match_card_in_set(name, number, edition):
    edition_json = _get_edition_json(edition)

    # Well that didn't work - let's evaluate some potential candidates
    best_score = 99999
    best_candidates = []

    for card in edition_json["cards"]:
        calc_distance = distance(name, card["name"])

        if calc_distance < best_score:
            best_score = calc_distance
            best_candidates = [card]
        elif calc_distance == best_score:
            best_candidates += card

    return best_score, best_candidates[0]


def _get_edition_json(edition):
     # Parse edition file
    edition_path = os.path.join(EDITIONS_DIR, edition.upper() + ".json")

    with open(edition_path) as edition_file:
        edition = json.load(edition_file)

    return edition