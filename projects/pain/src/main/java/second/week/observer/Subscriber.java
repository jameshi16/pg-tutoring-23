package second.week.observer;

public class Subscriber {
    String name;

    public Subscriber(String name) {
        this.name = name;
    }

    void on_message(String message) {
        System.out.printf("%s received %s\n", this.name, message);
    }
}
