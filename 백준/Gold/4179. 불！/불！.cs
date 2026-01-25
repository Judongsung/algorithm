using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const char CH_WALL = '#';
const char CH_PATH = '.';
const char CH_START = 'J';
const char CH_FIRE = 'F';
const int WALL = -1;
const int NOT_CHECKED = int.MaxValue;
const string IMPOSSIBLE = "IMPOSSIBLE";

(int dr, int dc)[] dirs = {(-1, 0), (0, 1), (0, -1), (1, 0)};

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int rLen = input[0];
int cLen = input[1];

int[,] board = new int[rLen, cLen];
int startR = 0;
int startC = 0;
Queue<(int r, int c)> fireQ = new Queue<(int r, int c)>();

for (int r=0;r<rLen;r++)
{
    string row = reader.ReadLine().Trim();

    for (int c=0;c<cLen;c++)
    {
        if (row[c] == CH_START)
        {
            startR = r;
            startC = c;
            board[r, c] = NOT_CHECKED;
        }
        else if (row[c] == CH_FIRE)
        {
            fireQ.Enqueue((r, c));
            board[r, c] = 0;
        }
        else if (row[c] == CH_WALL)
        {
            board[r, c] = WALL;
        }
        else
        {
            board[r, c] = NOT_CHECKED;
        }
    }
}

while (fireQ.Count > 0)
{
    var cur = fireQ.Dequeue();

    foreach (var dir in dirs)
    {
        int nr = cur.r+dir.dr;
        int nc = cur.c+dir.dc;

        if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen || board[nr, nc] != NOT_CHECKED) continue;

        board[nr, nc] = board[cur.r, cur.c]+1;
        fireQ.Enqueue((nr, nc));
    }
}

Queue<(int r, int c, int t)> escapeQ = new Queue<(int r, int c, int t)>();
escapeQ.Enqueue((startR, startC, 0));
bool[,] visited = new bool[rLen, cLen];
bool isSuccess = false;
int escapeTime = 0;

while (escapeQ.Count > 0 && !isSuccess)
{
    var cur = escapeQ.Dequeue();
    int nt = cur.t+1;

    foreach (var dir in dirs)
    {
        int nr = cur.r+dir.dr;
        int nc = cur.c+dir.dc;

        if (nr < 0 || nr >= rLen || nc < 0 || nc >= cLen)
        {
            isSuccess = true;
            escapeTime = nt;
            break;
        }

        if (board[nr, nc] == WALL || board[nr, nc] <= nt || visited[nr, nc]) continue;

        escapeQ.Enqueue((nr, nc, nt));
        visited[nr, nc] = true;
    }
}

writer.WriteLine(isSuccess? escapeTime:IMPOSSIBLE);