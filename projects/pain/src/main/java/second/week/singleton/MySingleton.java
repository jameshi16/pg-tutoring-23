package second.week.singleton;

class NotSingleton {
    public void printFields() {
        System.out.println("Has no fields");
    }
}

class MySingleton extends NotSingleton {
    public static String name = "Jack";
    public static String connection = "db://localhost";
    private static MySingleton instance = null;

    public MySingleton() {

    }

    public void printFields() {
        System.out.printf("%s %s\n", this.name, this.connection);
    }

    // public static MySingleton getInstance() {
    // if (instance == null) {
    // instance = new MySingleton();
    // }
    // return instance;
    // }
}
