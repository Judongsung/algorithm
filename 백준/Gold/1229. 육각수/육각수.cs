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

int[] hexArray = hexs.ToArray();

for (int num=1;num<=n;num++)
{
    int min = dp[num];
    if (min == 1) continue;

    for (int j=0;j<hexArray.Length;j++)
    {
        int hex = hexArray[j];
        if (hex > num) break;

        int next = dp[num - hex] + 1;
        if (next < min) min = next;
        if (min == 2) break;
    }

    dp[num] = min;
}

writer.WriteLine(dp[n]);