package Taylor_leetcode_prac;

import java.util.HashMap;

/*
 * You have a chat log of n messages. You are given two string arrays messages and senders where messages[i] is a message sent by senders[i].

    A message is list of words that are separated by a single space with no leading or trailing spaces. The word count of a sender is the total number of words sent by the sender. Note that a sender may send more than one message.

    Return the sender with the largest word count. If there is more than one sender with the largest word count, return the one with the lexicographically largest name.

    Note:

    Uppercase letters come before lowercase letters in lexicographical order.
    "Alice" and "alice" are distinct.
 */

public class M2284 {
    public String largestWordCount(String[] messages, String[] senders) {
        HashMap<String, Integer> map = new HashMap<>();
        for (int i = 0; i < messages.length; i++)
            // instead of having if-else to distinguish wheather a key is in dic
            // we can use getOrDefault to simplify
            map.put(senders[i], map.getOrDefault(senders[i], 0) + messages[i].split(" ").length);

        int max = -1;
        String result = "";
        for (String key : map.keySet()) {
            // other then checking charAt(0)'key value, we can use build in compareTo()
            // function
            if (map.get(key) > max || (map.get(key) == max && result.compareTo(key) < 0)) {
                max = map.get(key);
                result = key;
            }
        }
        return result;
    }
}
