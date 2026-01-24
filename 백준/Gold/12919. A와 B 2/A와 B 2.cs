using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

string start = reader.ReadLine().Trim();
string target = reader.ReadLine().Trim();
Stack<string> stack = new Stack<string>();
HashSet<string> visited = new HashSet<string>();
bool is_possible = false;

stack.Push(target);
visited.Add(target);

while (stack.Count > 0)
{
    string cur = stack.Pop();
    if (cur == start)
    {
        is_possible = true;
        break;
    }
    if (cur.Length == start.Length)
    {
        continue;
    }

    if (cur[^1] == 'A')
    {
        string next = cur.Substring(0, cur.Length-1);

        if (!visited.Contains(next))
        {
            stack.Push(next);
            visited.Add(next);
        }
    }
    if (cur[0] == 'B')
    {
        string next = cur.Substring(1, cur.Length-1);
        next = Reverse(next);

        if (!visited.Contains(next))
        {
            stack.Push(next);
            visited.Add(next);
        }
    }
}

writer.WriteLine(is_possible? 1:0);

static string Reverse(string s)
{
    char[] arr = s.ToCharArray();
    Array.Reverse(arr);
    return new string(arr);
}