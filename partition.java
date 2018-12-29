

public class partition {

	public static void main(String[] args) {
		
		//int[] X = new int[4];
		//generatePartitions(4,1,X,0);
		System.out.println(countAllPartitions(30));

	}
	
	public static void generatePartitions(int n, int k, int[] X, int index) {
		
		if(n==0) {
			for(int i =0; i<index; i++) {
				System.out.print(X[i]+" ");
			}
			System.out.println();
			return;
		}
		
		for(int i = k; i<=n; i++) {
			X[index] = i;
			generatePartitions(n-i, i, X, index+1);
		}
	}
	
	
	public static long countKPartitions(int n, int k) {
		
		long [][] f = new long [n+1][k+1];
		//create an (n+1) x (k+1) matrix of computed values, indices go from 1....n , and 1...k
		//we want the value of f[n][k] 
		
		
		//fill in known base case values
		for(int row=1; row <= n; row++) {
			for(int column=1; column <= k; column++) {
				if(row==column) {
		
					f[row][column] = 1;
				
				}
				
		}
		}
		
		//compute partitions quadratically
		for(int i = 1; i <= n; i++) {
			for(int j = 1; j <= k; j++) {
				if(f[i][j] == 0 && !(i==0 || j==0 || j>i)) {
					//need to compute f[i][j]
					f[i][j] = f[i-1][j-1] + f[i-j][j];
				}
				
			}
		}
		
		return f[n][k];
		
	}
	
	public static String countAllPartitions(int n) {
		
		//complexity O(n^3) worst case
		long result = 0;
		
		for(int i = 1; i <= n; i++) {
			result += countKPartitions(n, i);
		}
		
		String formatted = String.format("%,d", result);
		
		return formatted;
	}

}
