using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MAX_NUM = 1_000_000;
const int NOT_VISITED = -1;

int n = int.Parse(reader.ReadLine());
int[] nums = new int[n];
int[] counts = new int[MAX_NUM + 1];

for (int i=0;i<n;i++)
{
    int num = int.Parse(reader.ReadLine());
    nums[i] = num;
    counts[num]++;
}

int[] hitCache = new int[MAX_NUM + 1];
Array.Fill(hitCache, NOT_VISITED);

for (int i=0;i<n;i++)
{
    int num = nums[i];

    if (hitCache[num] != NOT_VISITED)
    {
        writer.WriteLine(hitCache[num]);
        continue;
    }

    int hit = 0;
    
    for (int j=1;j*j<=num;j++)
    {
        if (num % j == 0)
        {
            hit += counts[j];

            if (j * j != num)
            {
                hit += counts[num / j];
            }
        }
    }

    hitCache[num] = hit - 1;
    writer.WriteLine(hitCache[num]);
}