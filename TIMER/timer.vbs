Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "E:\PROJECTS\5.My_projects\FINISHED_PYTHON_PROJECTS\TIMER\timer.bat" & Chr(34), 0
Set WinScriptHost = Nothing