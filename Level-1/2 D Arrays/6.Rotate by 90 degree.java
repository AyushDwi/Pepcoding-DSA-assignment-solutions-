// take transpose , then perform row reversal.

import java.io.*;
import java.util.*;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System.in);
        int n=scn.nextInt();
        
        int [][] arr;
        arr= new int [n][n];
        for(int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                arr[i][j]=scn.nextInt();
            }
        }
        
        //transpose
        //cover only upper triangular portion.
        for(int i=0;i<n;i++){
            for (int j=i;j<n;j++){//prevents swapping twice.
                int temp=arr[i][j];
                arr[i][j]=arr[j][i];
                arr[j][i]=temp;
            }
        }
        
        //reversal
        for (int i=0;i<n;i++){
            int li=0;
            int ri=n-1;
            
            while (li<ri){
                int temp=arr[i][li];
                arr[i][li]=arr[i][ri];
                arr[i][ri]=temp;
                li++;
                ri--;
                
            }
        }
        
        
        for(int i=0;i<arr.length;i++){
            for(int j=0;j<arr[0].length;j++){
                System .out.print (arr[i][j]+ " ");
                
            }
            System .out.println ();
        }
            
        }
    }
