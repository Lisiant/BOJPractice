import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String[] s = br.readLine().split(" ");
        int y = Integer.parseInt(s[0]);
        int x = Integer.parseInt(s[1]);
        StringBuilder sb = new StringBuilder();
        int xy = x * y;
        for (int i = 1; i <= xy; i++) {
            if (i % x == 0 && i % y == 0) sb.append(3);
            else if (i % x == 0) sb.append(1);
            else if (i % y == 0) sb.append(2);
        }
        bw.write(sb.toString());
        bw.flush();


    }
}