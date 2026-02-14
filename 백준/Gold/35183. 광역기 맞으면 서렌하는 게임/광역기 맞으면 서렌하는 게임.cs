using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MIN = 1;
const int MAX = 1000;

const string SUCCESS = "World Champion";
const string FAIL = "Surrender";

int[] range = {-1, 0, 1};

int n = int.Parse(reader.ReadLine());
int[] left = new int[n];
int[] right = new int[n];

for (int i=0;i<n;i++)
{
    string[] input = reader.ReadLine().Split();
    left[i] = int.Parse(input[0]);
    right[i] = int.Parse(input[1]);
}

bool[,] dp = new bool[MAX+1, 2];

for (int i=left[0];i<=right[0];i++)
{
    dp[i, 0] = true;
}

for (int i=1;i<=MAX;i++)
{
    dp[i, 1] = true;
}

bool[,] nextDp = new bool[MAX+1, 2];
bool anyAlive = true;

for (int i=1;i<n;i++)
{
    anyAlive = false;

    for (int pos=1;pos<=MAX;pos++)
    {
        bool fromNotUsed = (pos > 1 && dp[pos-1, 0]) || dp[pos, 0] || (pos < MAX && dp[pos+1, 0]);
        bool fromUsed = (pos > 1 && dp[pos-1, 1]) || dp[pos, 1] || (pos < MAX && dp[pos+1, 1]);

        if (fromNotUsed && pos >= left[i] && pos <= right[i])
        {
            nextDp[pos, 0] = true;
            anyAlive = true;
        }

        if (fromUsed && pos >= left[i] && pos <= right[i])
        {
            nextDp[pos, 1] = true;
            anyAlive = true;
        }
        else if (fromNotUsed)
        {
            nextDp[pos, 1] = true;
            anyAlive = true;
        }
    }

    bool[,] temp = dp;
    dp = nextDp;
    nextDp = temp;

    Array.Clear(nextDp);

    if (!anyAlive)
    {
        break;
    }
}

writer.WriteLine(anyAlive? SUCCESS : FAIL);