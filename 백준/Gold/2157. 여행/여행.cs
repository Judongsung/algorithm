using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int n = input[0];
int m = input[1];
int k = input[2];
int[,] graph = new int[n, n];
int[,] dp = new int[n, m+1];

for (int i=0;i<k;i++)
{
    input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    int from = input[0]-1; // 1-base to 0-base
    int to = input[1]-1;
    int score = input[2];

    if (from > to) continue;

    if (graph[from, to] == 0 || score > graph[from, to])
    {
        graph[from, to] = score;
        
        if (from == 0) dp[to, 1] = score;
    }
}



for (int from=0;from<n;from++)
{
    for (int to=0;to<n;to++)
    {
        if (graph[from, to] > 0)
        {
            for (int i=1;i<m;i++)
            {
                if (dp[from, i] == 0) continue;

                int score = dp[from, i]+graph[from, to];

                if (score > dp[to, i+1])
                    dp[to, i+1] = dp[from, i]+graph[from, to];
            }
        }
    }
}

int maxScore = 0;

for (int i=1;i<m;i++)
{
    if (dp[n-1, i] > maxScore) maxScore = dp[n-1, i];
}

writer.WriteLine(maxScore);