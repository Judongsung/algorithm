using System.Text;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int NOT_MOVABLE = 0;
const int MOVABLE = 1;
const int GOAL = 2;
const int NOT_REACHED = -1;

(int dr, int dc)[] dirs = {(-1, 0), (0, 1), (1, 0), (0, -1)};

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int rLen = input[0];
int cLen = input[1];
int[,] matrix = new int[rLen, cLen];
int[,] distances = new int[rLen, cLen];
int rGoal = 0;
int cGoal = 0;

for (int r=0;r<rLen;r++)
{
    input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    
    for (int c=0;c<cLen;c++)
    {
        matrix[r, c] = input[c];

        if (input[c] == GOAL)
        {
            rGoal = r;
            cGoal = c;
        }

        if (matrix[r, c] == NOT_MOVABLE)
        {
            distances[r, c] = NOT_MOVABLE;
            continue;
        }
        distances[r, c] = NOT_REACHED;
    }
}

Queue<(int r, int c, int d)> queue = new Queue<(int, int, int)>();
queue.Enqueue((rGoal, cGoal, 0));
distances[rGoal, cGoal] = 0;

while (queue.Count > 0)
{
    var cur = queue.Dequeue();

    foreach (var dir in dirs)
    {
        int nr = cur.r+dir.dr;
        int nc = cur.c+dir.dc;

        if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen) continue;

        if (distances[nr, nc] == NOT_REACHED)
        {
            distances[nr, nc] = cur.d+1;
            queue.Enqueue((nr, nc, cur.d+1));
        }
    }
}

StringBuilder sb = new StringBuilder();

for (int r=0;r<rLen;r++)
{
    for (int c=0;c<cLen;c++)
    {
        sb.Append(distances[r, c]);
        sb.Append(' ');
    }

    sb.AppendLine();
}

writer.Write(sb);