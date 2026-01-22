using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int POP = 0;

int n = int.Parse(reader.ReadLine());
PriorityQueue<int, int> pq = new PriorityQueue<int, int>();

for(int i=0;i<n;i++)
{
    int input = int.Parse(reader.ReadLine());
    if(input == POP)
    {
        if(pq.Count == 0)
        {
            writer.WriteLine(0);
        }
        else
        {
            writer.WriteLine(pq.Peek());
            pq.Dequeue();
        }
    }
    else
    {
        pq.Enqueue(input, input);
    }
}