# `from backports.zoneinfo import ZoneInfo` if you
# are on Python <= 3.9 and have installed backports.zoneinfo

from zoneinfo import ZoneInfo


# Timezone aware
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
    """
    Cambia la zona horaria de la fecha
    """
    if not is_aware(dt_value):
        raise ValueError("Se necesita una fecha con zona horaria asociada")
    zone_info = ZoneInfo(timezone_name)
    return dt_value.astimezone(zone_info)
