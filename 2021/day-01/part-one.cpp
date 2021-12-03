#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int findIncrease(vector<string> data)
{
	int count{0};
	int i{0};
	
	while (i < data.size())
	{
		if (data[i] > data[i-1])
			count++
		i++;
	}
	return count;
}

int main ()
{
	ifstream input ("input.txt");
	string depth;
	vector<string> data;
	int index{0};

	if (input.is_open())
	{
		while (!input.eof())
		{
			getline(input, depth);
			data.push_back(depth);
			index++;
		}
		input.close();
	}
	else
		cout << "Unable to open file";

	cout << findIncrease(data);

	return 0;
}