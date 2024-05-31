import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int[] arr = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        int res = arr[0];

        int[] newArr = Arrays.stream(arr).map(value -> value - arr[0]).toArray();

        for (int i = 0; i < 3; i++) {
            res += newArr[i] / 3;
            newArr[i] = newArr[i] % 3;
        }

        if (newArr[1] == 0 && newArr[2] == 0) {
            res += 0;
        } else if (newArr[1] == 2 && newArr[2] == 1
                || newArr[1] == 1 && newArr[2] == 2
                || newArr[1] == 2 && newArr[2] == 2
        ) {
            res += 2;
        } else {
            res += 1;
        }
        System.out.println(res);
    }
}
