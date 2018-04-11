package fibonacciSeries;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Solution {
     HashMap<Integer,Integer> dump = new HashMap<Integer, Integer>();

    public static void main(String[] args) {
        Solution solution = new Solution();
        for (int i = 1;i<=10;i++){
            System.out.println(solution.fibonacciSeries(i));

        }
    }

    public int fibonacciSeries(int n){
        int value;
        if (dump.containsKey(n)){return dump.get(n);}
        if ((n ==1)){
            value=  0;
        }
        else if(n==2 || n ==3){
            value = 1;
        }
        else {
            value = fibonacciSeries(n-1) + fibonacciSeries(n-2);

        }
        dump.put(n,value);
        return value;
    }



}
