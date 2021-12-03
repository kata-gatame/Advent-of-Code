#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int convert(string str)
{
   string n{str};
   int val{0}, temp{1}, len = n.length();
   for (int i = len - 1; i >= 0; i--) {
		if (n[i] == '1')
		val += temp;
		temp = temp * 2;
   }
   return val;
}

void getGamma(vector<string> data, int *gamma, int *epsilon)
{
	int position{0};
	string g = "";
	string e = "";

	while (position < 12)
	{
		int ones{0};
		int zeroes{0};
		int i{0};

		while (i < data.size())
		{
			if (data[i][position] == '1')
				ones++;
			if (data[i][position] == '0')
				zeroes++;
			i++;
		}

		if (ones > zeroes)
		{
			g.append("1");
			e.append("0");
		}            
		else
		{
			g.append("0");
			e.append("1");
		}
		position++;
	}

	*gamma = convert(g);
	*epsilon = convert(e);
}

int main()
{
	ifstream input ("input.txt");
	string report;
	vector<string> data;
	int index{0}, gamma{0}, epsilon{0};

	if (input.is_open())
	{
		while (!input.eof())
		{
			getline(input, report);
			data.push_back(report);
			index++;
		}
		input.close();
	}
	else
		cout << "Unable to open file";
	
	getGamma(data, &gamma, &epsilon);

	cout << gamma * epsilon;

	return 0;
}