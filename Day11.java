import java.util.Scanner;

public class PrintNumbersInRange {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the low number: ");
        int low = scanner.nextInt();

        System.out.print("Enter the high number: ");
        int high = scanner.nextInt();

        if (low <= high) {
            System.out.println("Numbers between " + low + " and " + high + ":");
            for (int i = low; i <= high; i++) {
                System.out.println(i);
            }
        } else {
            System.out.println("Low number should be less than or equal to the high number.");
        }

        scanner.close();
    }
}
