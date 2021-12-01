#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findIncrease(int *array)
{
    int prevDepth{array[0]};
    int count{0};
    int i{0};
    
    while (i < 2000) {
        if (array[i] > prevDepth )
            count++;
        prevDepth = array[i];
        i++;        
    }
    return count;
}

int main () {
    ifstream input ("input.txt");
    string depth;

    int array[1999];
    int index{0};

    if (input.is_open())
    {
        while (! input.eof() )
        {
            getline (input, depth);
            array[index] = stoi(depth);
            index++;
        }
        input.close();
    }
    else
    {
        cout << "Unable to open file";
    }

    cout << findIncrease(array);

    return 0;
}