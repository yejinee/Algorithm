import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Q1655 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        // 최대힙
        PriorityQueue<Integer> maxQ = new PriorityQueue<>(Comparator.reverseOrder());
        // 최소힙
        PriorityQueue<Integer> minQ = new PriorityQueue<>();

        // 데이터 입력
        for (int i = 0; i < n; i++) {
            int data = Integer.parseInt(br.readLine());
            if (maxQ.size() == minQ.size()) {
                // 최대 Heap에 데이터 넣어줌
                maxQ.add(data);
                if (!minQ.isEmpty() && maxQ.peek() > minQ.peek()) {
                    //data change
                    minQ.add(maxQ.poll());
                    maxQ.add(minQ.poll());
                }
            } else {
                minQ.add(data);
                if (maxQ.peek() > minQ.peek()) {
                    minQ.add(maxQ.poll());
                    maxQ.add(minQ.poll());
                }
            }




            System.out.println(maxQ.peek()); // --> 1

        }


    }


}
