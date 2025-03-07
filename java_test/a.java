package java_test;

import java.util.Scanner;

public class a {
    public static void main(String[] args) {
        int num, a, b, c;
        Scanner sc = new Scanner(System.in);
        num = sc.nextInt();
        a = num / 100;
        b = num / 10 % 10;
        c = num % 10;

        System.out.printf("%d%d%d", c, b, a);
        sc.close();
        

    }

}