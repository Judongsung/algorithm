(int r, int c)[] dirs = {(0, -1), (-1, 0), (0, 1), (1, 0)};
int[] walls = {1, 2, 4, 8};

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);
int[,] graph = new int[n+1,n+1];

for (int i=1;i<=n;i++)
{
    for (int j=1;j<=n;j++)
    {
        graph[i, j] = 101;
    }
}

for (int i=0;i<m;i++)
{
    input = reader.ReadLine().Split();
    int one = int.Parse(input[0]);
    int other = int.Parse(input[1]);

    graph[one, other] = 1;
    graph[other, one] = 1;
}

for (int mid=1;mid<=n;mid++)
{
    for (int start=1;start<=n;start++)
    {
        for (int end=1;end<=n;end++)
        {
            if (start == end) continue;

            if (graph[start, mid] + graph[mid, end] < graph[start, end]) graph[start, end] = graph[start, mid] + graph[mid, end];
        }
    }
}

int[] kbs = new int[n+1];

for (int i=1;i<=n;i++)
{
    for (int j=i+1;j<=n;j++)
    {
        kbs[i] += graph[i, j];
        kbs[j] += graph[i, j];
    }
}

int minId = 0;
int minKb = int.MaxValue;

for (int i=1;i<=n;i++)
{
    if (kbs[i] < minKb)
    {
        minId = i;
        minKb = kbs[i];
    }
}

writer.WriteLine(minId);