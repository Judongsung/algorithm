using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

int[] nums = new int[n];

for (int i=0;i<n;i++)
{
    nums[i] = int.Parse(reader.ReadLine());
}

Array.Sort(nums);

if (m == 0)
{
    writer.WriteLine(0);
    return;
}

int l = 0;
int minDiff = int.MaxValue;

for (int r=1;r<n;r++)
{
    int diff = nums[r] - nums[l];

    while (diff >= m)
    {
        if (diff == m)
        {
            writer.WriteLine(diff);
            return;
        }

        if (diff < minDiff)
        {
            minDiff = diff;
        }

        l++;
        diff = nums[r] - nums[l];
    }
}

writer.WriteLine(minDiff);