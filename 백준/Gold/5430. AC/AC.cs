using var reader = new StreamReader(Console.OpenStandardInput());
using var writer = new StreamWriter(Console.OpenStandardOutput());

const char REVERSE = 'R';
const char DELETE = 'D';
const string ERROR  = "error";

int tc = int.Parse(reader.ReadLine());

for (int i=0;i<tc;i++)
{
    string funcs = reader.ReadLine();
    int n = int.Parse(reader.ReadLine());
    LinkedList<string> list = StringToLinkedList(reader.ReadLine());

    bool reverse = false;
    bool isFail = false;

    foreach (char f in funcs)
    {
        if (f == REVERSE)
        {
            reverse = !reverse;
        }
        else if (f == DELETE)
        {
            if (list.Count == 0)
            {
                isFail = true;
                break;
            }

            if (reverse)
            {
                list.RemoveLast();
            }
            else
            {
                list.RemoveFirst();
            }
        }
    }

    if (isFail)
    {
        writer.WriteLine(ERROR);
    }
    else
    {
        if (reverse)
        {
            LinkedList<String> temp = new LinkedList<string>();
            
            foreach (string s in list)
            {
                temp.AddFirst(s);
            }

            list = temp;
        }
        writer.WriteLine($"[{String.Join(',', list)}]");
    }
}

LinkedList<string> StringToLinkedList(string data)
{
    string temp = data.Substring(1, data.Length-2);
    LinkedList<string> result = new LinkedList<string>(temp.Split(','));

    if (result.First() == "")
    {
        result = new LinkedList<string>();
    }
    return result;
}