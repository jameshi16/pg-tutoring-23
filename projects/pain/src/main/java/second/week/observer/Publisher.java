package second.week.observer;

import java.util.ArrayList;
import java.util.List;

public class Publisher {
    List<Subscriber> subscribers = new ArrayList<>();

    public void add_observer(Subscriber subscriber) {
        this.subscribers.add(subscriber);
    }

    public void publish(String message) {
        for (Subscriber subscriber : this.subscribers) {
            subscriber.on_message(message);
        }
    }
}
