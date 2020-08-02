Dim WinScriptHost
Set WinScriptHost = CreateObject("WScript.Shell")
WinScriptHost.Run Chr(34) & "E:\STUDIES\Python\Finished_Projects\Timer\timer1.bat" & Chr(34), 0
Set WinScriptHost = Nothing