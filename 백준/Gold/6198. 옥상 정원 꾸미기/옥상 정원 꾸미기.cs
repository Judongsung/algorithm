using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int[] heights = new int[n];

for (int i=0;i<n;i++)
{
    heights[i] = int.Parse(reader.ReadLine());
}

long vision = 0;
Stack<int> stack = new Stack<int>();

for (int i=0;i<n;i++)
{
    while (stack.Count > 0 && heights[stack.Peek()] <= heights[i])
    {
        vision += i-1 - stack.Pop();
    }

    stack.Push(i);
}

while (stack.Count > 0)
{
    vision += n-1 - stack.Pop();
}

writer.WriteLine(vision);