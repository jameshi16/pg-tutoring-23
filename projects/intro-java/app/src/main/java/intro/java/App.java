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

    public static void scratch() {
    }

    public static void main(String[] args) {
        // m_1();
        // m_2();
        // m_3();
        m_4();
        // scratch();
    }
}
