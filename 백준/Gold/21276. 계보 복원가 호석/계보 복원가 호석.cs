using System.Collections.Generic;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

SortedDictionary<string, Node> graph = new SortedDictionary<string, Node>();
int n = int.Parse(reader.ReadLine());
string[] names = reader.ReadLine().Split();

for (int i=0;i<n;i++)
{
    string name = names[i];
    graph[name] = new Node(name);
}

int m = int.Parse(reader.ReadLine());

for (int i=0;i<m;i++)
{
    string[] input = reader.ReadLine().Split();
    string descendant = input[0];
    string ancestor = input[1];

    Node dNode = graph[descendant];
    dNode.aNum++;
    graph[ancestor].descendants.Add(dNode);
}

List<string> firsts = new List<string>();
Queue<Node> q = new Queue<Node>();

foreach (Node node in graph.Values)
{
    if (node.aNum == 0)
    {
        firsts.Add(node.name);
        q.Enqueue(node);
    }
}

firsts.Sort();
writer.WriteLine(firsts.Count);

foreach (String name in firsts)
{
    writer.Write(name + " ");
}
writer.WriteLine();

while (q.Count > 0)
{
    Node cur = q.Dequeue();

    for (int i=0;i<cur.descendants.Count;i++)
    {
        Node dNode = cur.descendants[i];
        dNode.aNum--;

        if (dNode.aNum == 0)
        {
            cur.children.Add(dNode.name);
            q.Enqueue(dNode);
        }
    }
}

foreach (Node node in graph.Values)
{
    writer.Write($"{node.name} {node.children.Count} ");

    node.children.Sort();

    foreach (string child in node.children)
    {
        writer.Write(child+" ");
    }
    writer.WriteLine();
}

class Node
{
    public string name;
    public List<Node> descendants;
    public int aNum;
    public List<string> children;

    public Node(string name)
    {
        this.name = name;
        descendants = new List<Node>();
        aNum = 0;
        children = new List<string>();
    }
}