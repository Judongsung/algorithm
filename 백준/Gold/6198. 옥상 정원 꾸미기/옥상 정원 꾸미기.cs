using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] heights = new int[n];

for (int i=0;i<n;i++)
{
    heights[i] = int.Parse(reader.ReadLine());
}

int maxIdx = n;
int maxHeight = 0;
long vision = 0;

for (int i=n-1;i>=0;i--)
{
    int cur = heights[i];

    if (cur > maxHeight)
    {
        vision += n-1 - i;
        maxHeight = cur;
        maxIdx = i;

        continue;
    }

    if (cur == maxHeight)
    {
        vision += maxIdx-1 - i;
        maxIdx = i;

        continue;
    }
    
    int blocked = maxIdx;

    for (int j=i+1;j<maxIdx;j++)
    {
        if (heights[j] >= cur)
        {
            blocked = j;
            break;
        }
    }
    
    vision += blocked-1 - i;
}

writer.WriteLine(vision);