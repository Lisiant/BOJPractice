import java.util.*;

class Solution {
    
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        Integer[] arr = Arrays.stream(score).boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Collections.reverseOrder());
        

        int cnt = score.length / m;
        ArrayList<Integer> temp = new ArrayList<>();

        for (int i = 0; i < score.length; i++) {

            if (i > 0 && i % m == 0) {
                Integer min = temp.stream().min(Integer::compareTo).get();
                answer += min * m;   
                temp.clear();
            }

            temp.add(arr[i]);

        }
        if (score.length % m == 0) {
            Integer min = temp.stream().min(Integer::compareTo).get();
            answer += min * m;

        }

        return answer;
    }
}