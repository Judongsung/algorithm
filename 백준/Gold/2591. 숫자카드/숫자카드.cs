using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int[] input = Array.ConvertAll(reader.ReadLine().ToCharArray(), x => x - '0');
int[] dp = new int[input.Length];
dp[0] = 1;
if (input.Length > 1)
{
    dp[1] = 1;
    if (input[1] != 0 && input[0] * 10 + input[1] <= 34) dp[1] = 2;
}

for (int i=2;i<input.Length;i++)
{
    if (input[i] != 0) dp[i] += dp[i-1];
    if (input[i] == 0 || (input[i-1] != 0 && input[i-1] * 10 + input[i] <= 34)) dp[i] += dp[i-2];
}

writer.WriteLine(dp[^1]);