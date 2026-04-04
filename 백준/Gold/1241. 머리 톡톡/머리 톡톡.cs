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

int[] hits = new int[MAX_NUM + 1];

for (int num=0;num<=MAX_NUM;num++)
{
    int count = counts[num];
    if (count == 0) continue;

    for (int multi=num;multi<=MAX_NUM;multi+=num)
    {
        hits[multi] += count;
    }
}

for (int i=0;i<n;i++)
{
    writer.WriteLine(hits[nums[i]] - 1);
}