package intro.java;

class MinimalClass {
    private String some_a;
    private Integer some_b;

    public MinimalClass() {
    }

    public MinimalClass(String some_a, Integer some_b) {
        this.some_a = some_a;
        this.some_b = some_b;
    }

    public void doSomething() {
        System.out.println(some_a);
        System.out.println(some_b);
    }
}
