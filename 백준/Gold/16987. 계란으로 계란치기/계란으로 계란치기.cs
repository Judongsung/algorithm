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

writer.WriteLine(find_max_broken(0));

int find_max_broken(int cur)
{
    if (cur == n) return 0;
    if (durabilities[cur] <= 0) return find_max_broken(cur+1);

    int maxBroken = 0;

    for (int i=0;i<n;i++)
    {
        if (durabilities[i] <= 0 || i == cur) continue;

        durabilities[cur] -= weights[i];
        durabilities[i] -= weights[cur];

        int broken = find_max_broken(cur+1);

        if (durabilities[cur] <= 0) broken++;
        if (durabilities[i] <= 0) broken++;

        if (broken > maxBroken) maxBroken = broken;

        durabilities[cur] += weights[i];
        durabilities[i] += weights[cur];
    }

    return maxBroken;
}

