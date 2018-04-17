package test;

public class Solution {
    public static void main(String[] args) {
        int[] queue = {1,2,3};
        int temp1;
        int temp2=queue[0];
        for (int i = 0;i<queue.length-1;i+=1){
            temp1 = queue[i+1];
            queue[i+1]=temp2;
            temp2 = temp1;
    }
        for(int i =0;i<queue.length;i++){
            System.out.println(queue[i]);
        }
}}
