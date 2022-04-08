import math
import random

CRIT = 2
WEAK = 1.42
RES = 0.5
WHOLE = 100
TARU = 1.2


class Physical:
    def __init__(self, move_name, hit_number, atk_power, hp_cost_percent, effect):
        self.move_name = str(move_name)
        self.hit_number = int(hit_number)
        self.atk_power = int(atk_power)
        self.hp_cost_percent = float(hp_cost_percent)
        self.effect = str(effect)

        def effect_exists(self):
            if self.effect == str('None'):
                return False
            else:
                return True


class Magic:
    def __init__(self, move_name, hit_number, atk_power, sp_cost, effect):
        self.move_name = str(move_name)
        self.hit_number = int(hit_number)
        self.atk_power = int(atk_power)
        self.hp_cost_percent = int(sp_cost)
        self.effect = str(effect)

        def effect_exists(self):
            if self.effect == str('None'):
                return False
            else:
                return True


def main():
    # Use a breakpoint in the code line below to debug your script.
    buff_check(10)
    equation_time()


def damage_mod(roll):
    pass


def equation_time():
    phys_or_mag = input('Basic, physical or magic?: ')
    true_input = phys_or_mag.lower()
    if true_input == str('b') or true_input == str('bas') or true_input == str('basic'):
        pass
    elif true_input == str('p') or true_input == str('phys') or true_input == str('physical'):
        physboi()
    elif true_input == str('m') or true_input == str('mag') or true_input == str('magic'):
        print('balls')
    else:
        equation_time()  # this might be bad, but it's the only way I can loop this lol


def player_hp():
    try:
        player_health = input('Enter HP of user: ')
        return int(player_health)
    except:
        player_hp()


def player_sp():
    try:
        player_mana = input('Enter SP of user: ')
        return int(player_mana)
    except:
        player_sp()


def enemy_hp():
    try:
        player_health = input('Enter HP of target: ')  # too lazy to change variable name
        return int(player_health)
    except:
        enemy_hp()


def phys_list():
    move_id = input('Enter move (full name): ')
    phys_1 = Physical("test move", 1, 50, 20, 'None')
    phys_2 = Physical("tes2", 1, 90, 40, 'None')
    move_list = (phys_1, phys_2)  # this is horrible for the full gamut of spells we'll probably have
    # future Az consider replacing this with a nice file reference system
    for i in move_list:
        try:
            move_name = i.move_name
            if move_name.lower() == move_id.lower():
                return i
        except AttributeError:
            phys_list()
        except TypeError:
            phys_list()


def hp_cost_percent_calc(chosen_move):
    try:
        cost_percent = chosen_move.hp_cost_percent
    except AttributeError:
        print('Not found! Try again.')
        chosen_move = phys_list()
        move = hp_cost_percent_calc(chosen_move)
        return move
    except TypeError:
        print('Not found! Try again.')
        chosen_move = phys_list()
        move = hp_cost_percent_calc(chosen_move)
        return move
    else:
        cost_total = float(cost_percent / WHOLE)
        return cost_total


def init_bas_damage(target_health):
    weapon_power = input('Enter weapon strength: ')  # placeholder? replace with function that references a weapon list?
    user_power = input('Enter user strength: ')


def init_phys_damage(chosen_move, target_health):
    math.sqrt(chosen_move.atk_power)


def basboi():
    target_health = enemy_hp()
    print('Target has', )


def physboi():
    user_health = player_hp()
    target_health = enemy_hp()
    chosen_move = phys_list()
    cost_total = hp_cost_percent_calc(chosen_move)
    # while cost_total is None:
    #     cost_total = hp_cost_percent_calc()
    health_cost = math.floor(cost_total * user_health)
    user_health_left = user_health - health_cost
    print('User has', user_health_left, 'HP left.')
    print('Target has')
    # print(user_health_left)
    # print(health_cost)  # debug


def buff_check(initial_damage):
    damage_mod = 1
    tarukaja_check = int(input('How many Tarukaja in effect? (0 if none): '))
    damage_mod *= math.pow(TARU, tarukaja_check)
    total_damage = damage_mod * initial_damage
    print(total_damage) # debug

#     double Yo = math.sqrt(Atk);
#     System.out.print("Enter End of Target: ");
#     double Res = input.nextDouble();
#     //  System.out.print("Enter Armor Def (put 0 if not applicable): ");
#     //  double Arm = input.nextDouble();
#     System.out.print("Enter Power of Skill/Strength of Weapon: ");
#     double Pwr = input.nextDouble();
#     double a = Res * 2;
#     //  double Pog = a + Arm;
#     // double Def = Math.sqrt(Pog);
#     double Def = Math.sqrt(a);
#     double BaseDam = Yo * Pwr;
#     System.out.print("Enter User/Muse level: ");
#     double ax = input.nextDouble();
#     System.out.print("Enter Persona level (if none/starter, reinput User level): ");
#     double ar = input.nextDouble();
#     System.out.print("Enter Enemy level (if it's a player, JUST Muse lvl): ");
#     double grim = input.nextDouble();
#     double gaming = ax + ar;
#     double gramb = gaming / 2;
#     double Mod = gramb / grim;
#     System.out.print("Enter Hits: ");
#     double Hits = input.nextDouble();
#     System.out.print("Apply any effects (normal = 1, weakness = 1.4, resist/guarded = 0.5, crit = 2): ");
#     double Eff = input.nextDouble();
#     System.out.print("Enter Rnd (use random.org or think of a random value between .97 and 1.03): ");
#     double Rnd = input.nextDouble();
#     double es = BaseDam / Def;
#     double e = es * Mod * Hits * Eff * Rnd;
#     long z = Math.round(e);
#     long xer = Math.round(HP - z);
#     System.out.println(z + " damage means...");
#     System.out.println(xer + " health left! That's poggers!");
# }
#
# public static void Gamer() {
#     Scanner input = new Scanner(System.in);
#     System.out.print("Enter HP of Target: ");
#     double HP = input.nextDouble();
#     System.out.print("Enter Mag of User: ");
#     double Atk = input.nextDouble();
#     System.out.print("Enter End of Target: ");
#     double Res = input.nextDouble();
#     //   System.out.print("Enter Armor Def (put 0 if not applicable): ");
#     //  double Arm = input.nextDouble();
#     System.out.print("Enter Power of Skill: ");
#     double Pwr = input.nextDouble();
#     double helix = Atk / 8;
#     double To = Pwr * helix;
#     double a = Res * 2;
#     //  double Pog = a + Arm;
#     //   double Def = Math.sqrt(Pog);
#     double Def = Math.sqrt(a);
#     double BaseDam = To + Pwr;
#     System.out.print("Enter User/Muse level: ");
#     double ax = input.nextDouble();
#     System.out.print("Enter Persona level (if none, reinput User level): ");
#     double ar = input.nextDouble();
#     System.out.print("Enter Enemy level (if it's a player, JUST Muse lvl): ");
#     double grim = input.nextDouble();
#     double gaming = ax + ar;
#     double gramb = gaming / 2;
#     double Mod = gramb / grim;
#     System.out.print("Enter Hits: ");
#     double Hits = input.nextDouble();
#     System.out.print("Apply any effects (normal = 1, weakness = 1.4, resist/guarded = 0.5, crit = 2): ");
#     double Eff = input.nextDouble();
#     System.out.print("Enter Rnd (use random.org or think of a random value between .97 and 1.03): ");
#     double Rnd = input.nextDouble();
#     double es = BaseDam / Def;
#     double e = es * Mod * Hits * Eff * Rnd;
#     long z = Math.round(e);
#     long xer = Math.round(HP - z);
#     System.out.println(z + " damage means...");
#     System.out.println(xer + " health left! That's poggers!");


if __name__ == '__main__':
    main()
