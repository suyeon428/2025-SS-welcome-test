package java_test;

import java.util.Scanner;

public class f {
    public static void main(String[] args) {

        int N;
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();

        for(int i=0; i<N; i++) {
            for(int j=0; j < N - i -1; j++) {
                System.out.print(' ');
            }
            for(int k=0; k < 2*i+1; k++){
                System.out.print('*');
            }
            System.out.println();
        }
        for(int i=N-2; i>=0; i--) {
            for(int j=0; j<N-i-1; j++) {
                System.out.print(' ');
            }
            for(int k = 0; k<2*i+1; k++) {
                System.out.print('*');
            }
            System.out.println();
        }
        sc.close();

    }

}
