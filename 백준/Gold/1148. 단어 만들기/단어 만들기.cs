using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const string END_OF_WORD = "-";
const string END_OF_PUZZLE = "#";
const int ALPHABET_COUNT = 26;

List<int> wordMasks = new List<int>();
List<int[]> wordCounters = new List<int[]>();

while (true)
{
    string word = reader.ReadLine();
    
    if (word == END_OF_WORD) break;

    int mask = Convert(word, out int[] counter);

    wordMasks.Add(mask);
    wordCounters.Add(counter);
}

while (true)
{
    string puzzle = reader.ReadLine();

    if (puzzle == END_OF_PUZZLE) break;

    int mask = Convert(puzzle, out int[] counter);
    int[] totalCounter = new int[ALPHABET_COUNT];
    
    for (int i=0;i<wordMasks.Count;i++)
    {
        int wordMask = wordMasks[i];
        int[] wordCounter = wordCounters[i];

        if ((mask & wordMask) == wordMask)
        {
            bool isFail = false;

            for (int j=0;j<ALPHABET_COUNT;j++)
            {
                if (counter[j] < wordCounter[j])
                {
                    isFail = true;
                    break;
                }
            }

            if (isFail)
            {
                continue;
            }

            for (int j=0;j<ALPHABET_COUNT;j++)
            {
                if ((wordMask & (1 << j)) != 0)
                {
                    totalCounter[j]++;
                }
            }
        }
    }

    int minCount = int.MaxValue;
    int maxCount = -1;
    List<char> minAlphabets = null;
    List<char> maxAlphabets = null;

    for (int i=0;i<ALPHABET_COUNT;i++)
    {
        if ((mask & (1 << i)) == 0) continue;
        int aCount = totalCounter[i];

        if (aCount < minCount)
        {
            minCount = aCount;
            minAlphabets = new List<char>();
            minAlphabets.Add((char)(i + 'A'));
        }
        else if (aCount == minCount)
        {
            minAlphabets.Add((char)(i + 'A'));
        }

        if (aCount > maxCount)
        {
            maxCount = aCount;
            maxAlphabets = new List<char>();
            maxAlphabets.Add((char)(i + 'A'));
        }
        else if (aCount == maxCount)
        {
            maxAlphabets.Add((char)(i + 'A'));
        }
    }

    writer.WriteLine($"{string.Join("", minAlphabets)} {minCount} {string.Join("", maxAlphabets)} {maxCount}");
}

int Convert(string str, out int[] counter)
{
    int mask = 0;
    counter = new int[ALPHABET_COUNT];

    foreach (char ch in str)
    {
        int idx = ch - 'A';

        mask |= 1 << idx;
        counter[idx] += 1;
    }

    return mask;
}