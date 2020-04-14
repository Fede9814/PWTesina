@echo Starting Influxd.exe
START /min D:\DesktopDocs\Script\Influx\idb\influxd.exe
TIMEOUT 3
cls
@echo Starting Influx.exe
START /min D:\DesktopDocs\Script\Influx\idb\influx.exe
TIMEOUT 1
cls
@echo Starting Chronograf.exe
START /min D:\DesktopDocs\Script\Influx\chr\chronograf.exe
TIMEOUT 3
cls
@echo opening InfluxUI
START "" http://localhost:8888/sources/1/status
TIMEOUT 1