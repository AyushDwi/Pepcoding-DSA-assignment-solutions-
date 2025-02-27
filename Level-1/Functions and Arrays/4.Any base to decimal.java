import java.util.*;
import java.lang.Math;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System .in);
        int n=scn.nextInt();
        int b=scn.nextInt ();
        int ans =b_to_d(n,b);
        System .out.println (ans);
        
    }

    public static int b_to_d (int n,int b){
        int temp=0;
        int rev=0;
        int p=0;
        while (n>0){
            rev=n%10;
            temp+=rev*Math.pow(b,p);
            n=n/10;
            p++;
        }
        return temp ;
    }
}
