using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

Dictionary<char, int> user_requires = new Dictionary<char, int>()
{
    {'Y', 2},
    {'F', 3},
    {'O', 4}
};

string[] firstLine = reader.ReadLine().Split();
int n = int.Parse(firstLine[0]);
char game = firstLine[1][0];

HashSet<string> users = new HashSet<string>();

for(int i=0;i<n;i++)
{
    users.Add(reader.ReadLine());
}

int result = users.Count/(user_requires[game]-1);
writer.WriteLine(result);