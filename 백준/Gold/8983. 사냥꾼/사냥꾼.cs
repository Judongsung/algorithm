using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
int m = input[0];
int n = input[1];
int l = input[2];

List<int> shootingPoints = Array.ConvertAll(reader.ReadLine().Split(), int.Parse).ToList();
shootingPoints.Sort();

int huntable = 0;

for(int i=0;i<n;i++)
{
    int[] animal = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    int x = animal[0];
    int y = animal[1];

    int closestPoint = FindClosest(shootingPoints, x);

    if (Math.Abs(closestPoint-x)+y <= l) huntable++;

}

writer.WriteLine(huntable);

int FindClosest(List<int> list, int target)
{
    int index = list.BinarySearch(target);

    if (index >= 0) return list[index];

    int nextIndex = ~index;

    if (nextIndex == 0) return list[0];

    if (nextIndex == list.Count) return list[list.Count-1];

    int prevValue = list[nextIndex-1];
    int nextValue = list[nextIndex];

    return target-prevValue < nextValue-target? prevValue:nextValue;
}