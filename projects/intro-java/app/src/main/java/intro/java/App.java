package intro.java;

public class App {
    public static void m_1() {
        MinimalClass mc = new MinimalClass();
        mc.doSomething();

        mc = new MinimalClass("something", 123);
        mc.doSomething();
    }

    public static void m_2() {
        int a = 100;
        int b = 100;

        System.out.println(a == b);
    }

    public static void m_3() {
        String a = "hello";
        String b = "hello";

        // What does this print?
        System.out.println(a == b);
    }

    public static void m_4() {
        String a = new String("hello");
        String b = new String("hello");

        // What does this print?
        System.out.println(a == b);
    }

    public static void m_5() {
        String a = "some_string";
        String b = "another_string";

        System.out.println(a + b);
        System.out.println(a.concat(b));
    }

    public static void m_6() {
        StringBuilder a = new StringBuilder("some_string");
        a.append("another_string");

        System.out.println(a.toString());
    }

    public static void m_7(Integer notANormalInt) {
        System.out.println(notANormalInt);
    }

    public static void m_8() {
        Something a = new Something();
        Something b = new Something();
        b.b = 100;
        System.out.println("Printing a");
        a.print_all();
        System.out.println("Printing b");
        b.print_all();

        Something.change_a();

        System.out.println("After changing, printing a");
        a.print_all();
        System.out.println("After changing, printing b");
        b.print_all();
    }

    public static void scratch() {
    }

    public static void main(String[] args) {
        // m_1();
        // m_2();
        // m_3();
        // m_4();
        // m_5();
        // m_6();
        m_7(123);
        // scratch();
    }
}
