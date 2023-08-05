# `from backports.zoneinfo import ZoneInfo` si estás
# en Python <= 3.9 y tienes instalado backports.zoneinfo

from zoneinfo import ZoneInfo


def is_aware(dt_value):
    """Nos dice si la fecha tiene zona horaria asociada"""
    return (
        dt_value.tzinfo is not None and dt_value.tzinfo.utcoffset(dt_value) is not None
    )


def make_aware(dt_value, timezone_name):
    """Agregar la zona horaria a la fecha"""
    if is_aware(dt_value):
        raise ValueError("La fecha ya tiene zona horaria asociada")
    zone_info = ZoneInfo(timezone_name)
    return dt_value.replace(tzinfo=zone_info)


def change_timezone(dt_value, timezone_name):
    """Cambia la zona horaria de la fecha, sin modificar la hora, es decir,
    representa la misma hora en otra zona horaria
    """
    if not is_aware(dt_value):
        raise ValueError("Se necesita una fecha con zona horaria asociada")
    zone_info = ZoneInfo(timezone_name)
    return dt_value.astimezone(zone_info)
