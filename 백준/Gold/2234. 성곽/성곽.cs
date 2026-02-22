(int r, int c)[] dirs = {(0, -1), (-1, 0), (0, 1), (1, 0)};
int[] walls = {1, 2, 4, 8};

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int m = int.Parse(input[1]);

int[,] board = new int[m, n];

for (int i=0;i<m;i++)
{
    input = reader.ReadLine().Split();

    for (int j=0;j<n;j++)
    {
        board[i, j] = int.Parse(input[j]);
    }
}

bool[,] visited = new bool[m, n];
List<HashSet<(int r, int c)>> rooms = new List<HashSet<(int r, int c)>>();
List<HashSet<(int r, int c)>> nears = new List<HashSet<(int r, int c)>>();
int maxSize = 0;

for (int i=0;i<m;i++)
{
    for (int j=0;j<n;j++)
    {
        if (visited[i, j]) continue;

        var room = FindRoom(i, j, out var near);
        rooms.Add(room);
        nears.Add(near);

        if (room.Count > maxSize)
        {
            maxSize = room.Count;
        }
    }
}

writer.WriteLine(rooms.Count);
writer.WriteLine(maxSize);

int maxExpand = 0;

for (int i=0;i<rooms.Count-1;i++)
{
    for (int j=i+1;j<rooms.Count;j++)
    {
        if (rooms[i].Overlaps(nears[j]))
        {
            int expandSize = rooms[i].Count + rooms[j].Count;

            if (expandSize > maxExpand) maxExpand = expandSize;
        }
    }
}

writer.WriteLine(maxExpand);

HashSet<(int r, int c)> FindRoom(int sr, int sc, out HashSet<(int r, int c)> near)
{
    HashSet<(int r, int c)> room = new HashSet<(int r, int c)>();
    near = new HashSet<(int r, int c)>();

    Queue<(int r, int c)> q = new Queue<(int r, int c)>();
    q.Enqueue((sr, sc));
    visited[sr, sc] = true;

    while (q.Count > 0)
    {
        var cur = q.Dequeue();
        room.Add(cur);

        for (int i=0;i<dirs.Length;i++)
        {
            int nr = cur.r + dirs[i].r;
            int nc = cur.c + dirs[i].c;

            if (!IsPassable(board[cur.r, cur.c], walls[i]))
            {
                near.Add((nr, nc));
                continue;
            }

            if (visited[nr, nc]) continue;

            q.Enqueue((nr, nc));
            visited[nr, nc] = true;
        }
    }

    return room;
}

bool IsPassable(int land, int wall)
{
    if ((land & wall) == 0)
    {
        return true;
    }

    return false;
}