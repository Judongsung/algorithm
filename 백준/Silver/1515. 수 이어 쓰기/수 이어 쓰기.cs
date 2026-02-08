using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string s = reader.ReadLine().Trim();
int cur = 0;
int idx = 0;

while (idx < s.Length)
{
    cur++;
    string sCur = cur.ToString();

    for (int i=0;i<sCur.Length;i++)
    {
        if (idx >= s.Length) break;

        if (sCur[i] == s[idx])
        {
            idx++;
        }
    }
}

writer.WriteLine(cur);