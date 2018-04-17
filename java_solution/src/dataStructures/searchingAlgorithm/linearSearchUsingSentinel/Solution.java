package dataStructures.searchingAlgorithm.linearSearchUsingSentinel;

public class Solution {
    public static void main(String[] args) {
        int[] arr = {1,4,2,3,5,6,7,9,8};
        Solution solution = new Solution();
        int res = solution.linearSearchUsingSentinel(arr,88);
        if (res>arr.length-1){
            System.out.println("The Key is not present in the Array");
        }
        else {
            System.out.println("The Key is present at : " + res);
        }
    }


    public int linearSearchUsingSentinel(int[] list, int key){
        if (list[list.length-1]!=key){
            list[list.length-1] =key;
        }else {
            return list.length;
        }
        int i = 0;
        while (list[i]!=key){
            i +=1;
        }
        return i+1;

    }
}
