using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int BASE = 10;

int n = int.Parse(reader.ReadLine());
List<long> result = new List<long>();

for (int i=0;i<BASE;i++)
{
    Dfs(i);
}
result.Sort();

if (n > result.Count) writer.WriteLine(-1);
else writer.WriteLine(result[n-1]); // 1-base to 0-base

void Dfs(long cur)
{
    result.Add(cur);

    for (int i=0;i<BASE;i++)
    {
        if (i >= cur % BASE) break;

        long next = cur * BASE + i;
        Dfs(next);
    }

    return;
}