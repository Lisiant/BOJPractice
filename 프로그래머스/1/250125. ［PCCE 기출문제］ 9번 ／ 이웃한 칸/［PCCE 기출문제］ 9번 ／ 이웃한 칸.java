class Solution {
    public int solution(String[][] board, int h, int w) {
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        int n = board.length;
        int nx, ny;
        int answer = 0;

        String cur = board[h][w];
        for (int i = 0; i < 4; i++) {
            nx = h + dx[i];
            ny = w + dy[i];

            if (!inRange(nx, ny, n)) continue;
            if (board[nx][ny].equals(cur)) answer++;
        }

        return answer;
    }
    
    public boolean inRange(int nx, int ny, int n) {
        return 0 <= nx && nx < n && 0 <= ny && ny < n;
    }
}