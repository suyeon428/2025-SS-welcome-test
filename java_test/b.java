package java_test;

import java.util.Scanner;

public class b {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int check = 0;

        for(int i=0; i<str.length(); i++){
            char c = str.charAt(i);
            
            if(c=='a' || c=='e' || c=='i' || c=='o' || c=='u'){
                check = 1;
                break;
            }
        }
        if(check == 1) {
            System.out.println('O');
        } else {
            System.out.println('X');
        }
        sc.close();


    }

}