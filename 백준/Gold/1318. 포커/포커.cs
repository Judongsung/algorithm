using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const int PATTERN_COUNT = 4;
const int MAX_NUM = 13;
const int TOTAL_MAX_NUM = PATTERN_COUNT * MAX_NUM;
const int HAND_NUM = 6;

int[] numCounts = new int[MAX_NUM];
int[] patternCounts = new int[PATTERN_COUNT];

Func<bool[], bool>[] candidates = new Func<bool[], bool>[12];
int cur = 0;

// 로얄 스트레이트 플러쉬
candidates[cur] = hand => {
    for (int p=0;p<PATTERN_COUNT;p++)
    {
        if (patternCounts[p] < 5) continue;
        
        int series = 0;

        for (int n=0;n<5;n++)
        {
            if (!hand[p * MAX_NUM + n]) break;
            
            series++;
        }

        if (series == 5) return true;
    }

    return false;
};
cur++;

// 스트레이트 플러쉬
candidates[cur] = hand => {
    for (int p=0;p<PATTERN_COUNT;p++)
    {
        if (patternCounts[p] < 5) continue;

        int series = 0;

        for (int n=0;n<MAX_NUM;n++)
        {
            if (!hand[p * MAX_NUM + n])
            {
                series = 0;
                continue;
            }
            
            series++;

            if (series == 5) return true;
        }
    }

    return false;
};
cur++;

// 포카드
candidates[cur] = hand => {
    foreach (int nCount in numCounts)
    {
        if (nCount >= 4) return true;
    }
    return false;
};
cur++;

// 풀하우스
candidates[cur] = hand => {
    int triples = 0;
    int pairs = 0;

    for (int n=0;n<MAX_NUM;n++)
    {
        if (numCounts[n] >= 3) triples++;
        else if (numCounts[n] == 2) pairs++;
    }

    return triples >= 2 || (triples >= 1 && pairs >= 1);
};
cur++;

// 플러쉬
candidates[cur] = hand => {
    foreach (int pCount in patternCounts)
    {
        if (pCount >= 5) return true;
    }

    return false;
};
cur++;

// 마운틴
candidates[cur] = hand => {
    return numCounts[0] > 0 && numCounts[^1] > 0 && numCounts[^2] > 0 && numCounts[^3] > 0 && numCounts[^4] > 0;
};
cur++;

// 빽스트레이트
candidates[cur] = hand => {
    return numCounts[0] > 0 && numCounts[1] > 0 && numCounts[2] > 0 && numCounts[3] > 0 && numCounts[4] > 0;
};
cur++;

// 스트레이트
candidates[cur] = hand => {
    int series = 0;

    foreach (int nCount in numCounts)
    {
        if (nCount == 0)
        {
            series = 0;
            continue;
        }

        series++;
        if (series >= 5) return true;
    }

    return false;
};
cur++;

// 트리플
candidates[cur] = hand => {
    foreach (int nCount in numCounts)
    {
        if (nCount >= 3)
        {
            return true;
        } 
    }

    return false;
};
cur++;

// 투페어
candidates[cur] = hand => {
    int pairCount = 0;

    foreach (int nCount in numCounts)
    {
        if (nCount >= 2)
        {
            pairCount++;
            if (pairCount >= 2) return true;
        } 
    }

    return false;
};
cur++;

// 원페어
candidates[cur] = hand => {
    foreach (int nCount in numCounts)
    {
        if (nCount >= 2) return true;
    }

    return false;
};
cur++;

// 탑
candidates[cur] = hand => {
    return true;
};
cur++;

bool[] hand = new bool[PATTERN_COUNT * MAX_NUM];
int[] cases = new int[candidates.Length];
int caseNum = 0;

Dfs(0, 0);

for (int i=cases.Length-1;i>=0;i--)
{
    int gcd = GetGcd(cases[i], caseNum);
    writer.WriteLine($"{cases[i]/ gcd}/{caseNum / gcd}");
}

void Dfs(int start, int depth)
{
    if (depth == HAND_NUM)
    {
        for (int i=0;i<candidates.Length;i++)
        {
            if (candidates[i](hand))
            {
                cases[i]++;
                break;
            }
        }
        caseNum++;
        return;
    }

    for (int i = start; i <= TOTAL_MAX_NUM - (HAND_NUM - depth); i++)
    {
        hand[i] = true;

        int p = i / MAX_NUM;
        int n = i % MAX_NUM;
        patternCounts[p]++;
        numCounts[n]++;

        Dfs(i + 1, depth + 1);

        hand[i] = false;
        patternCounts[p]--;
        numCounts[n]--;
    }
}

int GetGcd(int a, int b)
{
    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}