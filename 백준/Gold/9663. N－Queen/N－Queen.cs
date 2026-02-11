using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

(int dr, int dc)[] dirs = {(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)};

int n = int.Parse(reader.ReadLine());
int[,] board = new int[n,n];
bool[] usedCol = new bool[n];
bool[] usedDiag1 = new bool[n*2];
bool[] usedDiag2 = new bool[n*2];

writer.WriteLine(Find_max_cases(0));

int Find_max_cases(int r)
{
    if (r == n) return 1;

    int cases = 0;

    for (int c=0;c<n;c++)
    {
        if (IsUsed(r, c)) continue;

        Mark(r, c);

        cases += Find_max_cases(r+1);

        Unmark(r, c);
    }

    return cases;
}

void Mark(int r, int c)
{
    usedCol[c] = true;
    usedDiag1[r+c] = true;
    usedDiag2[r-c+n] = true;
}

void Unmark(int r, int c)
{
    usedCol[c] = false;
    usedDiag1[r+c] = false;
    usedDiag2[r-c+n] = false;
}

bool IsUsed(int r, int c)
{
    return usedCol[c] || usedDiag1[r+c] || usedDiag2[r-c+n];
}