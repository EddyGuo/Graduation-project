@echo off
echo 以下操作会删除数据库数据！！！
echo 是否继续，回车以继续
pause>nul
echo.
set MYSQL_HOME=%~dp0
cd %MYSQL_HOME%
net stop mysql 1> nul 2> nul && echo MySQL停止服务成功！ || echo MySQL未启动！
sc delete mysql 1> nul 2> nul && echo MySQL成功删除！ || echo MySQL未安装！
taskkill /F /IM mysqld.exe 2> nul
del /F my.ini 1> nul 2> nul && echo MySQL配置文件成功删除！ || echo  MySQL配置文件不存在!
rd /s /q data 1> nul 2> nul && echo MySQL data删除成功！ || echo MySQL data不存在！
