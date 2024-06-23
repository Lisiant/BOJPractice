import java.util.*;

class Solution {
    public String solution(String s, String skip, int index) {
        StringBuilder answer = new StringBuilder();
        ArrayList<Character> chs = new ArrayList<>();
        for (char i = 'a'; i <= 'z'; i++) {
            if (!skip.contains(Character.toString(i))) {
                chs.add(i);
            }
        }
        int maxLen = chs.size();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            int idx = chs.indexOf(c);
            Character c1 = chs.get((idx + index) % maxLen);
            answer.append(c1);
        }
        System.out.println(answer);
        return answer.toString();

    }
}