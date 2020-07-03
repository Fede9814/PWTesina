@echo off
for /f "delims=" %%a in ('wmic OS Get localdatetime ^| find "."') do set DateTime=%%a
set Yr=%DateTime:~0,4%
set Mon=%DateTime:~4,2%
set Day=%DateTime:~6,2%
set Hr=%DateTime:~8,2%
set Min=%DateTime:~10,2%
set Sec=%DateTime:~12,2%

@echo Starting backup...
@echo.
mkdir Backup_%Yr%-%Mon%-%Day%_(%Hr%-%Min%-%Sec%) | influxd backup -database test D:\DesktopDocs\Script\Influx\idb\Backup_%Yr%-%Mon%-%Day%_(%Hr%-%Min%-%Sec%)
@echo.
@echo Backup completed!
TIMEOUT 3