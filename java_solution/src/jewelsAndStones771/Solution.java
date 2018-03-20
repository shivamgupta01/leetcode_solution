package jewelsAndStones771;


//771. Jewels and Stones
//        DescriptionHintsSubmissionsDiscussSolution
//        You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.
//
//        The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
//
//        Example 1:
//
//        Input: J = "aA", S = "aAAbbbb"
//        Output: 3
//        Example 2:
//
//        Input: J = "z", S = "ZZ"
//        Output: 0
//        Note:
//
//        S and J will consist of letters and have length at most 50.
//        The characters in J are distinct.


import java.util.HashMap;

public class Solution {

    public static void main(String[] args) {

        Solution solution = new Solution();
        System.out.println(solution.numJewelsInStones("aA","aAAbbbb"));

            }




    public int numJewelsInStones(String J,String S) {

        HashMap<Character, Integer> jewel = new HashMap<Character, Integer>();
        int noOfStones = 0;

        for (int i = 0; i < S.length(); i++) {
            if (jewel.containsKey(S.charAt(i))) {
                jewel.put(S.charAt(i), jewel.get(S.charAt(i)) + 1);
            } else {
                jewel.put(S.charAt(i), 1);
            }
        }


        for (int i = 0; i < J.length(); i++) {
//            if (jewel.containsKey(J.charAt(i))) {
//
//                noOfStones = noOfStones + jewel.get(J.charAt(i));
//
//            }
                    try{        noOfStones = noOfStones + jewel.get(J.charAt(i));}
                    catch (Exception e){noOfStones = noOfStones;}


        }
            return noOfStones;



    }
}
