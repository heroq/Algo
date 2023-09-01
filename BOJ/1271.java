import java.io.*;
import java.util.*;
import java.math.*;
public class Main {
	public static void main(String[] args) throws Exception {
		var br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer a = new StringTokenizer(br.readLine());
		BigDecimal s1 = new BigDecimal(a.nextToken());
		BigDecimal s2 = new BigDecimal(a.nextToken());

		BigDecimal bg[] = s1.divideAndRemainder(s2);

		System.out.println(bg[0]);
		System.out.println(bg[1]);

	}
}

