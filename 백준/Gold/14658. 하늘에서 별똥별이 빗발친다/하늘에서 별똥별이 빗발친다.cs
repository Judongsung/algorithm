using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int rlen = input[0];
int clen = input[1];
int tlen = input[2];
int n = input[3];
HashSet<(int x, int y)> points = new HashSet<(int x, int y)>();

for (int i=0;i<n;i++)
{
    int[] point = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    points.Add((point[0], point[1]));
}

int maxCount = 0;

foreach (var xBasis in points)
{
    foreach (var yBasis in points)
    {
        int count = 0;

        foreach (var other in points)
        {
            if (other.x >= xBasis.x && other.x <= xBasis.x+tlen && other.y >= yBasis.y && other.y <= yBasis.y+tlen) count++;
            
        }

        if (count > maxCount) maxCount = count;
    }

}

writer.WriteLine(n-maxCount);