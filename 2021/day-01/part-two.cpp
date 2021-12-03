#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int findIncreases(vector<int> data)
{
	int prevSum{data[0] + data[1] + data[2]};
	int count{0};
	int i{0};

	while (i < data.size())
	{
		int currentSum{data[i] + data[i+1] + data[i+2]};

		if (currentSum < 0)
			return count;

		if (currentSum > prevSum)
			count++;

		prevSum = currentSum;
		i++;
	}
	return count;
}

int main ()
{
	ifstream input ("input.txt");
	string depth;
	vector<int> data;
	int index{0};

	if (input.is_open())
	{
		while (!input.eof())
		{
			getline(input, depth);
			data.push_back(stoi(depth));
			index++;
		}
		input.close();
	}
	else
		cout << "Unable to open file";

	cout << findIncreases(data);

	return 0;
}