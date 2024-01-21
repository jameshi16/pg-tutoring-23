package second.week.singleton;

class Main2 {
    public static void main(String[] args) {
        MySingleton singleton = new MySingleton();
        MySingleton singleton2 = new MySingleton();

        singleton.name = "something";
        singleton.printFields();
        System.out.println(singleton.name);
        System.out.println(singleton2.name);
    }
}
