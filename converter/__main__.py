"""This module contains code for GUI of the converter"""
import sys

from PIL import Image
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow

from converter import window
from converter.utils import convert, get_file_name


class ConverterGUI(QMainWindow, window.Ui_MainWindow):
    """
    This is a class for GUI of the pdf converter. It provides window,
    buttons and functions to handle them.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select_file_btn.clicked.connect(self.select_file)
        self.process_doc_btn.clicked.connect(self.process_file)
        self.save_file_btn.clicked.connect(self.save_file)
        self.to_next_btn.clicked.connect(self.to_next_page)
        self.to_prev_btn.clicked.connect(self.to_prev_page)
        self.dpi_box.currentTextChanged.connect(self.on_box_item_change)
        self.color_mode_box.currentTextChanged.connect(self.on_box_item_change)
        self.image_format_box.currentTextChanged.connect(
            self.on_box_item_change)
        self.display_page_label.resizeEvent = self.on_display_page_resize
        self.file_path = None
        self.processed = None
        self.image_format = None
        self.active_page_number = None
        self.color_mode = None

    @property
    def dpi(self):
        """
        :return: current DPI
        :rtype: int
        """
        return int(self.dpi_box.currentText())

    @property
    def color_format(self):
        """
        :return:
            PyQT image color format based on value from color_mode_box
        :rtype: int
        """
        # BGR888 for rgb format
        color_format = QImage.Format_RGB888
        if self.color_mode == 'rgba' and self.image_format == 'png':
            color_format = QImage.Format_RGBA8888
        elif self.color_mode == 'grayscale' or self.color_mode == 'binary':
            color_format = QImage.Format_Grayscale8
        return color_format

    @property
    def pages_count(self):
        """
        :return: Number of document pages
        :rtype: int
        """
        return len(self.processed) if self.processed else None

    def on_display_page_resize(self, event):  # noqa
        """
        Resize image in display_page_label when it is resizing

        :param PyQt5.QtGui.QResizeEvent.QResizeEvent event:
            resize event
        """
        if self.active_page_number:
            self.display_active_page()

    def on_box_item_change(self):
        """Handle changing active items in comboboxes"""
        if not self.process_doc_btn.isEnabled() and self.file_path:
            self.process_doc_btn.setDisabled(False)

    def select_file(self):
        """Set path to pdf file to handle and get its name"""
        file_path = QFileDialog.getOpenFileUrl(caption='Select file')[0].path()
        if file_path.endswith('.pdf'):
            self.select_file_label.setText('File selected')
            self.file_path = file_path
            self._clear_page_label()

            # enable document processing button and boxes and disable
            # save button
            self.dpi_box.setDisabled(False)
            self.color_mode_box.setDisabled(False)
            self.image_format_box.setDisabled(False)
            self.process_doc_btn.setDisabled(False)
            self.save_file_btn.setDisabled(True)

    def _clear_page_label(self):
        """Set pages info label to default state"""
        self.display_page_label.clear()
        self.display_page_label.setStyleSheet("background-color: white;")
        self._update_page_number_info()

    def process_file(self):
        """Convert selected pdf file to images"""
        # TODO: run this function in separate thread
        self.color_mode = self.color_mode_box.currentText().lower()
        self.image_format = self.image_format_box.currentText().lower()
        self.processed = convert(self.file_path, self.dpi, self.image_format,
                                 self.color_mode)

        self.active_page_number = 1
        self.save_file_btn.setDisabled(False)
        if self.active_page_number != self.pages_count:
            self.to_next_btn.setDisabled(False)
        self.process_doc_btn.setDisabled(True)
        self.display_active_page()

    def save_file(self):
        """Save images from pdf file to selected folder"""
        # TODO: run this function in separate thread
        try:
            save_dir = QFileDialog.getExistingDirectoryUrl(
                caption='Select saving directory').toLocalFile()
            for i, page in enumerate(self.processed):
                file_name = get_file_name(self.file_path)
                save_dir = f'{save_dir}/{file_name}_{i}.{self.image_format}'
                Image.fromarray(page).save(save_dir)
        except NotADirectoryError:
            pass

    def display_active_page(self):
        """Draw currently observed image in display_page_label"""
        cur_img = self.processed[self.active_page_number - 1]
        channels = cur_img.shape[2] if len(cur_img.shape) > 2 else 1

        qimg = QImage(
            cur_img, cur_img.shape[1], cur_img.shape[0],
            channels * cur_img.shape[1], self.color_format).smoothScaled(
            self.display_page_label.width(), self.display_page_label.height())
        pixmap = QPixmap(qimg)
        self.display_page_label.setPixmap(pixmap)
        self._update_page_number_info()

    def _update_page_number_info(self):
        """
        Update page numbers label text with currently active page
        number and pages count it it exists. Else, clear label text.
        """
        if self.active_page_number and self.pages_count:
            self.page_numbers_label.setText(
                f'Page {self.active_page_number} of {self.pages_count}')
        else:
            self.page_numbers_label.setText('Page 0 of 0')

    def to_next_page(self):
        """Draw next image from list of images taken from pdf"""
        if self.active_page_number < self.pages_count:
            self.active_page_number += 1
            self.display_active_page()
        if self.active_page_number == self.pages_count:
            self.to_next_btn.setDisabled(True)
        if not self.to_prev_btn.isEnabled():
            self.to_prev_btn.setDisabled(False)

    def to_prev_page(self):
        """Draw previous image from list of images taken from pdf"""
        if self.active_page_number > 1:
            self.active_page_number -= 1
            self.display_active_page()
        if self.active_page_number == 1:
            self.to_prev_btn.setDisabled(True)
        if not self.to_next_btn.isEnabled():
            self.to_next_btn.setDisabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window_ = ConverterGUI()
    window_.show()
    app.exec_()
