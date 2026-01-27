using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const char RED = 'R';
const char BLUE = 'B';

int n = int.Parse(reader.ReadLine());
char[] balls = reader.ReadLine().Trim().ToCharArray();

Dictionary<char, int> ballCounts = new Dictionary<char, int>();
ballCounts[RED] = 0;
ballCounts[BLUE] = 0;

char startBall = balls[0];
char endBall = balls[^1];
bool isStart = true;
int startCount = 0;
int endCount = 0;

for (int i=0;i<n;i++)
{
    char cur = balls[i];

    ballCounts[cur]++;

    if (isStart)
    {
        if (cur != startBall)
        {
            isStart = false;
            
        }
        else
        {
            startCount++;
        }
    }

    if (cur != endBall)
    {
        endCount = 0;
    }
    else
    {
        endCount++;
    }
}

int minCount = ballCounts.Values.Min();
int startMoveCount = ballCounts[startBall]-startCount;
int endMoveCount = ballCounts[endBall]-endCount;
minCount = Math.Min(minCount, Math.Min(startMoveCount, endMoveCount));

writer.WriteLine(minCount);