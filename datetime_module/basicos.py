from datetime import datetime
import sys

sys.path.insert(1, "..")

from timezone_utils import is_aware

# Fecha actual
fecha = datetime.now()
print(is_aware(fecha))
# hora actual
