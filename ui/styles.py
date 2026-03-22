from __future__ import annotations

ICON_BUTTON_STYLE = """
    QPushButton {
        font-size: 14px;
        min-width: 34px;
        max-width: 34px;
        min-height: 30px;
        max-height: 30px;
        border: 1px solid palette(mid);
        border-radius: 4px;
        padding: 0px;
    }
    QPushButton:hover {
        background-color: palette(midlight);
        border-color: palette(dark);
    }
    QPushButton:pressed {
        background-color: palette(mid);
    }
    QPushButton:disabled {
        color: palette(midlight);
        border-color: palette(midlight);
    }
"""

ACTION_BUTTON_STYLE = """
    QPushButton {
        padding: 5px 14px;
        border: 1px solid palette(mid);
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: palette(midlight);
        border-color: palette(dark);
    }
    QPushButton:pressed {
        background-color: palette(mid);
    }
    QPushButton:disabled {
        color: palette(midlight);
        border-color: palette(midlight);
    }
"""

TOOLBAR_BUTTON_STYLE = """
    QPushButton {
        padding: 4px 12px;
        border: 1px solid palette(mid);
        border-radius: 4px;
    }
    QPushButton:hover {
        background-color: palette(midlight);
        border-color: palette(dark);
    }
    QPushButton:pressed {
        background-color: palette(mid);
    }
    QPushButton:disabled {
        color: palette(midlight);
        border-color: palette(midlight);
    }
"""

PRIMARY_BUTTON_STYLE = """
    QPushButton {
        padding: 5px 14px;
        border: 1px solid #1a73e8;
        border-radius: 4px;
        background-color: #1a73e8;
        color: white;
    }
    QPushButton:hover {
        background-color: #1557b0;
        border-color: #1557b0;
    }
    QPushButton:pressed {
        background-color: #12479a;
    }
    QPushButton:disabled {
        background-color: palette(midlight);
        border-color: palette(midlight);
        color: palette(mid);
    }
"""

DANGER_BUTTON_STYLE = """
    QPushButton {
        padding: 5px 14px;
        border: 1px solid #d93025;
        border-radius: 4px;
        color: #d93025;
    }
    QPushButton:hover {
        background-color: #fce8e6;
        border-color: #a50e0e;
        color: #a50e0e;
    }
    QPushButton:pressed {
        background-color: #f5c6c2;
    }
    QPushButton:disabled {
        color: palette(midlight);
        border-color: palette(midlight);
    }
"""
