using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

(int dr, int dc)[] dirs = {(0, 1), (1, 0)};

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);
int k = int.Parse(reader.ReadLine());
HashSet<(int r1, int c1, int r2, int c2)> disabled = new HashSet<(int r1, int c1, int r2, int c2)>();

for (int i=0;i<k;i++)
{
    int[] info = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

    if (info[0] > info[2] || info[1] > info[3])
    {
        disabled.Add((info[2], info[3], info[0], info[1]));
        continue;
    }
    disabled.Add((info[0], info[1], info[2], info[3]));
}

ulong[,] dp = new ulong[n+1, m+1];
Queue<(int r, int c)> queue = new Queue<(int r, int c)>();
bool[,] visited = new bool[n+1, m+1];

dp[0, 0] = 1;
queue.Enqueue((0, 0));

while (queue.Count > 0)
{
    var cur = queue.Dequeue();

    foreach (var d in dirs)
    {
        int nr = cur.r+d.dr;
        int nc = cur.c+d.dc;

        if (nr < 0 || nr > n || nc < 0 || nc > m) continue;

        if (disabled.Contains((cur.r, cur.c, nr, nc))) continue;

        dp[nr, nc] += dp[cur.r, cur.c];

        if (visited[nr, nc]) continue;

        queue.Enqueue((nr, nc));
        visited[nr, nc] = true;
    }
}

writer.WriteLine(dp[n, m]);