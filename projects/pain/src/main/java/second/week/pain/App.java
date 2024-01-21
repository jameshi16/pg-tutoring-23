package second.week.pain;

import java.util.List;
import second.week.observer.Publisher;
import second.week.observer.Subscriber;

public class App {
    static <T> void print(T s) {
        System.out.println("my very unique and special print function: " + s.toString());
    }

    static <T extends List<X>, X> void print(T list) {
        for (X i : list) {
            System.out.println(i);
        }
    }

    static <T> void someGenericFunction(T thingy) {
        System.out.println(thingy instanceof String);
    }

    static <X> void someGenericListFunction(List<X> thingy) {
        System.out.println(thingy instanceof List<?>);
    }

    public static void main(String[] args) {
        // Transport transport = Factory.createTransport("car");
        // System.out.println(transport instanceof Car);

        // Eatable<SomeFood> eatable = new Eatable<>(new SomeFood());
        // fnOnEatable(eatable);

        Publisher publisher = new Publisher();

        Subscriber sub_1 = new Subscriber("first sub");
        Subscriber sub_2 = new Subscriber("julie");

        publisher.add_observer(sub_1);
        publisher.add_observer(sub_2);

        publisher.publish("a message");
    }
}
