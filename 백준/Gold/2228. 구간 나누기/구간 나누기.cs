using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MIN_NUM = -32768 * 100;

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

int[] nums = new int[n];

for (int i=0;i<n;i++)
{
    nums[i] = int.Parse(reader.ReadLine());
}

int[,] dp = new int[n, m+1];

for (int j=1;j<=m;j++)
{
    for (int i=0;i<n;i++)
    {
        dp[i, j] = MIN_NUM;

        if (i > 0 && dp[i-1, j] > dp[i, j])
        {
            dp[i, j] = dp[i-1, j];
        }

        int currentIntervalSum = 0;

        for (int k=i;k>=0;k--)
        {
            currentIntervalSum += nums[k];

            if (j == 1)
            {
                if (currentIntervalSum > dp[i, j])
                {
                    dp[i, j] = currentIntervalSum;
                }
            }
            else
            {
                if (k >= 2)
                {
                    int prevMax = dp[k-2, j-1];

                    if (prevMax != MIN_NUM && prevMax+currentIntervalSum > dp[i, j])
                    {
                        dp[i, j] = prevMax + currentIntervalSum;
                    }
                }
            }
        }
    }
}

writer.WriteLine(dp[n-1, m]);