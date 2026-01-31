using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int ROW = 5;
const int COL = 5;
const int LENGTH = 6;

(int dr, int dc)[] dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)};

char[,] board = new char[ROW, COL];

for (int r=0;r<ROW;r++)
{
    char[] line = Array.ConvertAll(reader.ReadLine().Trim().Split(), char.Parse);
    
    for (int c=0;c<COL;c++)
    {
        board[r, c] = line[c];
    }
}

Queue<(int r, int c, string s)> queue = new Queue<(int r, int c, string s)>();
HashSet<string>[,] visited = new HashSet<string>[ROW, COL];

for (int r=0;r<ROW;r++)
{
    for (int c=0;c<COL;c++)
    {
        string start = board[r, c].ToString();
        visited[r, c] = new HashSet<string>();

        queue.Enqueue((r, c, start));
        visited[r, c].Add(start);
    }
}

HashSet<string> result = new HashSet<string>();

while (queue.Count > 0)
{
    var cur = queue.Dequeue();

    foreach (var d in dirs)
    {
        int nr = cur.r+d.dr;
        int nc = cur.c+d.dc;

        if (nr < 0 || nr >= ROW || nc < 0 || nc >= COL) continue;

        string ns = cur.s+board[nr, nc];

        if (visited[nr, nc].Contains(ns)) continue;

        if (ns.Length == LENGTH)
        {
            result.Add(ns);
            continue;
        }

        queue.Enqueue((nr, nc, ns));
        visited[nr, nc].Add(ns);
    }
}

writer.Write(result.Count);