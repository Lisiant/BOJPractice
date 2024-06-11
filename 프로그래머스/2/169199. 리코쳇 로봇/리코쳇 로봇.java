import java.io.*;
import java.util.*;

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Solution {
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};


    public int solution(String[] board) {
        int answer = -1;
        int n = board.length;
        int m = board[0].length();

        int[][] vis = new int[n][m];
        Queue<Point> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i].charAt(j) == 'R') {
                    q.add(new Point(i, j));
                    vis[i][j] = 1;
                    break;
                }
            }
        }

        while (!q.isEmpty()) {
            Point cur = q.poll();
            // 현재 지점이 도착지점인지 확인

            if (board[cur.x].charAt(cur.y) == 'G') {
                answer = vis[cur.x][cur.y] - 1;
                break;
            }

            // 4가지 방향 탐색
            for (int i = 0; i < 4; i++) {
                int nx = cur.x + dx[i];
                int ny = cur.y + dy[i];

                // 해당 방향으로 끝까지 이동
                while (true) {
                    if (!inRange(nx, ny, n, m) || board[nx].charAt(ny) == 'D') {
                        nx -= dx[i];
                        ny -= dy[i];
                        break;
                    } else {
                        nx += dx[i];
                        ny += dy[i];
                    }
                }

                if (vis[nx][ny] == 0) {
                    vis[nx][ny] = vis[cur.x][cur.y] + 1;
                    q.add(new Point(nx, ny));
                }
            }
        }
        return answer;
    }

    private boolean inRange(int nx, int ny, int n, int m) {
        return 0 <= nx && nx < n && 0 <= ny && ny < m;
    }

}