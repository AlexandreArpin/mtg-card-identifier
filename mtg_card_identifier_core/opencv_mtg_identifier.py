import json
import os
import cv2
import re

from mtg_card_identifier_core import pytesser
from mtg_card_identifier_core.mtg_card_matcher import match_card
from mtg_card_identifier_core.opencv_card_finder import find_card_image

CARD_NUMBER_RE = "[0-9][0-9][0-9]/[0-9][0-9][0-9]"
EDITION_RE = "^[A-Za-z ][A-Za-z ][A-Za-z ] "

MINIMUM_WIDTH = 312
MINIMUM_HEIGHT = 446

DEBUG = True

BASE_DIR = os.path.dirname(__file__)
LATEST_DIR = os.path.join(BASE_DIR, "static/latest")


def identify_file(image_path, find_card=False):
    return identify_image(cv2.imread(image_path), find_card)


def identify_image(image, find_card=False):
    if find_card:
        image = find_card_image(image)

    color_dict = get_card_color(image)

    # Resize images that are too small for good OCR
    image_height, image_width = _get_image_size(image)
    if image_height < MINIMUM_HEIGHT or image_width < MINIMUM_WIDTH:
        scale_x = max(MINIMUM_WIDTH / image_width, 1)
        scale_y = max(MINIMUM_HEIGHT / image_height, 1)
        image = cv2.resize(image, (0, 0), fx=scale_x, fy=scale_y, interpolation=cv2.INTER_LANCZOS4)

    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    card_name = get_card_name(grayscale_image).strip()
    card_text = get_card_text(grayscale_image).strip()
    card_type = get_card_type(grayscale_image).strip()
    number, edition = get_card_number_and_edition(grayscale_image)

    debug = {
        "card_name": card_name,
        "number": number,
        "edition": edition,
        "color": color_dict,
        "text": card_text,
        "type": card_type,
    }

    with open(os.path.join(LATEST_DIR, "latest_debug.json"), 'w') as outfile:
        json.dump(debug, outfile)

    if DEBUG:
        print(debug)

    return match_card(card_name, number, edition)


def get_card_color(image):
    image_height, image_width = image.shape[:2]

    color_dict = {
        "white": 0,
        "blue": 0,
        "black": 0,
        "red": 0,
        "green": 0,
    }

    for y in range(0, image_height):
        for x in range(0, image_width):

            pixel = image[y, x]
            p_red = int(pixel[2])
            p_green = int(pixel[1])
            p_blue = int(pixel[0])

            if p_red > 222 and p_green > 222 and p_blue > 222:
                color_dict["white"] += 1
            elif p_red < 33 and p_green < 33 and p_blue < 33:
                color_dict["black"] += 1
            elif p_red > p_green + p_blue:
                color_dict["red"] += 1
            elif p_green > p_blue + p_red:
                color_dict["green"] += 1
            elif p_blue > p_green + p_red:
                color_dict["blue"] += 1

    # Transform Dict to % based
    color_sum = sum(color_dict.values())
    for key in color_dict:
        color_dict[key] = color_dict[key] / color_sum

    return color_dict


def get_card_name(image):
    image_height, image_width = image.shape[:2]
    left, top, width, height = _get_card_name_bounds(image_width, image_height)

    card_name_image_section = image[top:top + height, left:left + width]

    cv2.imwrite(os.path.join(LATEST_DIR, "latest_name.jpg"), card_name_image_section)

    return pytesser.mat_to_string(card_name_image_section, "mtg", psm=pytesser.PSM_SINGLE_LINE)


def get_card_type(image):
    image_height, image_width = image.shape[:2]
    left, top, width, height = _get_card_type_bounds(image_width, image_height)

    card_type_image_section = image[top:top + height, left:left + width]

    #if DEBUG:
    #    cv2.imshow("Type", card_type_image_section)
    #    cv2.waitKey(500)

    cv2.imwrite(os.path.join(LATEST_DIR, "latest_type.jpg"), card_type_image_section)

    return pytesser.mat_to_string(card_type_image_section, "eng", psm=pytesser.PSM_SINGLE_LINE)


def get_card_text(image):
    image_height, image_width = image.shape[:2]
    left, top, width, height = _get_card_text_bounds(image_width, image_height)

    card_text_image_section = image[top:top + height, left:left + width]

    #if DEBUG:
    #    cv2.imshow("Text", card_text_image_section)
    #    cv2.waitKey(500)

    cv2.imwrite(os.path.join(LATEST_DIR, "latest_text.jpg"), card_text_image_section)

    return pytesser.mat_to_string(card_text_image_section, "eng")


def get_card_number_and_edition(image):
    image_height, image_width = image.shape[:2]
    left, top, width, height = _get_number_and_edition_bounds(image_width, image_height)

    number_and_edition_image_section = image[top:top + height, left:left + width]

    cv2.imwrite(os.path.join(LATEST_DIR, "latest_number.jpg"), number_and_edition_image_section)

    # if DEBUG:
    # cv2.imshow("Image", number_and_edition_image_section)
    # cv2.waitKey(500)

    text = pytesser.mat_to_string(number_and_edition_image_section)

    card_number = re.search(CARD_NUMBER_RE, text)
    edition = re.search(EDITION_RE, text, re.MULTILINE)

    if card_number:
        card_number = card_number.group(0)[:3]

    if edition:
        edition = edition.group(0)[:3]

    return card_number, edition


def _get_image_size(image):
    """
    :return: Image Height, Image Width
    """
    return image.shape[:2]


def _get_card_name_bounds(width, height):
    top = int(0.030 * height)
    box_height = int(0.08 * height)

    left = int(0.05 * width)
    box_width = int(0.7 * width)

    return left, top, box_width, box_height


def _get_card_type_bounds(width, height):
    top = int(0.54 * height)
    box_height = int(0.11 * height)

    left = int(0.05 * width)
    box_width = int(0.7 * width)

    return left, top, box_width, box_height


def _get_card_text_bounds(width, height):
    top = int(0.65 * height)
    box_height = int(0.285 * height)

    left = int(0.025 * width)
    box_width = int(0.95 * width)

    return left, top, box_width, box_height


def _get_number_and_edition_bounds(width, height):
    top = int(0.9 * height)
    box_height = int(0.1 * height)

    left = 0
    box_width = int(0.4 * width)

    return left, top, box_width, box_height
