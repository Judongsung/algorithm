using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

int t = int.Parse(reader.ReadLine());

for (int i=0;i<t;i++)
{
    int[] input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
    int team = input[0];
    int problem = input[1];
    int target = input[2]-1; // 1-base to 0-base
    int log = input[3];

    TeamSolutions[] teamSolutions = new TeamSolutions[team];

    for (int j=0;j<team;j++)
    {
        teamSolutions[j] = new TeamSolutions(j);
    }

    for (int j=0;j<log;j++)
    {
        input = Array.ConvertAll(reader.ReadLine().Split(), int.Parse);
        int teamId = input[0]-1; // 1-base to 0-base
        int problemId = input[1];
        int score = input[2];

        teamSolutions[teamId].AddSolution(j, problemId, score);
    }

    Array.Sort(teamSolutions, (a, b) =>
    {
        int c = b.GetTotalScore().CompareTo(a.GetTotalScore());
        if (c != 0) return c;

        c = a.submitCount.CompareTo(b.submitCount);
        if (c != 0) return c;

        return a.lastSubmit.CompareTo(b.lastSubmit);
    });

    int targetRanking = 0;

    for (int j=0;j<team;j++)
    {
        if (teamSolutions[j].teamId == target)
        {
            targetRanking = j+1;
            break;
        }
    }

    writer.WriteLine(targetRanking);
}

class TeamSolutions
{
    public int teamId;
    public Dictionary<int, int> solutions;
    public int submitCount;
    public int lastSubmit;

    public TeamSolutions(int teamId)
    {
        this.teamId = teamId;
        solutions = new Dictionary<int, int>();
    }

    public void AddSolution(int submitNum, int problemId, int score)
    {
        if (!solutions.TryGetValue(problemId, out var lastScore) || lastScore < score)
        {
            solutions[problemId] = score;
        }
        lastSubmit = submitNum;
        submitCount++;
    }

    public int GetTotalScore()
    {
        int totalScore = 0;

        foreach(int score in solutions.Values)
        {
            totalScore += score;
        }

        return totalScore;
    }
}