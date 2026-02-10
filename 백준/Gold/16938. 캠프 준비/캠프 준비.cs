using System.Collections;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int l = int.Parse(input[1]);
int r = int.Parse(input[2]);
int x = int.Parse(input[3]);
int maxBits = (int)Math.Pow(2, n);

input = reader.ReadLine().Split();
int[] sum = new int[maxBits];
int[] min = new int[maxBits];
int[] max = new int[maxBits];
Array.Fill(min, int.MaxValue);

for (int i=0;i<n;i++)
{
    int score = int.Parse(input[i]);
    
    for (int j=0;j<maxBits;j++)
    {
        if (((1<<i) & j) > 0)
        {
            sum[j] += score;

            if (score < min[j]) min[j] = score;
            if (score > max[j]) max[j] = score;
        }
    }
}

int result = 0;

for (int i=0;i<maxBits;i++)
{
    if (sum[i] >= l && sum[i] <= r && max[i]-min[i] >= x) result++;
}

writer.WriteLine(result);