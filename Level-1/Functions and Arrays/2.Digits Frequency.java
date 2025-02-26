import java.util.*;

public class Program
{
    public static void main(String[] args) {
        
        Scanner scn=new Scanner (System .in);
        int n= scn.nextInt();
        int x=scn.nextInt ();
        int ans=dig_count(n,x);
        System .out.println ("count of digit "+x+" in the number "+n+" is "+ans);
    }
    
    public static int dig_count ( int n, int x){
        int count=0;
        while (n>0){
            if (n%10==x){
                count++;
                
            }
            n=n/10;
        }
        
        return count ;
    }
}
