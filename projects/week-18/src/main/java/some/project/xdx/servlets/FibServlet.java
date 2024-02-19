package some.project.xdx.servlets;

import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.BigInteger;

@WebServlet("/fib")
public class FibServlet extends HttpServlet {
    static BigInteger fib(int n) {
        BigInteger a = BigInteger.ZERO;
        BigInteger b = BigInteger.ONE;
        for (int i = 0; i < n; i++) {
            BigInteger c = a.add(b);
            a = b;
            b = c;
        }
        return a;
    }

    @Override
    protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {
        var limit = Integer.parseInt(req.getParameter("limit"));
        var writer = resp.getWriter();
        for (int i = 0; i < limit; i++)
            writer.println(fib(i));
    }
}
