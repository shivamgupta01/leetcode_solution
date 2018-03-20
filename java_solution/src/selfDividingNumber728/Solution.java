package selfDividingNumber728;

import java.util.ArrayList;
import java.util.List;




public class Solution {

    public static void main(String[]args){
        Solution solution = new Solution();
        System.out.println("Solution is : " + solution.selfDividingNumbers(9,11));
    }
    public List<Integer> selfDividingNumbers(int left, int right) {
        int flag = 1;
        List<Integer> listOfSelfDividingNumber = new ArrayList<Integer>();
        for(int i =left;i<=right;i++) {
            flag = 1;
            String[] parts = (Integer.toString(i).split(""));

            for (String s : parts) {
                try{
                    if (Integer.valueOf(i)==0 || Integer.valueOf(i)%Integer.valueOf(s)!=0 ){
                        flag = 0;
                        break;
                    }}
                catch (Exception e){
                    flag = 0;
                }

            }
            if (flag == 1){
                listOfSelfDividingNumber.add(Integer.valueOf(i));}
        }
        return listOfSelfDividingNumber;

    }
}
