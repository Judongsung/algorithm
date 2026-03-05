using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);
int k = int.Parse(input[2]);

input = reader.ReadLine().Split();
int[] pos = new int[k];

for (int i=0;i<k;i++)
{
    pos[i] = int.Parse(input[i]);
}

int min = 0;
int max = n;
int maxDist = 0;

while (min <= max)
{
    int avg = (min + max + 1) / 2;
    int l = 0;
    int count = 1;

    for (int r=1;r<k;r++)
    {
        if (pos[r] - pos[l] >= avg)
        {
            count++;
            l = r;
        }
    }

    if (count < m)
    {
        max = avg-1;
    }
    else
    {
        maxDist = avg;
        min = avg+1;
    }
}

{
    int l = -1;
    int count = 0;

    for (int r=0;r<k;r++)
    {
        if (count == 0 || pos[r] - pos[l] >= maxDist)
        {
            writer.Write(1);
            count++;
            l = r;

            if (count == m)
            {
                for (int i=r+1;i<k;i++)
                {
                    writer.Write(0);
                }
                break;
            }
        }
        else
        {
            writer.Write(0);
        }
    }
}