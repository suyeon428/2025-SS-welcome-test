package java_test;

import java.util.Scanner;

public class d {
    public static void main(String[] args) {

        int n, result=0;
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();

        if(n <= 0) {
            System.out.println('X');
        } else{
            for(int i=n; i>0; i--)
            result += i;
        }
        if(result != 0){
            System.out.println(result);
        }
        sc.close();

    }

}