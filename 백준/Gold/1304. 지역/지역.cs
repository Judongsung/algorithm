using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

List<int>[] graph = new List<int>[n];

for (int i=0;i<n;i++)
{
    graph[i] = new List<int>();

    if (i < n-1) graph[i].Add(i+1);
}

for (int i=0;i<m;i++)
{
    input = reader.ReadLine().Split();
    int s = int.Parse(input[0]) - 1; // 1-base to 0-base
    int e = int.Parse(input[1]) - 1;
    
    graph[s].Add(e);
}

List<int> divisors = GetDivisors(n);
divisors.Sort();

foreach (int d in divisors)
{
    bool isFail = false;

    for (int start=n-d;start>0;start-=d)
    {
        if (HasLowerWay(start))
        {
            isFail = true;
            break;
        }
    }

    if (!isFail)
    {
        writer.WriteLine(n / d);
        break;
    }
}

List<int> GetDivisors(int num)
{
    List<int> divisors = new List<int>();

    for (int i=1;i*i<=num;i++)
    {
        if (num % i == 0)
        {
            divisors.Add(i);

            if (i * i != num)
            {
                divisors.Add(num / i);
            }
        }
    }

    return divisors;
}

bool HasLowerWay(int start)
{
    Queue<int> queue = new Queue<int>();
    bool[] visited = new bool[n];
    queue.Enqueue(start);
    visited[start] = true;

    while (queue.Count != 0)
    {
        int cur = queue.Dequeue();

        foreach (int next in graph[cur])
        {
            if (visited[next]) continue;
            if (next < start) return true;

            queue.Enqueue(next);
            visited[next] = true;
        }
    }

    return false;
}