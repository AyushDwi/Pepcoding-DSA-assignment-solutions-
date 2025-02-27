import java.util.*;
import java.lang.Math;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System .in);
        int n=scn.nextInt();
        int b1=scn.nextInt ();
        int b2=scn.nextInt ();
        
        int ans1 =b_to_d(n,b1);
        int ans2=d_to_b(ans1 ,b2);
        
        System .out.println (ans2);
        
    }
    
    
    public static int d_to_b (int n,int b){
        int temp=0;
        int p=1;
        while(n>0){
            int dig=n%b;
            n=n/b;
            
            temp+=dig*p;
            p=p*10;
        }
        return temp ;
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
