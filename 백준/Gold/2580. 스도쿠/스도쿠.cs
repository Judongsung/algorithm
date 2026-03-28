using System.Runtime.CompilerServices;

using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int BLANK = 0;
const int MAX_NUM = 9;
const int PLACE_SIZE = 3;

Cell[,] board = new Cell[MAX_NUM, MAX_NUM];
List<Cell> blanks = new List<Cell>();

for (int i=0;i<MAX_NUM;i++)
{
    string[] input = reader.ReadLine().Split();
    
    for (int j=0;j<MAX_NUM;j++)
    {
        int num = int.Parse(input[j]);
        Cell cell = new Cell(i, j, num);
        
        if (num == BLANK) blanks.Add(cell);
        board[i, j] = cell;
    }
}

foreach (Cell bc in blanks)
{
    for (int i=0;i<MAX_NUM;i++)
    {
        int cur = board[i, bc.col].num;
        if (cur != BLANK) bc.candidates.Remove(cur);

        cur = board[bc.row, i].num;
        if (cur != BLANK) bc.candidates.Remove(cur);
    }

    int startRow = (bc.row / PLACE_SIZE) * PLACE_SIZE;
    int startCol = (bc.col / PLACE_SIZE) * PLACE_SIZE;

    for (int i=0;i<PLACE_SIZE;i++)
    {
        for (int j=0;j<PLACE_SIZE;j++)
        {
            int cur = board[startRow + i, startCol + j].num;
            if (cur != BLANK) bc.candidates.Remove(cur);
        }
    }

    foreach (Cell other in blanks)
    {
        if (other == bc) continue;

        if (bc.row == other.row) bc.linkedBlanks.Add(other);
        else if (bc.col == other.col) bc.linkedBlanks.Add(other);
        else if (bc.row / PLACE_SIZE == other.row / PLACE_SIZE && bc.col / PLACE_SIZE == other.col / PLACE_SIZE) bc.linkedBlanks.Add(other);
    }
}

CompleteSudoku(0);

for (int i=0;i<MAX_NUM;i++)
{
    for (int j=0;j<MAX_NUM;j++)
    {
        writer.Write($"{board[i, j].num} ");
    }
    writer.WriteLine();
}

bool CompleteSudoku(int bidx)
{
    if (bidx == blanks.Count) return true;

    Cell cur = blanks[bidx];

    foreach (int candidate in cur.candidates.ToList())
    {
        bool isContinue = false;
        cur.num = candidate;

        List<Cell> removedFrom = new List<Cell>();

        foreach (Cell linked in cur.linkedBlanks)
        {
            if (linked.num != BLANK) continue;

            if(linked.candidates.Remove(candidate))
            {
                removedFrom.Add(linked);

                if (linked.candidates.Count == 0)
                {
                    isContinue = true;
                    break;
                }
            }

        }

        if (!isContinue)
        {
            bool isSuccess = CompleteSudoku(bidx+1);
            if (isSuccess) return true;
        }

        foreach (Cell linked in removedFrom)
        {
            linked.candidates.Add(candidate);
        }
        cur.num = BLANK;
    }

    return false;
}

class Cell
{
    const int BLANK = 0;
    public int row;
    public int col;
    public int num;
    public HashSet<int> candidates;
    public List<Cell> linkedBlanks;

    public Cell(int row, int col, int num)
    {
        this.row = row;
        this.col = col;
        this.num = num;
        
        if (num != BLANK) return;

        candidates = new HashSet<int>();

        for (int i=1;i<=9;i++)
        {
            if (num == i) continue;
            candidates.Add(i);
        }

        linkedBlanks = new List<Cell>();
    }
}

