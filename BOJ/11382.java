import java.util.*;
import java.io.*;
import java.math.*;

public class Main{
	public static void main(String[] args) throws Exception{
		var br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer s = new StringTokenizer(br.readLine());
		BigInteger result = new BigInteger("0");
		while(s.hasMoreTokens()){
			BigInteger b = new BigInteger(s.nextToken());
			result = result.add(b);
		}
		System.out.println(result);
	}
}
