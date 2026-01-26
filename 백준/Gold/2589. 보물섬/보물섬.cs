using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const char WALL ='W';
const char LAND = 'L';

(int dr, int dc)[] dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)};

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int rLen = input[0];
int cLen = input[1];

char[,] board = new char[rLen, cLen];

for (int r=0;r<rLen;r++)
{
    string row = reader.ReadLine().Trim();

    for (int c=0;c<cLen;c++)
    {
        board[r, c] = row[c];
    }
}

int maxDist = 0;

for (int r=0;r<rLen;r++)
{
    for (int c=0;c<cLen;c++)
    {
        if (board[r, c] == WALL) continue;
        
        int dist = BFS(r, c);

        if (dist > maxDist) maxDist = dist;
    }
}

writer.WriteLine(maxDist);

int BFS(int sr, int sc)
{
    int maxDist = 0;
    Queue<(int r, int c, int d)> queue = new Queue<(int r, int c, int d)>();
    HashSet<(int r, int c)> visited = new HashSet<(int r, int c)>();

    queue.Enqueue((sr, sc, 0));
    visited.Add((sr, sc));

    while (queue.Count > 0)
    {
        var cur = queue.Dequeue();

        if (cur.d > maxDist) maxDist = cur.d;
        
        foreach (var dir in dirs)
        {
            int nr = cur.r+dir.dr;
            int nc = cur.c+dir.dc;

            if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen || visited.Contains((nr, nc)) || board[nr, nc] == WALL) continue;

            queue.Enqueue((nr, nc, cur.d+1));
            visited.Add((nr, nc));
        }
    }

    return maxDist;
}