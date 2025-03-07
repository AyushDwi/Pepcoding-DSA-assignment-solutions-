import java.io.*;
import java.util.*;

public class Program
{
    public static void main(String[] args) {
        Scanner scn=new Scanner (System.in);
        int n=scn.nextInt();
        int m=scn.nextInt ();
        
        int [][] arr= new int [n][m];
        for(int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                arr[i][j]=scn.nextInt();
            }
        }
        
        int minrow=0;
        int mincol=0;
        int maxrow=n-1;
        int maxcol=m-1;
        int tne=n*m;
        int count=0;
        
        while (count <tne ){
            //left wall 
            for (int i=minrow,j=mincol;i<=maxrow && count <tne;i++){
                System .out.println (arr[i][j]);
                count ++;
            }
            
            mincol =mincol+1;
            
            //bottom wall
            for(int i=maxrow,j=mincol;j<=maxcol && count <tne;j++){
                System .out.println (arr[i][j]);
                count++;
            }
            
            maxrow =maxrow-1;
            
            //right wall
            for(int i=maxrow,j=maxcol;i>=minrow && count<tne;i--){
                System .out.println (arr[i][j]);
                count++;
            }
            
            maxcol =maxcol-1;
            
            //top wall
            
            for(int i=minrow,j=maxcol;j>=mincol && count <tne;j--){
                System .out.println (arr[i][j]);
                count++;
            }
            
            minrow =minrow+1;
        }
    
        
    
         
    }
}
