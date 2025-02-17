import java.io.*;
import java.util.*;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System.in);
        int n=scn.nextInt();
        int m=scn.nextInt ();
        
        int [][] arr;
        arr= new int [n][m];// n*m matrix
        for(int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                arr[i][j]=scn.nextInt();
            }
        }
        
        for(int i=0;i<n;i++){
            for (int j=0;j<m;j++){
               System .out.println (arr[i][j]);
            }
        }
        
        System .out.println ("rows are "+ arr.length);
        System .out.println ("cols are "+arr[0].length );
         
    }
          }
