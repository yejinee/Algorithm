import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q9655 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());

        int[] winner = new int[1001];
        winner[1] = 1;
        winner[2] = 2;
        winner[3] = 1;

        for(int i =4;i<=n;i++){
            winner[i] = Math.min(winner[i-1], winner[i-3])+1;
        }

        if(winner[n]%2==1){
            System.out.println("SK");
        }else{
            System.out.println("CY");
        }
    }
}
