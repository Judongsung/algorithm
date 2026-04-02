using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
List<int> hexs = new List<int>();
int[] dp = new int[n+1];
Array.Fill(dp, int.MaxValue);
dp[0] = 0;

int cur = 0;
int i = 1;
while (true)
{
    cur = i * (i * 2 - 1);

    if (cur > n) break;

    hexs.Add(cur);
    dp[cur] = 1;
    i++;
}

for (int num=1;num<=n;num++)
{
    int min = dp[num];

    for (int j=0;j<hexs.Count;j++)
    {
        int hex = hexs[j];
        if (hex > num) break;

        int next = dp[num - hex] + 1;
        if (next < min) min = next;
    }

    dp[num] = min;
}

writer.WriteLine(dp[n]);