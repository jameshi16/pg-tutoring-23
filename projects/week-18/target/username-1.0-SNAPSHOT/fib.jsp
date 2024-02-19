<%= page import="some.project.xdx.servlets.FibServlet" %>
<%@ page contentType="text/html;charset=UTF-8" %>

<h1>Nice Page showing some fib numbers</h1>
<jsp:include page="/fib">
  <jsp:param>
    <jsp:param-name>fib</jsp:param-name>
    <jsp:param-value>10</jsp:param-value>
  </jsp:param>
</jsp:include>
