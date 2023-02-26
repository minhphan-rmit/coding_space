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
    int route[5] = {1, 2, 9, 18, 99};
    int routeLength = sizeof(route) / sizeof(int);
    int maxHP = HP;
    for (int i = 1; i < (routeLength + 1); i++) {
        // the event code is 0 then stop immediately and rescue = 1
        if (route[i] == 0) {
            rescue = 1;
            break;
        }

        // the event code is 1 to 5:
        if (route[i] >= 1 && route[i] <= 5) {
            int currentLevel0 = level0_cal(i);
            int currentDmg = dmg_cal(currentLevel0, route[i]);
            if (level > currentLevel0) {
                level += 1;
            } else if (level == currentLevel0) {
                level += 0;
            } else {
                HP = HP - currentDmg;
            }
            if (level > 10) {
                level = 10;
            }
            if (HP <= 0) {
                if (phoenixdown > 0) {
                    HP = maxHP;
                    phoenixdown -= 1;
                } else {
                    rescue = 0;
                    break;
                }
            } 
        }
        // the event code is 6 (Shaman)
        if (route[i] == 6) {
           int currentLevel0 = level0_cal(i); 
           if (level > currentLevel0) {
                level += 2;
            } else if (level == currentLevel0) {
                level += 0;
            } else {
                if (remedy >= 1) {
                    remedy -= 1;
                } else {
                    if (HP <= 5) {
                        HP = 1;
                    } else {
                        HP = HP / 5;
                    }
                }
            }
        }
    }
    cout << "Function isn't implemented" << endl;
}