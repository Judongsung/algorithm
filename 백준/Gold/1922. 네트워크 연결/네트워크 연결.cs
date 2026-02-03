using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int n = int.Parse(reader.ReadLine());
int m = int.Parse(reader.ReadLine());

PriorityQueue<Line, int> pq = new PriorityQueue<Line, int>();

for (int i=0;i<m;i++)
{
    int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

    if (input[0] == input[1]) continue;

    Line line = new Line(input);

    pq.Enqueue(line, line.cost);
}

int totalCost = 0;
HashSet<int> linked = new HashSet<int>();
linked.Add(1);

for (int i=0;i<n-1;i++)
{
    Line cur;
    bool containsP1;
    bool containsP2;

    List<Line> temp = new List<Line>();

    do
    {
        cur = pq.Dequeue();
        containsP1 = linked.Contains(cur.p1);
        containsP2 = linked.Contains(cur.p2);

        if (!containsP1 && !containsP2)
        {
            temp.Add(cur);
        }
    } while (!(containsP1 ^ containsP2));

    totalCost += cur.cost;
    
    if (!containsP1) linked.Add(cur.p1);
    else if (!containsP2) linked.Add(cur.p2);

    foreach (Line line in temp)
    {
        pq.Enqueue(line, line.cost);
    }
}

writer.WriteLine(totalCost);

struct Line
{
    public Line(int p1, int p2, int cost)
    {
        this.p1 = p1;
        this.p2 = p2;
        this.cost = cost;
    }

    public Line(int[] info)
    {
        this.p1 = info[0];
        this.p2 = info[1];
        this.cost = info[2];
    }

    public int p1;
    public int p2;
    public int cost;
}