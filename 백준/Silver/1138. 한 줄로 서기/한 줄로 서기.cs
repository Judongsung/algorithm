using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] people = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int[] line = Enumerable.Repeat(0, n).ToArray();

for (int i=0;i<n;i++)
{
    int leftCount = people[i];
    int count = 0;

    for (int j=0;j<n;j++)
    {
        if (line[j] == 0)
        {
            if (count == leftCount)
            {
                line[j] = i+1;
                break;
            }
            count += 1;
        }

    }
}

foreach (int p in line)
{
    writer.Write(p+" ");
}