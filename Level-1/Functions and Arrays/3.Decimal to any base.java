import java.util.*;

public class Program {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
    
        int n = scn.nextInt();
        
        int b = scn.nextInt();

        String ans = d_to_b(n, b);  
        System.out.println("The decimal number " + n + " in the base of " + b + " is written as " + ans);  
    }  

    public static String d_to_b(int n, int b) {  
        if (n == 0) {
            return "0";
        }
        StringBuilder result = new StringBuilder();
        while (n > 0) {
            int remainder = n % b;
            result.insert(0, remainder); // Insert the remainder at the beginning of the string
            n = n / b;
        }
        return result.toString();
    }
}
