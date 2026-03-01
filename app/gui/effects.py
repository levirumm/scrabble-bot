from PySide6.QtWidgets import QGraphicsDropShadowEffect


def get_drop_shadow() -> QGraphicsDropShadowEffect:
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setXOffset(0)
    shadow.setYOffset(1)
    return shadow