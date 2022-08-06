package Taylor_leetcode_prac;

public class M11 {
    /*
     * You are given an integer array height of length n. There are n vertical lines
     * drawn such that the two endpoints of the ith line are (i, 0) and (i,
     * height[i]).
     * 
     * Find two lines that together with the x-axis form a container, such that the
     * container contains the most water.
     * 
     * Return the maximum amount of water a container can store.
     * 
     * Notice that you may not slant the container.
     */

    /*
     * two pointer solution, one from left, one from right. update pointers based on
     * smaller value
     */
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int max = 0;

        while (left < right) {
            int currHeight = Math.min(height[right], height[left]);
            int currWidth = right - left;

            int currAmount = currHeight * currWidth;

            if (currAmount > max) {
                max = currAmount;
            }

            if (height[left] > height[right]) {
                right--;
            } else {
                left++;
            }

        }

        return max;
    }
}
