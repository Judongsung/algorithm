using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] scores = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

int[,] scoreDiffs = new int[n, n];

for (int i=0;i<n;i++)
{
    int max = scores[i];
    int min = scores[i];

    for (int j=i;j<n;j++)
    {
        int right = scores[j];

        if (right > max) max = right;
        else if (right < min) min = right;

        scoreDiffs[i, j] = max-min;
    }
}

int[] dp = new int[n];
dp[0] = 0;

for (int i=1;i<n;i++)
{
    int maxSum = scoreDiffs[0, i];

    for (int j=0;j<i;j++)
    {
        int sum = dp[j]+scoreDiffs[j+1, i];

        if (sum > maxSum) maxSum = sum;
    }

    dp[i] = maxSum;
}

writer.WriteLine(dp[n-1]);