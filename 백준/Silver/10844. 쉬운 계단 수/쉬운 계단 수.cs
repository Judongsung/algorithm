using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MOD = 1_000_000_000;

int n = int.Parse(reader.ReadLine());

long[] dp = new long[10];

for (int i=1;i<=9;i++)
{
    dp[i] = 1;
}

long[] nextDp = new long[10];

for (int i=1;i<n;i++)
{
    nextDp[1] = (nextDp[1] + dp[0]) % MOD;

    for (int j=1;j<=8;j++)
    {
        nextDp[j-1] = (nextDp[j-1] + dp[j]) % MOD;
        nextDp[j+1] = (nextDp[j+1] + dp[j]) % MOD;
    }

    nextDp[8] = (nextDp[8] + dp[9]) % MOD;

    long[] temp = dp;
    dp = nextDp;
    nextDp = temp;

    Array.Fill(nextDp, 0);
}

long result = 0;

for (int i=0;i<10;i++)
{
    result = (result + dp[i]) % MOD;
}

writer.WriteLine(result);