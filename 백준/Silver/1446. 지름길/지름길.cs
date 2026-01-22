using System.Collections;


using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string[] line = reader.ReadLine().Split();
int n = int.Parse(line[0]);
int dist = int.Parse(line[1]);

List<(int Start, int End, int Len)> shortcuts = new List<(int, int, int)>(n);

for(int i=0;i<n;i++)
{
    int[] s = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);

    if(s[1] <= dist && s[1]-s[0] > s[2])
    {
        shortcuts.Add((s[0], s[1], s[2]));
    }
}

shortcuts.Sort();
Queue<(int Start, int End, int Len)> queue = new Queue<(int, int, int)>(shortcuts);

int[] dp = new int[dist+1];

for(int i=0;i<dist+1;i++)
{
    dp[i] = i;
}

for(int i=0;i<dist+1;i++)
{
    if(i > 0)
    {
        dp[i] = Math.Min(dp[i], dp[i-1]+1);
    }

    while(queue.Count > 0 && queue.Peek().Start == i)
    {
        var shortcut = queue.Dequeue();
        dp[shortcut.End] = Math.Min(dp[shortcut.End], dp[shortcut.Start]+shortcut.Len);
    }
}

writer.WriteLine(dp[dist]);