using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

List<(int s, int e)> backwardEdges = new List<(int s, int e)>();

for (int i=0;i<m;i++)
{
    input = reader.ReadLine().Split();
    int s = int.Parse(input[0]) - 1; // 1-base to 0-base
    int e = int.Parse(input[1]) - 1;
    
    if (s > e) backwardEdges.Add((s, e));
}

List<int> divisors = GetDivisors(n);
divisors.Sort();

foreach (int d in divisors)
{
    bool isFail = false;

    foreach (var edge in backwardEdges)
    {
        if (edge.s / d != edge.e / d)
        {
            isFail = true;
            break;
        }
    }

    if (!isFail)
    {
        writer.WriteLine(n / d);
        break;
    }
}

List<int> GetDivisors(int num)
{
    List<int> divisors = new List<int>();

    for (int i=1;i*i<=num;i++)
    {
        if (num % i == 0)
        {
            divisors.Add(i);

            if (i * i != num)
            {
                divisors.Add(num / i);
            }
        }
    }

    return divisors;
}