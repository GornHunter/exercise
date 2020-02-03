<%
dim fname,city
fname=Request.Form("name")
fsurname=Request.Form("surname")
city=Request.Form("city")
Response.Write("Dear " & fname & surname &". ")
Response.Write("Hope you live well in " & city & ".")
%>
