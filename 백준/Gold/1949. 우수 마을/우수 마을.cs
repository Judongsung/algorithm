using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
Node[] graph = new Node[n];

string[] input = reader.ReadLine().Split();

for (int i=0;i<n;i++)
{
    int population = int.Parse(input[i]);
    graph[i] = new Node(population);
}

for (int i=0;i<n-1;i++)
{
    input = reader.ReadLine().Split();
    int one = int.Parse(input[0]) - 1; // 1-base to 0-base
    int other = int.Parse(input[1]) - 1;

    graph[one].Connect(other);
    graph[other].Connect(one);
}

int[,] dp = new int[n, 2];
Dfs(0, -1);

writer.WriteLine(Math.Max(dp[0, 0], dp[0, 1]));

void Dfs(int cur, int prev)
{
    dp[cur, 1] = graph[cur].population;

    foreach (int next in graph[cur].connected)
    {
        if (next == prev) continue;

        Dfs(next, cur);
        dp[cur, 0] += Math.Max(dp[next, 0], dp[next, 1]);
        dp[cur, 1] += dp[next, 0];
    }
}

struct Node
{
    public int population;
    public List<int> connected;

    public Node(int population)
    {
        this.population = population;
        connected = new List<int>();
    }

    public void Connect(int nodeNum)
    {
        connected.Add(nodeNum);
    }
}
