import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int minPackage = Integer.MAX_VALUE;
        int minEach = Integer.MAX_VALUE;

        for (int i = 0; i < m; i++) {
            int[] array = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            minPackage = Math.min(array[0], minPackage);
            minEach = Math.min(array[1], minEach);
        }
/**
 * 1. 최소 패키지가격 * (n/6+1)
 * 2. 최소 패키지 가격 * (n/6) + 최소 낱개 가격 * (n%6)
 * 3. 최소 낱개 가격 * n
 */


        int res = Math.min(Math.min(minPackage * (n / 6 + 1), minEach * n), minPackage * (n / 6) + minEach * (n % 6));
        System.out.println(res);

    }
}