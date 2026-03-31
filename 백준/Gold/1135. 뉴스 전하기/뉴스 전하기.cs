using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int ROOT = -1;

int n = int.Parse(reader.ReadLine());
string[] input = reader.ReadLine().Split();

List<int>[] graph = new List<int>[n];

for (int i=0;i<n;i++)
{
    graph[i] = new List<int>();
    int upper = int.Parse(input[i]);

    if (upper == ROOT) continue;

    graph[upper].Add(i);
}

int result = solve(0);
writer.WriteLine(result);

int solve(int cur)
{
    List<int> lowers = graph[cur];

    if (lowers.Count == 0) return 0;

    PriorityQueue<int, int> nextTimes = new PriorityQueue<int, int>();

    foreach (int lower in lowers)
    {
        int nextTime = solve(lower);
        nextTimes.Enqueue(nextTime, -nextTime);
    }

    int maxTime = 0;

    for (int i=0;i<lowers.Count;i++)
    {
        int nextEndTime = nextTimes.Dequeue() + i;
        if (nextEndTime > maxTime) maxTime = nextEndTime;
    }

    return maxTime + 1;
}