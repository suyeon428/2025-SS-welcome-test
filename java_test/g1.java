package java_test;

import java.util.Scanner;

class Fan {
    private String model;
    private int price;

    public Fan (String model, int price) {
        this.model = model;
        this.price = price;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
}


public class g1 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        String mod1 = sc.next();
        int pri1 = sc.nextInt();
        Fan fan1 = new Fan(mod1, pri1);

        String mod2 = sc.next();
        int pri2 = sc.nextInt();
        Fan fan2 = new Fan(mod2, pri2);

        String mod3 = sc.next();
        int pri3 = sc.nextInt();
        Fan fan3 = new Fan(mod3, pri3);

        Fan cheap = fan1;

        if (fan2.getPrice() < cheap.getPrice()) {
            cheap = fan2;
        }
        if (fan3.getPrice() < cheap.getPrice()) {
            cheap = fan3;
        }

        System.out.println(cheap.getModel());
        sc.close();


    }

}