from __future__ import annotations
from PySide6.QtCore import QObject, QEvent, QTimer
from PySide6.QtWidgets import QTreeWidget, QHeaderView
from PySide6.QtGui import QFontMetrics


class ProportionalColumnSizer(QObject):

    def __init__(self, tree: QTreeWidget) -> None:
        super().__init__(tree)
        self._tree = tree
        self._ideal_widths: list[int] = []
        self._min_widths: list[int] = []
        self._proportions: list[float] = []

        header = tree.header()
        header.setStretchLastSection(False)
        for i in range(header.count()):
            header.setSectionResizeMode(i, QHeaderView.Interactive)

        tree.viewport().installEventFilter(self)

    def recalculate(self) -> None:
        header = self._tree.header()
        col_count = header.count()
        if col_count == 0:
            return

        fm = QFontMetrics(header.font())
        self._min_widths = []
        self._ideal_widths = []

        for i in range(col_count):
            header_text = self._tree.headerItem().text(i)
            sort_indicator_padding = 30
            header_width = fm.horizontalAdvance(header_text) + sort_indicator_padding
            self._min_widths.append(header_width)

        for i in range(col_count):
            self._tree.resizeColumnToContents(i)

        for i in range(col_count):
            content_width = header.sectionSize(i)
            self._ideal_widths.append(max(content_width, self._min_widths[i]))

        total_ideal = sum(self._ideal_widths)
        if total_ideal > 0:
            self._proportions = [w / total_ideal for w in self._ideal_widths]
        else:
            self._proportions = [1.0 / col_count] * col_count

        QTimer.singleShot(0, self._apply_widths)

    def _apply_widths(self) -> None:
        header = self._tree.header()
        col_count = header.count()
        if col_count == 0 or not self._proportions:
            return

        available = self._tree.viewport().width()
        if available <= 0:
            return

        total_min = sum(self._min_widths)

        if available <= total_min:
            for i in range(col_count):
                header.resizeSection(i, self._min_widths[i])
            return

        widths = []
        for i in range(col_count):
            w = max(int(available * self._proportions[i]), self._min_widths[i])
            widths.append(w)

        assigned = sum(widths)
        diff = available - assigned
        if diff != 0:
            largest = max(range(col_count), key=lambda i: widths[i])
            widths[largest] += diff

        for i in range(col_count):
            header.resizeSection(i, widths[i])

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if obj is self._tree.viewport() and event.type() == QEvent.Resize:
            if self._proportions:
                self._apply_widths()
        return False
