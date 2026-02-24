const char EMPTY = '.';
const char WALL = '#';
const char START = '@';
const char FIRE = '*';

const int NOT_VISITED = 1000_000;
const int FAIL = -1;
const string IMPOSSIBLE = "IMPOSSIBLE";

(int r, int c)[] dirs = {(-1, 0), (1, 0), (0, -1), (0, 1)};

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int t = int.Parse(reader.ReadLine());

for (int i=0;i<t;i++)
{
    string[] input = reader.ReadLine().Split();
    int cLen = int.Parse(input[0]);
    int rLen = int.Parse(input[1]);

    string[] board = new string[rLen];
    int startR = 0;
    int startC = 0;

    for (int j=0;j<rLen;j++)
    {
        board[j] = reader.ReadLine().Trim();

        for (int k=0;k<cLen;k++)
        {
            if (board[j][k] == START)
            {
                startR = j;
                startC = k;
            }
        }
    }

    int result = FindEscapeTime(board, rLen, cLen, startR, startC);
    writer.WriteLine(result == FAIL? IMPOSSIBLE : result);
}

int FindEscapeTime(string[] board, int rLen, int cLen, int startR, int startC)
{
    if (startR == 0 || startR == rLen-1 || startC == 0 || startC == cLen-1) return 1;

    int[,] fBoard = CreateFireBoard(board, rLen, cLen);
    Queue<(int r, int c, int time)> queue = new Queue<(int r, int c, int time)>();
    bool[,] visited = new bool[rLen, cLen];
    queue.Enqueue((startR, startC, 0));
    visited[startR, startC] = true;

    while (queue.Count > 0)
    {
        var cur = queue.Dequeue();
        int nt = cur.time + 1;

        foreach (var d in dirs)
        {
            int nr = cur.r + d.r;
            int nc = cur.c + d.c;

            if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen || board[nr][nc] == WALL || visited[nr, nc]) continue;

            if (fBoard[nr, nc]  <= nt) continue;

            if (nr == 0 || nr == rLen-1 || nc == 0 || nc == cLen-1) return nt+1;

            queue.Enqueue((nr, nc, nt));
            visited[nr, nc] = true;
        }
    }

    return FAIL;
}

int[,] CreateFireBoard(string[] board, int rLen, int cLen)
{
    int[,] fBoard = new int[rLen, cLen];
    Queue<(int r, int c, int time)> queue = new Queue<(int r, int c, int time)>();

    for (int i=0;i<rLen;i++)
    {
        for (int j=0;j<cLen;j++)
        {
            if  (board[i][j] == FIRE)
            {
                queue.Enqueue((i, j, 0));
                fBoard[i, j] = 0;
            }
            else fBoard[i, j] = NOT_VISITED;
        }
    }

    while (queue.Count > 0)
    {
        var cur = queue.Dequeue();
        int nt = cur.time + 1;

        foreach (var d in dirs)
        {
            int nr = cur.r + d.r;
            int nc = cur.c + d.c;

            if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen || board[nr][nc] == WALL || fBoard[nr, nc] != NOT_VISITED) continue;

            queue.Enqueue((nr, nc, nt));
            fBoard[nr, nc] = nt;
        }
    }

    return fBoard;
}