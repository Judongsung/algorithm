using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
List<int> hexs = new List<int>();
int[] dp = new int[n+1];
Array.Fill(dp, 6);
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

int[] hexArray = hexs.ToArray();

foreach (int hex in hexArray)
{
    for (int num=hex;num<=n;num++)
    {
        if (hex > num) break;

        int next = dp[num - hex] + 1;
        if (next < dp[num]) dp[num] = next;
    }
}

writer.WriteLine(dp[n]);