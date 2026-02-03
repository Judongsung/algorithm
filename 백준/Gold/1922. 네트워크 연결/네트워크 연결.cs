using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int m = int.Parse(reader.ReadLine());

List<(int node, int cost)>[] graph = new List<(int node, int cost)>[n+1];
for (int i=1;i<=n;i++) graph[i] = new List<(int node, int cost)>();

for (int i=0;i<m;i++)
{
    int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    int p1 = input[0];
    int p2 = input[1];
    int cost = input[2];

    if (p1 == p2) continue;
    
    graph[p1].Add((p2, cost));
    graph[p2].Add((p1, cost));
}

PriorityQueue<int, int> pq = new PriorityQueue<int, int>();
bool[] visited = new bool[n+1];
int totalCost = 0;
int linkedCount = 0;

pq.Enqueue(1, 0);

while (linkedCount < n && pq.Count > 0)
{
    pq.TryDequeue(out int node, out int cost);

    if (visited[node]) continue;

    totalCost += cost;
    visited[node] = true;
    linkedCount++;
    
    foreach (var next in graph[node])
    {
        if (visited[next.node]) continue;

        pq.Enqueue(next.node, next.cost);
    }
}

writer.WriteLine(totalCost);