using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int t = int.Parse(reader.ReadLine());

for (int i=0;i<t;i++)
{
    int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    int n = input[0];
    int m = input[1];
    
    long[,] dp = new long[n+1, m+1];


    for (int j=1;j<=m;j++) dp[1, j] = 1;
    
    for (int j=2;j<=n;j++)
    {
        long sum = 0;
        int p = 1;

        for (int k=1;k<=m;k++)
        {
            while (p*2 <= k)
            {
                sum += dp[j-1, p];
                p++;
            }

            dp[j, k] = sum;
        }
    }

    long result = 0;
    
    for (int j=1;j<=m;j++) result += dp[n, j];

    writer.WriteLine(result);
}
