package java_test;

import java.util.Scanner;

public class c {
    public static void main(String[] args) {

        int age, height;
        Scanner sc = new Scanner(System.in);
        age = sc.nextInt();
        height = sc.nextInt();

        if(age >= 14 || height >= 155) {
            System.out.println('X');
        } else{
            System.out.println('O');
        }
        sc.close();

    }

}