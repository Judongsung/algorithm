using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

long n = long.Parse(reader.ReadLine());
int[] dice = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

if (n == 1)
{
    writer.WriteLine(dice.Sum() - dice.Max());
    return;
}

int[] minVisible = new int[3];

for (int i=0;i<3;i++)
{
    minVisible[i] = Math.Min(dice[i], dice[5-i]);
}

long result = minVisible.Min() * ((n-2) * (n-2) * 5 + (n-2) * 4);
result += (minVisible.Sum() - minVisible.Max()) * ((n-2) * 8 + 4);
result += (minVisible.Sum()) * 4;

writer.WriteLine(result);