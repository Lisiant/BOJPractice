import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] data = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .sorted()
                .toArray();

        int m = Integer.parseInt(br.readLine());
        int[] check = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt).toArray();

        for (int i : check) {
            int mid = binarySearch(data, i, n-1);
            System.out.println(mid);
        }
    }

    private static int binarySearch(int[] data, int target, int en) {
        int st = 0;
        int mid;

        while (st <= en) {

            mid = (st + en) / 2;
            
            if (data[mid] == target) {
                return 1;
            } else if (data[mid] < target) {
                st = mid + 1;
            } else {
                en = mid - 1;
            }
        }
        return 0;
    }


}