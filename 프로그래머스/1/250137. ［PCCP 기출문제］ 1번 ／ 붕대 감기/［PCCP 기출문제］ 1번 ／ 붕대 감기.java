class Solution {

    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = 0;

        int lastAttack = attacks[attacks.length - 1][0];
        int curHealth = health;
        int attackNum = 0;
        int cnt = -1;

        for (int i = 0; i <= lastAttack; i++) {

            int[] curAttack = attacks[attackNum];

            if (i != curAttack[0]) {
                curHealth += bandage[1];
                curHealth = Math.min(curHealth, health);
                cnt += 1;

                if (cnt == bandage[0]) {
                    cnt = 0;
                    curHealth += bandage[2];
                    curHealth = Math.min(curHealth, health);
                }

            } else {
                curHealth -= curAttack[1];
                cnt = 0;
                if (curHealth <= 0){
                    System.out.println(i);
                    return -1;
                }
                attackNum++;
            }

        }

        answer = curHealth;
        return answer;
    }
}