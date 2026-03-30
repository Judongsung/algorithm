using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int MAX_NUM = 9;
const int AREA_SIZE = 3;
const int BLANK = 0;
const int DEFAULT_CANDIDATE = (1 << (MAX_NUM)) - 1;

int[] bit = new int[MAX_NUM+1];

for (int i=1;i<=MAX_NUM;i++)
{
    bit[i] = 1 << (i-1);
}

int[,] board = new int[MAX_NUM, MAX_NUM];

for (int r=0;r<MAX_NUM;r++)
{
    string input = reader.ReadLine();

    for (int c=0;c<MAX_NUM;c++)
    {
        board[r, c] = input[c]-'0';
    }
}

solve(0);

for (int r=0;r<MAX_NUM;r++)
{
    for (int c=0;c<MAX_NUM;c++)
    {
        writer.Write(board[r, c]);
    }
    writer.WriteLine();
}

bool solve(int pos)
{
    if (pos == MAX_NUM * MAX_NUM)
    {
        return true;
    }

    int r = pos / MAX_NUM;
    int c = pos % MAX_NUM;

    if (board[r, c] != BLANK)
    {
        return solve(pos+1);
    }

    int candidates = GetCandidates(r, c);

    if (candidates == 0)
    {
        return false;
    }

    for (int i=1;i<=MAX_NUM;i++)
    {
        if ((candidates & bit[i]) != 0)
        {
            board[r, c] = i;

            bool isSuccess = solve(pos+1);
            if (isSuccess) return true;

            board[r, c] = BLANK;
        }
    }

    return false;
}

int GetCandidates(int r, int c)
{
    int candidates = DEFAULT_CANDIDATE;

    for (int i=0;i<MAX_NUM;i++)
    {
        int num = board[r, i];
        if (num != BLANK)
        {
            candidates &= ~bit[num];
        }

        num = board[i, c];
        if (num != BLANK)
        {
            candidates &= ~bit[num];
        }
    }

    int rStart = (r / AREA_SIZE) * AREA_SIZE;
    int cStart = (c / AREA_SIZE) * AREA_SIZE;

    for (int i=0; i<AREA_SIZE;i++)
    {
        for (int j=0;j<AREA_SIZE;j++)
        {
            int num = board[rStart + i, cStart + j];
            if (num != BLANK)
            {
                candidates &= ~bit[num];
            }
        }
    }

    return candidates;
}