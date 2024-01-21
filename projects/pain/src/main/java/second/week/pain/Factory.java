package second.week.pain;

class Factory {
    static int a = 0;
    int b = 0;

    static Transport createTransport(String iden) {
        switch (iden) {
            case "ship":
                return new Ship();
            case "car":
                return new Car();
            default:
                return new Car();
        }
    }
}
