using System.Collections.Generic;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int LENGTH = 3;
const int IMPOSSIBLE = -1;
const int GOAL = 087654321;

(int r, int c)[] dirs = {(0, -1), (0, 1), (1, 0), (-1, 0)};

int start = 0;
int br = 0;
int bc = 0;

for (int i=0;i<LENGTH;i++)
{
    string[] input = reader.ReadLine().Split();

    for (int j=0;j<LENGTH;j++)
    {
        int num = int.Parse(input[j]);

        if (num == 0)
        {
            br = i;
            bc = j;
        }

        start += num * (int) Math.Pow(10, i*LENGTH + j);
    }
}

if (start == GOAL)
{
    writer.WriteLine(0);
    return;
}

Queue<(int board, int br, int bc, int move)> q = new Queue<(int, int, int, int)>();
HashSet<int> visited = new HashSet<int>();
q.Enqueue((start, br, bc, 0));
visited.Add(start);

while (q.Count > 0)
{
    var cur = q.Dequeue();
    
    foreach (var d in dirs)
    {
        int sr = cur.br + d.r;
        int sc = cur.bc + d.c;

        if (sr < 0 || sr >= LENGTH || sc < 0 || sc >= LENGTH) continue;

        int nextBoard = Swap(cur.board, cur.br, cur.bc, sr, sc);

        if (visited.Contains(nextBoard)) continue;

        if (nextBoard == GOAL)
        {
            writer.WriteLine(cur.move+1);
            return;
        }

        q.Enqueue((nextBoard, sr, sc, cur.move+1));
        visited.Add(nextBoard);
    }
}

writer.WriteLine(IMPOSSIBLE);

int Swap(int puzzle, int r1, int c1, int r2, int c2)
{
    int d1 = GetDigit(r1, c1);
    int d2 = GetDigit(r2, c2);
    int n1 = GetDigitNum(puzzle, d1);
    int n2 = GetDigitNum(puzzle, d2);

    puzzle -= n1 * (int) Math.Pow(10, d1) + n2 * (int) Math.Pow(10, d2);
    puzzle += n1 * (int) Math.Pow(10, d2) + n2 * (int) Math.Pow(10, d1);

    return puzzle;
}

int GetDigit(int r, int c)
{
    return r*LENGTH + c;
}

int GetDigitNum(int num, int digit)
{
    return (num / (int) Math.Pow(10, digit)) % 10;
}