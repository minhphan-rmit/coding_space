#include "knight.h"

void display(int HP, int level, int remedy, int maidenkiss, int phoenixdown, int rescue) {
    cout << "HP=" << HP
         << ", level=" << level
         << ", remedy=" << remedy
         << ", maidenkiss=" << maidenkiss
         << ", phoenixdown=" << phoenixdown
         << ", rescue=" << rescue << endl;
}

// Function for calculating levelO of the opponent
int levelO_cal(int i) {
    int iO = i + 1; // because the the array index starts from 0
    int b = iO % 10;
    int levelO = iO > 6 ? (b > 5 ? b : 5) : b;
    
    return levelO;
}

// Function for calculating the damage of the opponent
int dmg_cal(int levelO, int opponentCode) {
    opponentCode = opponentCode - 1;
    int baseDmg[5] = {1, 1.5, 4.5, 7.5, 9.5};
    int dmg = baseDmg[opponentCode] * levelO * 10;

    return dmg;
}

// Function for checking the level is max or not
int maxLevel_check(int level) {
    if (level > 10) {
         return level = 10;
    } else {
        return level;
    }
}

void BowserGG(int & rescue) {
    rescue = 1;
}

void easyOpponents(int i, int & level, int & HP, int & maxHP, int & phoenixdown, int & rescue, int opponentCode) {
    int current_levelO = levelO_cal(i);

    if (level > current_levelO) {
        level += 1;
        level = maxLevel_check(level);
    } else if (level == current_levelO) {
        level += 0;
    } else {
        // combat procedure
        int current_dmg = dmg_cal(current_levelO, opponentCode);
        HP = HP - current_dmg;

        // HP check
        if (HP <= 0) {
            if (phoenixdown <= 0) {
                rescue = 0;
            } else {
                phoenixdown -= 1;
                HP = maxHP;
            }
        }
    }
}

void ShamanWitch(int i, int & level, int & HP, int & maxHP, int & phoenixdown, int & remedy, int & rescue, int opponentCode, int & ShamanExpire) {
    int current_levelO = levelO_cal(i);

    if (level > current_levelO) {
        level += 2;
        level = maxLevel_check(level);
    } else if (level == current_levelO) {
        level += 0;
    } else {
        ShamanExpire = i + 4;
        
        if (remedy >= 1) {
            remedy -= 1;
        } else {
            if (HP < 5) {
                HP = 1;
            } else {
                HP = HP / 5;
            }
        }
    }
}

void ExpiredShamanCheck(int i, int & HP, int & maxHP, int & ShamanExpire) {
    if (i == ShamanExpire) {
        HP = HP * 5;
        if (HP > maxHP) {
            HP = maxHP;
        } else {
            HP = HP;
        }
    } else {
        return;
    }
}

void SirenVajsh(int i, int & level, int & HP, int & maxHP, int & phoenixdown, int & remedy, int & maidenkiss, int & rescue, int opponentCode, int & SirenVajshExpire, int & beforeFrog) {
    int current_levelO = levelO_cal(i);

    if (level > current_levelO) {
        level += 2;
        level = maxLevel_check(level);
    } else if (level == current_levelO) {
        level += 0;
    } else {
        SirenVajshExpire = i + 4;

        if (maidenkiss >= 1) {
            level = level;
        } else {
            beforeFrog = level;
            level = 1;
        }
    }
}

void ExpiredSirenVajshCheck(int i, int & level, int & SirenVajshExpire, int & beforeFrog) {
    if (i == SirenVajshExpire) {
        level = beforeFrog;
    } else {
        return;
    }
}

void MushMario(int & HP, int & maxHP, int & level, int & phoenixdown) {
    int n1 = ((level + phoenixdown) % 5 + 1) * 3;
    int s1 = 0;
    for (int i = 99; i > (99 - (n1 * 2)); i -= 2) {
        s1 += i;
    }
    HP = HP + (s1 % 100);
    if (check_prime(HP)) {
        HP = HP;
    } else {
        for (int k=1; k < (HP*HP); k++) {
            HP += 1;
            if (check_prime(HP)) {
                break;
            }
        }
    }
} 

bool check_prime(int n) {
    bool is_prime = true;

    // 0 and 1 are not prime numbers
    if (n == 0 || n == 1) {
        is_prime = false;
    }

    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            is_prime = false;
            break;
        }
    }

    return is_prime;
}

void MushFibo(int & HP) {
    if (HP == 1) {
        return;
    } else {
        int f1 = 1;
        int f2 = 1;
        int fibo;
        for (int i = 1; i < HP; i++) {
            fibo = f1 + f2;
            if (fibo > HP) {
                fibo = fibo - f1;
                break;
            } else {
                f1 = f2;
                f2 = fibo;
            }
        }
        HP = fibo;
    }
}

void adventureToKoopa(string file_input, int & HP, int & level, int & remedy, int & maidenkiss, int & phoenixdown, int & rescue) {
    // sample route
    int route[5] = {1, 2, 8, 18, 99};
    int routeLength = sizeof(route) / sizeof(int); // size of will return bytes

    // Set max HP
    int maxHP = HP;

    int ShamanExpire = -1;
    int SirenVajshExpire = -1;
    int beforeFrog = level;

    // Loop through every events stored in the array
    for (int i = 0; i < routeLength; i++) {
        
        switch (rescue) {
            // check the value of rescue
            case 0:
                break;
            case 1:
                break;
            case -1:
                ExpiredShamanCheck(i, HP, maxHP, ShamanExpire);
                ExpiredSirenVajshCheck(i, level, SirenVajshExpire, beforeFrog);
                switch (route[i]) {
                    case 0: // Bowser GG (event code = 0)
                        BowserGG(rescue);
                        break;
    
                    case 1: // Mad Bear (event code = 1)
                    case 2: // Bandit (event code = 2)
                    case 3: // Lord Lupin (event code = 3)
                    case 4: // Elf (event code = 4)
                    case 5: // Troll (event code = 5)
                        easyOpponents(i, level, HP, maxHP, phoenixdown, rescue, route[i]);
                        break;

                    // Shaman (event code = 6)
                    case 6:
                        if (i >= (SirenVajshExpire - 3) && i < SirenVajshExpire) {
                            break;
                        } else {
                            ShamanWitch(i, level, HP, maxHP, phoenixdown, remedy, rescue, route[i], ShamanExpire);
                            break;
                        }

                    // Siren Vajsh (event code = 7)
                    case 7:
                        if (i >= (ShamanExpire - 3) && i < ShamanExpire) {
                            break;
                        } else {
                            SirenVajsh(i, level, HP, maxHP, phoenixdown, remedy, maidenkiss, rescue, route[i], SirenVajshExpire, beforeFrog);
                            break;
                        }

                    // Mush Mario (event code = 11)
                    case 11:  
                        MushMario(HP, maxHP, level, phoenixdown);
                        break;

                    // Mush Fibonacci (event code = 12)
                    case 12:
                        MushFibo(HP);
                        break;
                        
                    // Mush Ghost (event code = 13<ms>)
                    case 13:

                    // Remedy (event code = 15)
                    case 15:

                    // Maiden Kiss (event code = 16)
                    case 16:

                    // Phoenix Down (event code = 17)
                    case 17:

                    // Merlin (event code = 18)
                    case 18:

                    // Asclepius (event code = 19)
                    case 19:

                    // Bowser (event code = 99)
                    case 99:
                    default:
                }
        }
    }
}