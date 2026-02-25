const int MAX_SIZE = 100_001;
const int START = -1;
const int NOT_VISITED = -2;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] input = reader.ReadLine().Split();
int n = int.Parse(input[0]);
int k = int.Parse(input[1]);

if (k <= n)
{
    int[] result = new int[n - k];

    writer.WriteLine(n - k);
    for (int i=n;i>=k;i--)
    {
        writer.Write($"{i} ");
    }

    return;
}

Queue<(int pos, int time)> queue = new Queue<(int pos, int time)>();
int[] prevPos = new int[MAX_SIZE];
Array.Fill(prevPos, NOT_VISITED);

queue.Enqueue((n, 0));
prevPos[n] = START;

Func<int, int>[] moves = {(int x) => x*2, (int x) => x+1, (int x) => x-1};

while (queue.Count > 0)
{
    (int pos, int time) cur = queue.Dequeue();
    int nTime = cur.time + 1;

    foreach (var move in moves)
    {
        int nPos = move(cur.pos);

        if (nPos < 0 || nPos >= MAX_SIZE || prevPos[nPos] != NOT_VISITED) continue;

        if (nPos == k)
        {
            List<int> result = new List<int>();
            
            result.Add(nPos);

            int prev = cur.pos;

            while (prev != START)
            {
                result.Add(prev);
                prev = prevPos[prev];
            }

            result.Reverse();

            writer.WriteLine(nTime);
            writer.WriteLine(string.Join(" ", result));

            return;
        }

        queue.Enqueue((nPos, nTime));
        prevPos[nPos] = cur.pos;
    }
}