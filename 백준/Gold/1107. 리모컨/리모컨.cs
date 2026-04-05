using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int START = 100;

int target = int.Parse(reader.ReadLine());
int m = int.Parse(reader.ReadLine());
HashSet<int> buttonSet = new HashSet<int>();
for (int i=0;i<10;i++) buttonSet.Add(i);

if (m > 0)
{
    string[] input = reader.ReadLine().Split();
    foreach (string s in input)
    {
        int disabled = int.Parse(s);
        buttonSet.Remove(disabled);
    }
}

int[] buttons = buttonSet.ToArray();
Array.Sort(buttons);

int minClick = Math.Abs(target - START);
int maxDigits = target.ToString().Length;

Dfs(0, 0);
writer.WriteLine(minClick);

void Dfs(int cur, int digits)
{
    if (digits > maxDigits) return;

    int nextDigits = digits + 1;

    foreach (int button in buttons)
    {
        int next = cur * 10 + button;
        int nextClick = nextDigits + Math.Abs(target - next);

        if (nextClick < minClick) minClick = nextClick;

        Dfs(next, nextDigits);
    }
}