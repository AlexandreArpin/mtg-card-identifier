import os
import cv2
import numpy as np

BASE_DIR = os.path.dirname(__file__)
LATEST_DIR = os.path.join(BASE_DIR, "static/latest")


def find_card_file(image_path):
    return find_card_image(cv2.imread(image_path))


def find_card_image(image):
    cv2.imwrite(os.path.join(LATEST_DIR, "latest_raw.jpg"), image)

    img = _get_magic_card_crop(image)

    cv2.imwrite(os.path.join(LATEST_DIR, "latest_crop.jpg"), img)

    return img


def _auto_canny_otsu(image):
    otsu_thresh_val = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    high_thresh_val = otsu_thresh_val[0]
    lower_thresh_val = otsu_thresh_val[0] * 0.5

    edged = cv2.Canny(image, lower_thresh_val, high_thresh_val)

    cv2.imwrite(os.path.join(LATEST_DIR, "steps_thres.jpg"), otsu_thresh_val[1])
    cv2.imwrite(os.path.join(LATEST_DIR, "steps_edged.jpg"), edged)

    return edged


def _get_magic_card_contour(mat):
    bw = cv2.cvtColor(mat, cv2.COLOR_BGR2GRAY)
    edged = _auto_canny_otsu(bw)

    img, contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

    return contours


def _get_magic_card_crop(original_image):
    scale_mult = 0.15
    mat = cv2.resize(original_image, (0, 0), fx=scale_mult, fy=scale_mult)
    contour = _get_magic_card_contour(mat)

    # Obtain shape approximation
    card = contour[0]
    peri = cv2.arcLength(card, True)
    approx = cv2.approxPolyDP(card, 0.02 * peri, True)

    x, y, w, h = cv2.boundingRect(card)
    w /= scale_mult
    h /= scale_mult

    w = int(w)
    h = int(h)

    # Test to see if our approximation is a quadrilateral
    if len(approx) != 4:
        rect = rectify(cv2.boxPoints(cv2.minAreaRect(card)))
    else:
        # Great! We can safely apply our perspective correction technique
        rect = rectify(approx)

    for i in range(4):
        # Compute all 4 corners on original image (re-apply scaling)
        rect[i][0] /= scale_mult
        rect[i][1] /= scale_mult
        
    cv2.imwrite(os.path.join(LATEST_DIR, "steps_contours_bon.jpg"), original_image)

    # Output perspective correction to an image of about the same size
    output = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)
    transform = cv2.getPerspectiveTransform(rect, output)
    return cv2.warpPerspective(original_image, transform, (w, h))


def rectify(h):
    """
    Utility code from http://git.io/vGi60A
    Thanks to author of the sudoku example for the wonderful blog posts!
    """

    h = h.reshape((4, 2))
    hnew = np.zeros((4, 2), dtype=np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis=1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew
