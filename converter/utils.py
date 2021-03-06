"""This module contains utility functions for pdf converter"""
from os.path import basename, splitext

from numpy import array
from pdf2image import convert_from_path


def convert(file, dpi=300, image_format='jpg', color_mode='rgb'):
    """
    Convert pdf file to selected format

    :param str file:
        Path to PDF file that need to be converted
    :param int dpi:
        DPI of converter
    :param str image_format:
        format of output file. Possible formats: ['jpg', 'png']
    :param str color_mode:
        Color mode of output images
        Possible modes: ['rgb', 'rgba', 'grayscale', 'binary']
    :return: list of converted pages
    :rtype: list of numpy.ndarray
    """
    transparent = color_mode == 'rgba'
    grayscale = color_mode == 'grayscale'

    # Convert document to list of Pillow images
    converted = convert_from_path(file, dpi, fmt=image_format,
                                  transparent=transparent,
                                  grayscale=grayscale)
    # Convert colors from RGB(A) to BGR(A)
    if color_mode == 'rgb':
        converted = [im.convert('RGB') for im in converted]
    elif color_mode == 'rgba':
        if image_format == 'png':
            converted = [im.convert('RGBA') for im in converted]
        else:
            converted = [im.convert('RGB') for im in converted]
    elif color_mode == 'binary':
        converted = [im.convert('1') for im in converted]
    else:
        # Convert to grayscale
        converted = [im.convert('L') for im in converted]

    converted = [array(im) for im in converted]
    return converted


def get_file_name(file_path):
    """
    :param str file_path: Path to file
    :return: Name of file without extension
    :rtype: str
    """
    return splitext(basename(file_path))[0]
