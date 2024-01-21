package second.week.generics;

import java.util.ArrayList;
import java.util.List;

class SuperClass {
    void something() {
        System.out.println("im super");
    }
}

class SubClass extends SuperClass {
    void something() {
        System.out.println("im sub");
    }
}

public class Generics {
    public static <T extends SuperClass> void doSomethingGeneric(T object) {
        object.something(); // static dispatch
        awefioojaweofjawioej
    }

    public static void doSomething(SuperClass object) {
        object.something(); // dynamic dispatch
    }

    public static void main(String[] args) {
        SuperClass object = new SubClass();
        doSomething(object);
        doSomethingGeneric(object);
    }
}
