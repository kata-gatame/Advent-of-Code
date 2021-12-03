#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

string getDirection(string command)
{
	return command.substr(0, command.find(' '));
}

int getDistance(string command)
{
	size_t i{0};
	for (; i < command.length(); i++) { if (isdigit(command[i])) break; }
	command = command.substr(i, command.length() - i);
	return atoi(command.c_str());
}

void calculate(vector<string> data, int *x, int *y)
{
	string command{data[0]};
	int i{0};
	int aim{0};

	while (i < data.size())
	{
		string movementDirection = getDirection(data[i]);
		int movementDistance = getDistance(data[i]);

		if (movementDirection == "forward") { *x += movementDistance; *y += movementDistance * aim; }
		if (movementDirection == "down") aim += movementDistance;
		if (movementDirection == "up") aim -= movementDistance;

		i++;
	}
}

int main()
{
	ifstream input ("input.txt");
	string command;
	vector<string> data;
	int index{0}, x{0}, y{0};

	if (input.is_open())
	{
		while (! input.eof())
		{
			getline(input, command);
			data.push_back(command);
			index++;
		}
		input.close();
	}
	else
		cout << "Unable to open file";

	calculate(data, &x, &y);

	cout << x*y;

	return 0;
}