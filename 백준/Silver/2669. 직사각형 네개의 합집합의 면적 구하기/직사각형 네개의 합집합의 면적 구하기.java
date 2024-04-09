import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st;
        int[][] grid = new int[101][101];
        int res = 0;

        for (int i = 0; i < 4; i++) {
            st = new StringTokenizer(br.readLine());
            int ldx = Integer.parseInt(st.nextToken());
            int ldy = Integer.parseInt(st.nextToken());
            int rux = Integer.parseInt(st.nextToken());
            int ruy = Integer.parseInt(st.nextToken());

            for (int x = ldx; x < rux; x++) {
                for (int y = ldy; y < ruy; y++) {
                    if (grid[x][y] == 1) {
                        continue;
                    }
                    grid[x][y] = 1;
                }
            }
        }
        
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (grid[i][j] == 1) {
                    res += 1;
                }
            }
        }

        System.out.println(res);


    }
}
