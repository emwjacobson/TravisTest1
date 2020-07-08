#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(int argc, char* argv[]) {
    if(argc < 2) {
        cerr << "Invalid arguments. Usage: " << argv[0] << " #" << endl;
        return 1;
    }

    string a(argv[1]);
    float num = 0;
    try {
        num = stof(a);
    } catch (const invalid_argument &ia) {
        cerr << "Error, number not entered. Usage: " << argv[0] << " #" << endl;
        return 1;
    }
    cout << pow(num, 2) << endl;
    return 0;
}