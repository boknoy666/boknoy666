Dim message, sapi
message=InputBox("created by jules")
set sapi=CreateObject("sapi.spvoice")
sapi.Speak message