
import java.io.*;
import java.util.*;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System.in);
        int n=scn.nextInt();
        int m=scn.nextInt ();
        
        int [][] arr;
        arr= new int [n][m];
        for(int i=0;i<arr.length ;i++){
            for (int j=0;j<arr[0].length ;j++){
                arr[i][j]=scn.nextInt();
            }
        }
        
        int x =scn.nextInt ();
        int i=0;
        int j=arr[0].length -1;
        while (i<arr.length && j>=0){
            if(x==arr[i][j]){
                System .out.println (i);
                System .out.println (j);
                return ;
            }
            else if(x<arr[i][j]){
                j--;
            }
            else {
                i++;
            }
        }
        System .out.println ("not found");

        
    }
    

}
