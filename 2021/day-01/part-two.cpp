#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int findIncreases(int *array, int size, int window)
{
    int prevSum{0};
    int count{0};
 
    for (int i = 0; i < size - window + 1; i++) {
        int currentSum = 0;

        for (int j = 0; j < window; j++)
            currentSum = currentSum + array[i + j];
        
        if (currentSum > prevSum)
            count++;
        
        prevSum = currentSum;
    }
    return count;
}

int main ()
{
    int array[1999];
    short i{0};

    string line; 
    ifstream input("input.txt"); 
    if (input.is_open())
    {
        while (! input.eof() )
        {
            getline(input, line);
            array[i] = stoi(line);
            i++;
        }
        input.close();
    }
    else cout << "Unable to open file";
    
    int w = 3;
    int s = sizeof(array) / sizeof(array[0]);
    cout << findIncreases(array, s, w);

    return 0;
}