using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MOD = 9901;

int n = int.Parse(reader.ReadLine());
int[] cur = {1, 1, 1};
int[] prev = new int[3];

for (int i=1;i<n;i++)
{
    int[] temp = cur;
    cur = prev;
    prev = temp;

    cur[0] = (prev[0] + prev[1] + prev[2])%MOD;
    cur[1] = (prev[0] + prev[2])%MOD;
    cur[2] = (prev[0] + prev[1])%MOD;
}

writer.WriteLine(cur.Sum()%MOD);