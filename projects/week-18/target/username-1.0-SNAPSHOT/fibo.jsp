<%@ page import="some.project.xdx.servlets.FibServlet" %>
<%@ page contentType="text/html;charset=UTF-8" %>
<%
  request.setAttribute("limit", "10");
  if (request.getParameterMap().containsKey("limit")) {
    request.setAttribute("limit", request.getParameter("limit"));
  }
%>

<h1>Nice Page showing some fib numbers</h1>
<jsp:include page="/fib">
  <jsp:param name="limit" value="<%=request.getAttribute(\"limit\") %>" />
</jsp:include>

<p>If you want to generate more numbers, see this:</p>
<form action="fibo.jsp" method="get">
  <input type="number" name="limit" />
  <input type="submit" value="Generate" />
</form>
