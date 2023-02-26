#include "knight.h"

void display(int HP, int level, int remedy, int maidenkiss, int phoenixdown, int rescue) {
    cout << "HP=" << HP
        << ", level=" << level
        << ", remedy=" << remedy
        << ", maidenkiss=" << maidenkiss
        << ", phoenixdown=" << phoenixdown
        << ", rescue=" << rescue << endl;
}

int level0_cal(int & i) {
    int b, level0;
    b = i % 10;
    level0 = i > 6 ? (b > 5 ? b : 5) : b;
    return level0;
}

int dmg_cal(int & level0, int & opponentCode) {
    int baseDmg[5] = {1, 1.5, 4.5, 7.5, 9.5};
    int dmg;
    dmg = baseDmg[opponentCode] * level0 * 10;
    return dmg;
}

void adventureToKoopa(string file_input, int & HP, int & level, int & remedy, int & maidenkiss, int & phoenixdown, int & rescue) {
    cout << "Function isn't implemented" << endl;
}