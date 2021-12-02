#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string getDirection(string command) {
    return command.substr(0, command.find(' '));
}

int getDistance(string command) {
    size_t i{0};
    for (; i < command.length(); i++){ if (isdigit(command[i])) break; }
    command = command.substr(i, command.length() - i);
    return atoi(command.c_str());
}

void functionX(string *array, int *x, int *y)
{
    string command{array[0]};
    int i{0};

    while (i < 1000) {
        string movementDirection = getDirection(array[i]);
        int movementDistance = getDistance(array[i]);

        if (movementDirection == "forward") *x += movementDistance;
        if (movementDirection == "down") *y += movementDistance;
        if (movementDirection == "up") *y -= movementDistance;

        i++;
    }
}

int main() {
    ifstream input ("input.txt");
    string command;
    string array[999];
    int index{0}, x{0}, y{0};

    if (input.is_open())
    {
        while (! input.eof() )
        {
            getline(input, command);
            array[index] = command;
            index++;
        }
        input.close();
    }
    else
    {
        cout << "Unable to open file";
    }

    functionX(array, &x, &y);
    cout << x*y;

    return 0;
}