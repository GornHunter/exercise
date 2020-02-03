<%
dim fname,city,surname
fname=Request.Form("name")
fsurname=Request.Form("surname")
city=Request.Form("city")
Response.Write("Dear " & fname & " " & fsurname & ". ")
Response.Write("Hope you live well in " & city & ".")
%>
