import win32com.client as client

wsh = client.Dispatch('WScript.Shell')
wsh.AppActivate("RustClient.exe")
wsh.SendKeys('1')
