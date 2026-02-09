using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MAX_LENGTH = 100000;
const int IMPOSSIBLE = -1;

(int dr, int dc)[] receivePos = {(0, 0), (-1, 0), (0, -1), (1, 0), (0, 1)};

int n = int.Parse(reader.ReadLine());
string[] input = reader.ReadLine().Split();
int curX = int.Parse(input[0]);
int curY = int.Parse(input[1]);

long[] memo = new long[receivePos.Length];
long[] nextMemo = new long[receivePos.Length];

for (int i=0;i<receivePos.Length;i++)
{
    memo[i] = IMPOSSIBLE;
    nextMemo[i] = IMPOSSIBLE;
}

memo[0] = 0;

for (int i=0;i<n;i++)
{
    input = reader.ReadLine().Split();
    int nextX = int.Parse(input[0]);
    int nextY = int.Parse(input[1]);

    for (int j=0;j<receivePos.Length;j++)
    {
        if (memo[j] == IMPOSSIBLE) continue;

        int xp = curX+receivePos[j].dr;
        int yp = curY+receivePos[j].dc;

        for (int k=0;k<receivePos.Length;k++)
        {
            int nxp = nextX+receivePos[k].dr;
            int nyp = nextY+receivePos[k].dc;

            if (nxp < 0 || nxp > MAX_LENGTH || nyp < 0 || nyp > MAX_LENGTH) continue;

            long dist = memo[j] + Math.Abs(xp-nxp) + Math.Abs(yp-nyp);

            if (nextMemo[k] == IMPOSSIBLE || dist < nextMemo[k]) nextMemo[k] = dist;
        }
    }

    curX = nextX;
    curY = nextY;

    long[] temp = memo;
    memo = nextMemo;
    nextMemo = temp;

    for (int j=0;j<receivePos.Length;j++)
    {
        nextMemo[j] = IMPOSSIBLE;
    }
}


long minDist = memo[0];

for (int i=1;i<receivePos.Length;i++)
{
    if (memo[i] != IMPOSSIBLE && memo[i] < minDist) minDist = memo[i];
}
writer.WriteLine(minDist);