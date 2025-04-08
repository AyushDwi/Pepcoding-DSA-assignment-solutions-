import java.util.*;
import java.lang.Math;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System .in);
        int n1=scn.nextInt();
        int n2=scn.nextInt ();
        int b=scn.nextInt ();
        int ans =AnyBaseAddition(n1,n2,b);
        System .out.println (ans);
    }
    
    public static int AnyBaseAddition (int n1,int n2,int b){
        int rem1=0;
        int rem2=0;
        int c=0;
        int temp =0;
        int p=0;
        int s=0;
        while (n1!=0 || n2!=0 || c!=0){
            rem1 =n1%10;
            rem2 =n2%10;
            n1=n1/10;
            n2=n2/10;
            if(rem1 +rem2+c>=b){
                s=(rem1 +rem2+c)%b;
                c=(rem1 +rem2+c)/b;
                
            }
            
            else {
                s=(rem1 +rem2+c);
                c=0;
            }
            
            temp+= (int)Math.pow(10,p)*s;
            p++;
            
        }
        return temp;
        
    }
}
//mistakes I previously did.
//didn't reset the carry in the else part.
//wrote rem1+rem2+c>b instead of >=b.
