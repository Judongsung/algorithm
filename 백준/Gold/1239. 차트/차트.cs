using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int TARGET = 50;

int n = int.Parse(reader.ReadLine());
string[] input = reader.ReadLine().Split();
int[] groups = new int[n];
int[] graph = new int[n];
bool[] visited = new bool[n];

for (int i=0;i<n;i++)
{
    int group = int.Parse(input[i]);

    if (group > TARGET)
    {
        writer.WriteLine(0);
        return;
    }
    else if (group == TARGET)
    {
        writer.WriteLine(1);
        return;
    }

    groups[i] = group;
}

graph[0] = groups[0];
visited[0] = true;
int result = Dfs(0, 0, groups[0]);

writer.WriteLine(result);

int Dfs(int graphIdx, int left, int slice)
{
    if (graphIdx == n - 2)
    {
        return 0;
    }

    int maxCount = 0;
    int nextIdx = graphIdx + 1;
    
    for (int i=0;i<n;i++)
    {
        if (visited[i]) continue;

        int nextGroup = groups[i];
        int nextSlice = slice + nextGroup;
        int nextLeft = left;
        graph[nextIdx] = nextGroup;
        visited[i] = true;

        while (nextSlice > TARGET)
        {
            nextSlice -= graph[nextLeft++];
        }

        int count = 0;

        if (nextSlice == TARGET)
        {
            count++;
        }

        count += Dfs(nextIdx, nextLeft, nextSlice);

        visited[i] = false;

        if (count > maxCount) maxCount = count;
    }

    return maxCount;
}