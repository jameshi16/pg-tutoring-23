package second.week.pain;

import java.util.List;

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
        print("hi");
        print(123);
        print(List.of("1", "2", "3"));
        someGenericFunction("tomfoolery");
        someGenericFunction(123);
        Parent p = new Child();
        System.out.println("Hello World!");
    }
}
