using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int c = int.Parse(input[0]);
int n = int.Parse(input[1]);

int[] costs = new int[n];
int[] vals = new int[n];

for (int i=0;i<n;i++)
{
    input = reader.ReadLine().Split();
    costs[i] = int.Parse(input[0]);
    vals[i] = int.Parse(input[1]);
}

int[] dp = new int[c + vals.Max() + 1];
Array.Fill(dp, 100000);
dp[0] = 0;

for (int i=0;i<n;i++)
{
    dp[vals[i]] = costs[i];
}

for (int i=0;i<n;i++)
{
    int cost = costs[i];
    int val = vals[i];

    for (int j=0;j<c;j++)
    {
        int nextCost = dp[j] + cost;
        int nextVal = j + val;

        if (nextCost < dp[nextVal]) dp[nextVal] = nextCost;
    }
}

int result = int.MaxValue;

for (int i=c;i<dp.Length;i++)
{
    if (dp[i] < result) result = dp[i];
}

writer.WriteLine(result);