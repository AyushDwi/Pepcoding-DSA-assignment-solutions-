//step1: store from shell to 1 D array.
//step2: rotate the 1 D array.
//step3: store from rotated 1D array to shell.


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
        for(int i=0;i<arr.length ;i++){
            for (int j=0;j<arr[0].length ;j++){
                arr[i][j]=scn.nextInt();
            }
        }
        
        int s = scn.nextInt ();
        int r=scn.nextInt ();
        
        rotateShell(arr,s,r);
        
        display(arr);
        
    }
    
    public static void rotateShell (int[][] arr,int s, int r){
        int[] one_d=fillOneD_FromShell(arr,s);
        rotate(one_d ,r);
        fillShellFrom_OneD(arr,s,one_d );
    }
    
    public static int[] fillOneD_FromShell (int[][] arr,int s){
    int minr=s-1;
    int minc=s-1;
    int maxr=arr.length -s;
    int maxc=arr[0].length -s;
    int sz=2*(maxr-minr+maxc -minc);
    int[] one_d =new int [sz];
    
    //lw
    int idx=0;
    for(int i=minr,j=minc;i<=maxr;i++){
       one_d [idx]=arr[i][j];
       idx ++;
    }
    
    //bw
    for(int i=maxr,j=minc+1;j<=maxc;j++){
       one_d [idx]=arr[i][j];
       idx ++;
    }
    
    //rw
    for(int i=maxr-1,j=maxc;i>=minr;i--){
       one_d [idx]=arr[i][j];
       idx ++;
    }
    
    //tw
    for(int i=minr,j=maxc-1;j>=minc+1;j--){
       one_d [idx]=arr[i][j];
       idx ++;
    }
    
    
    return one_d ;
        
    }
    
    
    public static void fillShellFrom_OneD (int[][] arr,int s,int[] one_d ){
        
        
        int minr=s-1;
    int minc=s-1;
    int maxr=arr.length -s;
    int maxc=arr[0].length -s;
    
    //lw
    int idx=0;
    for(int i=minr,j=minc;i<=maxr;i++){
      arr[i][j]= one_d [idx];
       idx ++;
    }
    
    //bw
    for(int i=maxr,j=minc+1;j<=maxc;j++){
       arr[i][j]= one_d [idx];
       idx ++;
    }
    
    //rw
    for(int i=maxr-1,j=maxc;i>=minr;i--){
       arr[i][j]= one_d [idx];
       idx ++;
    }
    
    //tw
    for(int i=minr,j=maxc-1;j>=minc+1;j--){
       arr[i][j]= one_d [idx];
       idx ++;
    }
    
    }
    
    
    
    public static void rotate(int[] one_d ,int r){
        r=r%one_d.length ;
        if(r<0){
            r=r+one_d.length ;
        }
        reverse(one_d ,0,one_d .length -r-1);
        reverse (one_d ,one_d .length -r,one_d .length-1 );
        reverse (one_d,0 ,one_d .length -1);
    }
    
    public static void reverse (int[] one_d , int li,int ri){
        while (li<ri){
            int temp=one_d[li];
            one_d [li]=one_d[ri];
            one_d [ri]=temp;
            li++;
            ri--;
        
        }
    }
    
    public static void display(int[][] arr){
        for(int i=0;i<arr.length;i++){
            for (int j=0;j<arr[0].length;j++){
               System .out.print (arr[i][j]+ " ");
            }
            System .out. println ();
        }
    }
}
