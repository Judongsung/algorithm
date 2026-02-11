using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] durabilities = new int[n];
int[] weights = new int[n];

for (int i=0;i<n;i++)
{
    string[] egg = reader.ReadLine().Split();
    durabilities[i] = int.Parse(egg[0]);
    weights[i] = int.Parse(egg[1]);
}

writer.WriteLine(find_max_broken(durabilities, weights, 0));

int find_max_broken(int[] d, int[] w, int cur)
{
    if (cur == n) return 0;
    if (d[cur] <= 0) return find_max_broken(d, w, cur+1);

    int maxBroken = 0;

    for (int i=0;i<n;i++)
    {
        if (d[i] <= 0 || i == cur) continue;

        int[] newD = (int[]) d.Clone();
        int[] newW = (int[]) w.Clone();

        newD[cur] -= newW[i];
        newD[i] -= newW[cur];

        int broken = find_max_broken(newD, newW, cur+1);

        if (newD[cur] <= 0) broken++;
        if (newD[i] <= 0) broken++;

        if (broken > maxBroken) maxBroken = broken;
    }

    return maxBroken;
}

