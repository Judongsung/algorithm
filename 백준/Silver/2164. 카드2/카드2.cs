using System.Collections;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
Queue<int> queue = new Queue<int>(n);

for(int i=1;i<=n;i++)
{
    queue.Enqueue(i);
}

while(queue.Count > 1)
{
    queue.Dequeue();
    queue.Enqueue(queue.Dequeue());
}

writer.WriteLine(queue.Peek());