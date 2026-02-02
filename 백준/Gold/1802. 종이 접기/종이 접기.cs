using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const string YES = "YES";
const string NO = "NO";

int t = int.Parse(reader.ReadLine());

for (int i=0;i<t;i++)
{
    string input = reader.ReadLine().Trim();
    bool isPossible = CheckPossible(input, input.Length);

    writer.WriteLine(isPossible? YES:NO);
}

bool CheckPossible(String origami, int length)
{
    if (length == 1) return true;

    int mid = length/2;

    for (int i=0;i<mid;i++)
    {
        if (origami[i] == origami[length-1-i])
        {
            return false;
        }
    }

    return CheckPossible(origami, mid);
}