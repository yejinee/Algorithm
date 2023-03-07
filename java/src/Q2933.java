import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Q2933 {
    static class Loc {
        int x;
        int y;

        public Loc(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static int r;
    static int c;
    static char[][] board;
    static int[][] cluster;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] inputs = br.readLine().split(" ");

        r = Integer.parseInt(inputs[0]);
        c = Integer.parseInt(inputs[1]);

        board = new char[r][c];

        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for (int j = 0; j < c; j++) {
                board[i][j] = line.charAt(j);
            }
        }
        int n = Integer.parseInt(br.readLine());
        String[] heights = br.readLine().split(" ");


        for (int i = 0; i < heights.length; i++) {
            int h = Integer.parseInt(heights[i]);
            // 1. 미네랄 제거
            removeMineral(h, i % 2 == 0 ? 0 : 1);
            // 2. 클러스터 확인
            findcluster();
        }
        // print result
        for (int i = 0; i < r; i++) {
            System.out.println(board[i]);
        }
    }

    private static void removeMineral(int h, int direction) {
        // 짝수 => 왼쪽에서부터 던짐
        if (direction == 0) {
            for (int col = 0; col < c; col++) {
                if (board[r - h][col] == 'x') {
                    board[r - h][col] = '.';
                    return;
                }
            }
        } else {    // 짝수 => 오른쪽에서부터 던짐
            for (int col = c - 1; col >= 0; col--) {
                if (board[r - h][col] == 'x') {
                    board[r - h][col] = '.';
                    return;
                }
            }
        }
    }

    private static void findcluster() {
        cluster = new int[r][c];
        int cluster_no = 1;

        // 3. 모든 미네랄에 대해서 bfs로 클러스터 확인
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (board[i][j] == 'x' && cluster[i][j] == 0) {
                    // 4. 떠있는 클러스터를 확인
                    if (checkCluster(i, j, cluster_no)) {
                        return;
                    }
                    cluster_no++;
                }
            }
        }
    }

    private static boolean checkCluster(int i, int j, int clusterNo) {
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};

        int lowest = -1;
        Queue<Loc> q = new LinkedList<>();
        ArrayList<Loc> cluster_info = new ArrayList<>();

        q.add(new Loc(i, j));
        cluster[i][j] = clusterNo;

        while (!q.isEmpty()) {
            Loc now = q.poll();
            lowest = Math.max(lowest, now.x);

            for (int k = 0; k < 4; k++) {
                int nx = now.x + dx[k];
                int ny = now.y + dy[k];

                if (nx < 0 || ny < 0 || nx >= r || ny >= c) continue;

                if (cluster[nx][ny] == 0 && board[nx][ny] == 'x') {
                    cluster[nx][ny] = clusterNo;
                    q.add(new Loc(nx, ny));
                }
            }
            cluster_info.add(now);
        }
        // 공중에 떠있는 경우
        if (lowest != r - 1) {
            fallCluster(cluster_info);
            return true;
        }
        return false;
    }

    private static void fallCluster(ArrayList<Loc> clusterInfo) {

        for (Loc loc : clusterInfo) {
            board[loc.x][loc.y] = '.';
        }
        int moveheight = 1;
        Loop1 :
        for (int h = 1; h < r; h++) {
            for (Loc loc : clusterInfo) {

                if (loc.x + h == r || board[loc.x + h][loc.y] == 'x') {
                    moveheight = h - 1;
                    break Loop1;
                }
            }
        }

        for (Loc loc : clusterInfo) {
            board[loc.x + moveheight][loc.y] = 'x';
//            System.out.println(loc.x + moveheight + "   " + loc.y);
        }
    }
}