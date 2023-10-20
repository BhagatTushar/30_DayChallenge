
import java.util.Scanner;

//number to roman no 


public class IntegerToRoman {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.print("Enter an integer (0 to 3999): ");
            int number = scanner.nextInt();

            if (number == 0) {
                System.out.println("Exiting the program.");
                break;
            }

            if (number < 1 || number > 3999) {
                System.out.println("Please enter a valid integer between 1 and 3999 or 0 to exit.");
            } else {
                String roman = intToRoman(number);
                System.out.println("Roman numeral: " + roman);
            }
        }

        scanner.close();
    }

    public static String intToRoman(int num) {
        String[] thousands = {"", "M", "MM", "MMM"};
        String[] hundreds = {"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
        String[] tens = {"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
        String[] ones = {"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};

        return thousands[num / 1000] +
               hundreds[(num % 1000) / 100] +
               tens[(num % 100) / 10] +
               ones[num % 10];
    }
}