using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int l = int.Parse(input[1]);

int cur = 0;
(int s, int e)[] puddle = new (int s, int e)[n];
int result = 0;

for (int i=0;i<n;i++)
{
    input = reader.ReadLine().Split();
    puddle[i].s = int.Parse(input[0]);
    puddle[i].e = int.Parse(input[1]);
}

Array.Sort(puddle);

for (int i=0;i<n;i++)
{
    int start = puddle[i].s;
    int end = puddle[i].e;

    if (start > cur) cur = start;
    else if (cur > end) continue;

    int need = (end-cur) / l;
    if ((end-cur) % l != 0) need += 1;
    
    cur += need * l;
    result += need;
}

writer.WriteLine(result);