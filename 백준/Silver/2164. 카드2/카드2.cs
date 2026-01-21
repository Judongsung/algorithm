using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
LinkedList<int> deque = new LinkedList<int>(Enumerable.Range(1, n));

while(deque.Count > 1)
{
    deque.RemoveFirst();
    deque.AddLast(deque.First.Value);
    deque.RemoveFirst();
}

writer.WriteLine(deque.First.Value.ToString());