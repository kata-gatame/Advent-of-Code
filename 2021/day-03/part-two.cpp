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

vector<string> getO2(vector<string> data)
{
	vector<string>onesLeading;
	vector<string>zeroesLeading;

	int position{0};
	while (position < 12)
	{
		int i{0};
		while (i < data.size())
		{
			if (data[i].at(position) == '1')
				onesLeading.push_back(data[i]);
			
			if (data[i].at(position) == '0')
				zeroesLeading.push_back(data[i]);

			i++;
		}

		if (onesLeading.size() >= zeroesLeading.size())
			data = onesLeading;
		else
			data = zeroesLeading;

		onesLeading.clear();
		zeroesLeading.clear();
		position++;
	}

	return data;
}

vector<string> getCO2(vector<string> data)
{
	vector<string>onesLeading;
	vector<string>zeroesLeading;

	int position{0};
	while (position < 12)
	{
		int i{0};
		while (i < data.size())
		{
			if (data[i].at(position) == '1')
				onesLeading.push_back(data[i]);
			
			if (data[i].at(position) == '0')
				zeroesLeading.push_back(data[i]);

			i++;
		}

		if (onesLeading.size() < zeroesLeading.size())
			data = onesLeading;
		else
			data = zeroesLeading;

		onesLeading.clear();
		zeroesLeading.clear();
		position++;
	}

	return data;
}

int main()
{
	ifstream input ("input.txt");
	string report;
	vector<string> data;

	int index{0}, o2{0}, co2{0};

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

	vector<string> O2rating = getO2(data);
	vector<string> CO2rating = getCO2(data);
  
	cout << convert(O2rating[0]) * convert(CO2rating[0]);

	return 0;
}