package some.project.xdx.servlets;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletResponse;

import java.io.IOException;

@WebFilter("/fib")
public class FibFilter implements Filter {
    @Override
    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain)
            throws IOException, ServletException {
        if (req.getParameter("limit") == null || req.getParameter("limit").isEmpty()) {
            ((HttpServletResponse) resp).setStatus(400);
            return;
        }
        chain.doFilter(req, resp);
    }
}
