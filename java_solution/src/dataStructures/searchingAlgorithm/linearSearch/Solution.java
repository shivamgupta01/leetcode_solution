package dataStructures.searchingAlgorithm.linearSearch;

public class Solution {
    public static void main(String[] args) {
        int[] arr = {1,4,2,3,5,6,7,9,8};
        Solution solution = new Solution();
        int res = solution.LinearSearch(arr,4);
        if (res==-1){
            System.out.println("The Key is not present in the Array");
        }
        else {
            System.out.println("The Key is present at : " + res);
        }
    }


    public int LinearSearch(int[] arr, int key){
        for(int i = 0;i<arr.length;i++){
            if (arr[i]==key){
                return (i+1);
            }
        }
        return -1;
    }
}
