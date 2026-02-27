const string IMPOSSIBLE = "IMPOSSIBLE";
const int FAIL = -1;
const int NULL = 0;
const int ENDPOINT = 1;
const int WALL = 2;
const int LINE = 3;

(int x, int y)[] dirs = {(0, -1), (0, 1), (-1, 0), (1, 0)};

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

List<Point> pPair1 = new List<Point>();

for (int i=0;i<2;i++)
{
    input = reader.ReadLine().Split();

    int x = int.Parse(input[0]);
    int y = int.Parse(input[1]);
    Point p = new Point(ENDPOINT, x, y);

    pPair1.Add(p);
}

List<Point> pPair2 = new List<Point>();

for (int i=0;i<2;i++)
{
    input = reader.ReadLine().Split();

    int x = int.Parse(input[0]);
    int y = int.Parse(input[1]);
    Point p = new Point(ENDPOINT, x, y);

    pPair2.Add(p);
}

int dist1 = FindMinDistOfTwo(pPair1, pPair2);
int dist2 = FindMinDistOfTwo(pPair2, pPair1);

if (dist1 != FAIL && dist2 != FAIL) writer.WriteLine(dist1 < dist2? dist1: dist2);
else if (dist1 != FAIL) writer.WriteLine(dist1);
else if (dist2 != FAIL) writer.WriteLine(dist2);
else writer.WriteLine(IMPOSSIBLE);

int FindMinDistOfTwo(List<Point> pairOne, List<Point> pairTwo)
{
    List<Point> first = FindMinPath(pairOne, pairTwo);

    if (first.Count == 0) return FAIL;

    List<Point> second = FindMinPath(pairTwo, first);
    
    if (second.Count == 0) return FAIL;

    return first.Count + second.Count - 2;
}

List<Point> FindMinPath(List<Point> targets, List<Point> walls)
{
    Point[,] pBoard = new Point[n+1, m+1];

    foreach (var w in walls)
    {
        Point p = w;
        p.type = WALL;
        pBoard[w.x, w.y] = p;
    }

    Queue<Point> queue = new Queue<Point>();
    Point start = targets[0];
    start.prevX = ENDPOINT;
    start.prevY = ENDPOINT;
    Point end = targets[1];

    queue.Enqueue(start);
    pBoard[start.x, start.y] = start;

    while (queue.Count > 0)
    {
        Point cur = queue.Dequeue();

        foreach (var d in dirs)
        {
            int nx = cur.x + d.x;
            int ny = cur.y + d.y;

            if (nx < 0 || nx > n || ny < 0 || ny > m || pBoard[nx, ny].type != NULL) continue;

            if (nx == end.x && ny == end.y)
            {
                List<Point> path = new List<Point>();
                Point p = new Point(LINE, nx, ny);
                p.prevX = cur.x;
                p.prevY = cur.y;
                path.Add(p);

                while (p.type != ENDPOINT)
                {
                    p = pBoard[p.prevX, p.prevY];
                    path.Add(p);
                }
                
                return path;
            }

            Point np = new Point(LINE, nx, ny);
            np.prevX = cur.x;
            np.prevY = cur.y;

            queue.Enqueue(np);
            pBoard[nx, ny] = np;
        }
    }

    return new List<Point>();
}

struct Point
{
    public int type; // NULL
    public int x;
    public int y;
    public int prevX;
    public int prevY;

    public Point(int type, int x, int y)
    {
        this.type = type;
        this.x = x;
        this.y = y;
        prevX = 0;
        prevY = 0;
    }
}