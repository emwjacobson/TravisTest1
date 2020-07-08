#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    if(argc < 2) {
        cout << "Invalid arguments. Usage: " << argv[0] << " #" << endl;
        return 1;
    }

    string a(argv[1]);
    int num = 0;
    try {
        num = stoi(a);
    } catch (const invalid_argument &ia) {
        cout << "Error, number not entered. Usage: " << argv[0] << " #" << endl;
        return 1;
    }
    cout << num << endl;
    return 0;
}