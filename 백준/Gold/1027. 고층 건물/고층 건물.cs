using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] heights = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int[] counts = new int[n];

for (int i=0;i<n;i++)
{
    double maxSlope = -double.MaxValue;

    for (int j=i+1;j<n;j++)
    {
        double slope = (double)(heights[j]-heights[i])/(j-i);
        
        if (slope > maxSlope)
        {
            maxSlope = slope;

            counts[i]++;
            counts[j]++;
        }
    }
}

writer.WriteLine(counts.Max());
