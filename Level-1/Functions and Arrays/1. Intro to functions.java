import java.util.*;


public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System .in);
        int n=scn.nextInt();
        int r=scn.nextInt ();
        
        int nfact=fact(n);
        int rf=fact(n-r);
        int ans=nfact/rf;
        System .out.println ("Number of permutations of "+r+" items out of "+n+" items ="+ans);
    }
    
    public static int fact (int n){
        if (n<=1){
            return 1;
        }
        return n*fact(n-1);
    }
}
