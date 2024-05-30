import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        int res = Integer.MAX_VALUE;
        ArrayList<Integer> data = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int element = Integer.parseInt(br.readLine());
            data.add(element);
        }

        data.sort(Comparator.naturalOrder());

        for (Integer x : data) {
            int temp = 0;
            for (int i = x; i < x + 5; i++) {
                if (!data.contains(i)) {
                    temp += 1;
                }
            }
            res = Integer.min(temp, res);
        }
        System.out.println(res);
    }
}
