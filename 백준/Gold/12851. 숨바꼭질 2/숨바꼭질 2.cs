const int MAX_SIZE = 100_001;
const int TIME = 0;
const int NUM = 1;

Func<int, int>[] moves = {(int x) => x*2, (int x) => x+1, (int x) => x-1};

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int k = int.Parse(input[1]);

if (k <= n)
{
    writer.WriteLine(n - k);
    writer.WriteLine(1);
    return;
}

int[,] board = new int[MAX_SIZE, 2];
Queue<(int pos, int time)> queue = new Queue<(int pos, int time)>();

queue.Enqueue((n, 0));
board[n, TIME] = 0;
board[n, NUM] = 1;

while (queue.Count > 0)
{
    (int pos, int time) cur = queue.Dequeue();
    int nTime = cur.time + 1;
    
    if (board[k, TIME] > 0 && board[k, TIME] < nTime) break;

    foreach (var move in moves)
    {
        int nPos = move(cur.pos);

        if (nPos < 0 || nPos >= MAX_SIZE) continue;

        if (board[nPos, TIME] == 0 && board[nPos, NUM] == 0)
        {
            board[nPos, TIME] = nTime;
            board[nPos, NUM] = board[cur.pos, NUM];
            queue.Enqueue((nPos, nTime));
        }
        else if (board[nPos, TIME] == nTime)
        {
            board[nPos, NUM] += board[cur.pos, NUM];
        }
    }
}

writer.WriteLine(board[k, TIME]);
writer.WriteLine(board[k, NUM]);