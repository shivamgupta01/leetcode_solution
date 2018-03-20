package selfDividingNumber728;

import java.util.ArrayList;
import java.util.List;




public class Solution {

    public static void main(String[]args){
        Solution solution = new Solution();
        System.out.println("Solution is : " + solution.selfDividingNumbers(1,22));
    }
    public List<Integer> selfDividingNumbers(int left, int right) {
        int flag = 1;
        List<Integer> listOfSelfDividingNumber = new ArrayList<Integer>();
        for(int i =left;i<=right;i++) {
            flag = 1;

            for (char s : String.valueOf(i).toCharArray()) {

                    if (s=='0' || i%(s-'0')!=0 ){
                        flag = 0;
                        break;
                    }


            }
            if (flag == 1){
                listOfSelfDividingNumber.add(Integer.valueOf(i));}
        }
        return listOfSelfDividingNumber;

    }
}
