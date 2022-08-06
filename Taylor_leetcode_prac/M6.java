package Taylor_leetcode_prac;

import java.util.ArrayList;

public class M6 {
    /*
     * The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
     * of rows like this: (you may want to display this pattern in a fixed font for
     * better legibility)
     * 
     * P A H N
     * A P L S I I G
     * Y I R
     * And then read line by line: "PAHNAPLSIIGYIR"
     * 
     * Write the code that will take a string and make this conversion given a
     * number of rows:
     * 
     * string convert(string s, int numRows);
     */

    // first try, intuitive solution: 30% 8%
    /*
     * following the logic order of letters entered, and manipulate row & column
     * numbers:
     * 1 5 9
     * 2 4 6 8
     * 3 7
     * 
     */
    public String convert(String s, int numRows) {
        ArrayList<ArrayList<String>> raw = new ArrayList<>();

        for (int i = 0; i < numRows; i++) {
            raw.add(new ArrayList<String>());
        }

        int i = 0;
        int counter = 0;

        while (i < s.length()) {

            while (counter < numRows && i < s.length()) {
                raw.get(counter).add(Character.toString(s.charAt(i)));
                i++;
                counter++;
            }

            counter = Math.max(0, counter - 2);

            while (counter >= 0 && i < s.length()) {
                raw.get(counter).add(Character.toString(s.charAt(i)));
                i++;
                counter--;
            }

            counter = Math.min(numRows - 1, counter + 2);
        }

        String res = "";

        for (int j = 0; j < raw.size(); j++) {
            for (int k = 0; k < raw.get(j).size(); k++) {
                res = res + raw.get(j).get(k);
            }
        }

        return res;
    }
}
