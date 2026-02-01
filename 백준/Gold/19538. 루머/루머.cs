using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
Node[] graph = new Node[n+1];

for (int i=1;i<=n;i++)
{
    graph[i] = new Node();
}

for (int i=1;i<=n;i++)
{
    int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

    for (int j=0;j<input.Length-1;j++)
    {
        graph[i].Connect(graph[input[j]]);
    }
}

int m = int.Parse(reader.ReadLine());
int[] spreaders = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

Queue<(Node node, int time)> queue = new Queue<(Node node, int time)>();

foreach (int s in spreaders)
{
    Node node = graph[s];
    queue.Enqueue((node, 0));
    node.Work(0);
}

while (queue.Count > 0)
{
    var cur = queue.Dequeue();

    cur.node.Work(cur.time);

    foreach (Node linked in cur.node.GetLinkedNodes())
    {
        if (linked.Spread())
        {
            queue.Enqueue((linked, cur.time+1));
        }
    }
}

for (int i=1;i<=n;i++)
{
    writer.Write(graph[i].GetStartTime()+" ");
}

class Node
{
    int workingLinks = 0;
    bool isQueued = false;
    int startTime = -1;
    int threshold = 0;

    List<Node> linkedNodes;

    public Node()
    {
        linkedNodes = new List<Node>();
    }

    public void Connect(Node linked)
    {
        linkedNodes.Add(linked);
        threshold = (linkedNodes.Count+1)/2;
    }

    public bool Spread()
    {
        if (isQueued) return false;

        workingLinks++;

        if (workingLinks >= threshold)
        {
            isQueued = true;
        }

        return isQueued;
    }

    public void Work(int time)
    {
        if (!isQueued) isQueued = true;
        startTime = time;
    }

    public List<Node> GetLinkedNodes()
    {
        return linkedNodes;
    }

    public int GetStartTime()
    {
        return startTime;
    }
}