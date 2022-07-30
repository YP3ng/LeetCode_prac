package Taylor_leetcode_prac;

/*
 * Given a string s, find the length of the longest substring without repeating characters.
 */
public class M3 {
    /*
     * use two pointers, one point at start of sub string, one point at end of sub
     * aka sliding window
     */
    public int lengthOfLongestSubstring(String s) {
        int res = 0;
        int[] chars = new int[128];
        int left = 0;
        int right = 0;

        while (right < s.length()) {
            char r = s.charAt(right);
            chars[r]++;

            while (chars[r] > 1) {
                char l = s.charAt(left);
                chars[l]--;
                left++;
            }

            res = Math.max(res, right - left + 1);
            right++;
        }

        return res;
    }
}
