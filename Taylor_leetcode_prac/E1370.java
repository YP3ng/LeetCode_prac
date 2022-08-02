package Taylor_leetcode_prac;
/*
 * 1370. Increasing Decreasing String
 * 
 * You are given a string s. Reorder the string using the following algorithm:

    Pick the smallest character from s and append it to the result.
    Pick the smallest character from s which is greater than the last appended character to the result and append it.
    Repeat step 2 until you cannot pick more characters.
    Pick the largest character from s and append it to the result.
    Pick the largest character from s which is smaller than the last appended character to the result and append it.
    Repeat step 5 until you cannot pick more characters.
    Repeat the steps from 1 to 6 until you pick all characters from s.
    In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

    Return the result string after sorting s with this algorithm.
 */

/*
 * first try by having three helper function removeLetter(), findSmall(), findLarge(), do it as normal logic
 * second try by using linkedHashMap and 26 char as keys, iterate forward and backwards until n.length == 0
 * lhm = {a : 1
 *        b : 1
 *        c : 0
 *        ...
 *        z : 0}
 
 * optimal solution, using int[] to represent 26 chars, same logic as above
 */
public class E1370 {
    public String sortString(String s) {
        int n = s.length(), cnt[] = new int[26];
        for (char c : s.toCharArray())
            cnt[c - 'a']++; // [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0] = 'aaaabbbbcccc'
                            // a b c d ... z
                            // 'b' - 'a' = 1

        StringBuilder sb = new StringBuilder();
        while (n > 0) {
            // increasing order checking
            for (int i = 0; i < 26 && n > 0; i++) {
                // check if we have usable char, if yes, take it to sb
                if (cnt[i] > 0) {
                    cnt[i]--;
                    sb.append((char) ('a' + i));
                    n--;
                }
            }

            // check from z to a
            for (int i = 25; i >= 0 && n > 0; i--) {
                if (cnt[i] > 0) {
                    cnt[i]--;
                    sb.append((char) ('a' + i));
                    n--;
                }
            }
        }
        return sb.toString();

        // String s = aaaabbbcccdde
        // int arr = [3, 2, 1, 0, 0..., 0]
        // res = abcbaa
        // "aaaabbbcccdde"

        // insertion steps:

        // ab ba ab acccdde

        // mergesort

        // a-b c-d e-d d-c
        // ab cd de cd
        //  abcd cdde

        // abcde ddc
        // example = abcde dcba abc aa
    }
}
