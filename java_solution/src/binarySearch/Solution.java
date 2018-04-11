package binarySearch;

import java.util.List;

public class Solution {
    public static void main(String[] args) {
        int[] list = {1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,13,14,15};
        int result = binarySearch(list,16);
        if (result == -1){
            System.out.println("The Element was not found in the list");
        }
        else {
            System.out.println("The element was found at position: " + result);
        }
    }
    public static int binarySearch(int[] list,int key){
        int i = 0;
        int j = list.length-1;

        while(i<=j){
            int mid = (i +j)/2;
            if (list[mid]==key){
                return mid+1;
            }
            else if (list[mid]>key) {
                j = mid-1;
            }
            else {
                i = mid+1;
            }
        }
        return -1;
    }
}
