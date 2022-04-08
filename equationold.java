import java.util.Scanner;

class FINALFINALEQUATION {
    public static void main(String[] args) {
        Yes();
    }

    public static void Yes() {
        Scanner input = new Scanner(System.in);
        System.out.print("Phys or Mag? (TYPE p OR m): ");
        String Type = input.nextLine();
        if (Type.equals("p")) {
            Physboi();
        }
        if (Type.equals("m")) {
            Gamer();
        }

    }

    public static void Physboi() {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter HP of Target: ");
        double HP = input.nextDouble();
        System.out.print("Enter Str of User: ");
        double Atk = input.nextDouble();
        double Yo = Math.sqrt(Atk);
        System.out.print("Enter End of Target: ");
        double Res = input.nextDouble();
        //  System.out.print("Enter Armor Def (put 0 if not applicable): ");
        //  double Arm = input.nextDouble();
        System.out.print("Enter Power of Skill/Strength of Weapon: ");
        double Pwr = input.nextDouble();
        double a = Res * 2;
        //  double Pog = a + Arm;
        // double Def = Math.sqrt(Pog);
        double Def = Math.sqrt(a);
        double BaseDam = Yo * Pwr;
        System.out.print("Enter User/Muse level: ");
        double ax = input.nextDouble();
        System.out.print("Enter Persona level (if none/starter, reinput User level): ");
        double ar = input.nextDouble();
        System.out.print("Enter Enemy level (if it's a player, JUST Muse lvl): ");
        double grim = input.nextDouble();
        double gaming = ax + ar;
        double gramb = gaming / 2;
        double Mod = gramb / grim;
        System.out.print("Enter Hits: ");
        double Hits = input.nextDouble();
        System.out.print("Apply any effects (normal = 1, weakness = 1.4, resist/guarded = 0.5, crit = 2): ");
        double Eff = input.nextDouble();
        System.out.print("Enter Rnd (use random.org or think of a random value between .97 and 1.03): ");
        double Rnd = input.nextDouble();
        double es = BaseDam / Def;
        double e = es * Mod * Hits * Eff * Rnd;
        long z = Math.round(e);
        long xer = Math.round(HP - z);
        System.out.println(z + " damage means...");
        System.out.println(xer + " health left! That's poggers!");
    }

    public static void Gamer() {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter HP of Target: ");
        double HP = input.nextDouble();
        System.out.print("Enter Mag of User: ");
        double Atk = input.nextDouble();
        System.out.print("Enter End of Target: ");
        double Res = input.nextDouble();
        //   System.out.print("Enter Armor Def (put 0 if not applicable): ");
        //  double Arm = input.nextDouble();
        System.out.print("Enter Power of Skill: ");
        double Pwr = input.nextDouble();
        double helix = Atk / 8;
        double To = Pwr * helix;
        double a = Res * 2;
        //  double Pog = a + Arm;
        //   double Def = Math.sqrt(Pog);
        double Def = Math.sqrt(a);
        double BaseDam = To + Pwr;
        System.out.print("Enter User/Muse level: ");
        double ax = input.nextDouble();
        System.out.print("Enter Persona level (if none, reinput User level): ");
        double ar = input.nextDouble();
        System.out.print("Enter Enemy level (if it's a player, JUST Muse lvl): ");
        double grim = input.nextDouble();
        double gaming = ax + ar;
        double gramb = gaming / 2;
        double Mod = gramb / grim;
        System.out.print("Enter Hits: ");
        double Hits = input.nextDouble();
        System.out.print("Apply any effects (normal = 1, weakness = 1.4, resist/guarded = 0.5, crit = 2): ");
        double Eff = input.nextDouble();
        System.out.print("Enter Rnd (use random.org or think of a random value between .97 and 1.03): ");
        double Rnd = input.nextDouble();
        double es = BaseDam / Def;
        double e = es * Mod * Hits * Eff * Rnd;
        long z = Math.round(e);
        long xer = Math.round(HP - z);
        System.out.println(z + " damage means...");
        System.out.println(xer + " health left! That's poggers!");
    }
}