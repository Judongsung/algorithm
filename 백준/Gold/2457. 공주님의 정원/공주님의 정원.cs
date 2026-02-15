using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
int[] dayPresum = new int[days.Length+2]; // dayPresum[month] = month월 이전 일수

dayPresum[2] = days[0];

for (int i=3;i<days.Length+2;i++)
{
    dayPresum[i] = dayPresum[i-1] + days[i-2];
}

int n = int.Parse(reader.ReadLine());
(int start, int end)[] period = new (int start, int end)[n];

for (int i=0;i<n;i++)
{
    string[] input = reader.ReadLine().Split();
    int startMonth = int.Parse(input[0]);
    int startDay = int.Parse(input[1]);
    int endMonth = int.Parse(input[2]);
    int endDay = int.Parse(input[3]);

    period[i] = (DateToNum(startMonth, startDay), DateToNum(endMonth, endDay));
}

Array.Sort(period, (a, b) => a.start.CompareTo(b.start));

int result = 0;
PriorityQueue<int, int> endPq = new PriorityQueue<int, int>();
int latestEnd = DateToNum(3, 1);
int lastDay = DateToNum(12, 1);

for (int i=0;i<n;i++)
{
    var cur = period[i];

    if (cur.start > latestEnd)
    {
        if (endPq.Count == 0)
        {
            result = 0;
            break;
        }

        latestEnd = endPq.Dequeue();
        result++;

        if (cur.start > latestEnd)
        {
            result = 0;
            break;
        }

        if (latestEnd >= lastDay) break;
    }

    endPq.Enqueue(cur.end, -cur.end);
}

if (latestEnd < lastDay)
{
    if (endPq.Count > 0 && endPq.Peek() >= lastDay) result++;
    else result = 0;
}

writer.WriteLine(result);

int DateToNum(int month, int day)
{
    return dayPresum[month] + day;
}