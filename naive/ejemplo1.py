from datetime import datetime
from zoneinfo import ZoneInfo

utc_now = datetime.now(ZoneInfo("UTC"))
local_now = datetime.now(tz=ZoneInfo("America/Mexico_City"))
loacal_as_UTC = local_now.astimezone(ZoneInfo("UTC"))

print("LOCAL:", local_now)
print("UTC:", utc_now)
# print("¿Vamos adelantados a UTC?", local_now.time() > utc_now.time())
