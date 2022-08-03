package Taylor_leetcode_prac;

import java.util.LinkedHashMap;

public class M12 {
    /*
     * Given an integer, convert it to a roman numeral.
     */

    public String intToRoman(int num) {
        LinkedHashMap<String, Integer> values = new LinkedHashMap<>();
        // can replace linked hashmap with two parellel array

        values.put("M", 1000);
        values.put("CM", 900);
        values.put("D", 500);
        values.put("CD", 400);
        values.put("C", 100);
        values.put("XC", 90);
        values.put("L", 50);
        values.put("XL", 40);
        values.put("X", 10);
        values.put("IX", 9);
        values.put("V", 5);
        values.put("IV", 4);
        values.put("I", 1);

        int remain = num;
        String res = "";

        while (remain != 0) {
            for (String key : values.keySet()) {
                if (values.get(key) <= remain) {
                    res += key;
                    remain -= values.get(key);
                    break;
                }
            }
        }

        return res;
    }
}
