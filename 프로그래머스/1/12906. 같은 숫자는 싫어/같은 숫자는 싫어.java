import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        stk.add(arr[arr.length - 1]);
        for (int i = arr.length - 2; i >= 0; i--) {
            if (arr[i] == stk.peek()) {
                continue;
            }
            stk.add(arr[i]);
        }
        int size = stk.size();
        int[] answer = new int[size];

        for (int i = 0; i < size; i++) {
            answer[i] = stk.pop();
        }
        return answer;
    }
}