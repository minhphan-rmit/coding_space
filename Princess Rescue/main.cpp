#include "knight.h"

int main(int argc, char ** argv) {
    string file_input(argv[1]);

    int HP, level, remedy, maidenKiss, phoenixDown, rescue;
    adventureToKoopa(file_input, HP, level, remedy, maidenKiss, phoenixDown, rescue);

    return 0;
}
