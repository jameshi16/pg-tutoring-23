package intro.java;

class Something {
    static int a = 123;
    public int b = 456;

    Something() {
        this.b = 789;
    }

    static void change_a() {
        Something.a = 0;
    }

    void print_all() {
        System.out.println(Something.a);
        System.out.println(this.b);
    }
}
