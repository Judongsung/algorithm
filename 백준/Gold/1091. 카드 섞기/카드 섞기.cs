using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] target = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int[] shuffleWay = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

int[] start = new int[n];
int[] cur = new int[n];

for (int i=0;i<n;i++)
{
    start[i] = i;
    cur[i] = i;
}

int count = 0;
int[] next = new int[n];

while (!CompareTarget())
{
    for (int i=0;i<n;i++)
    {
        next[shuffleWay[i]] = cur[i];
    }
    count++;

    if (CompareArray(next, start, n))
    {
        writer.WriteLine(-1);
        return;
    }

    for (int i=0;i<n;i++)
    {
        cur[i] = next[i];
    }
}
writer.WriteLine(count);

bool CompareTarget()
{
    for (int i=0;i<n;i++)
    {
        if (target[cur[i]] != i % 3) return false;
    }
    return true;
}

bool CompareArray(int[] one, int[] other, int length)
{
    for (int i=0;i<length;i++)
    {
        if (one[i] != other[i]) return false;
    }
    return true;
}