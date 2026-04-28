import java.time.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Введите день: ");
        int day = sc.nextInt();

        System.out.print("Введите месяц: ");
        int month = sc.nextInt();

        System.out.print("Введите год: ");
        int year = sc.nextInt();

        LocalDate date = LocalDate.of(year, month, day);

        System.out.println("День недели: " + getDayOfWeek(date));

        System.out.println("Високосный год: " + (isLeap(year) ? "Да" : "Нет"));

        System.out.println("Возраст: " + getAge(date));

        System.out.println("\nДата звездочками:");
        printDateWithStars(day, month, year);
    }

    public static String getDayOfWeek(LocalDate date) {
        switch (date.getDayOfWeek()) {
            case MONDAY:
                return "Понедельник";
            case TUESDAY:
                return "Вторник";
            case WEDNESDAY:
                return "Среда";
            case THURSDAY:
                return "Четверг";
            case FRIDAY:
                return "Пятница";
            case SATURDAY:
                return "Суббота";
            case SUNDAY:
                return "Воскресенье";
            default:
                return "Неизвестно";
        }
    }

    public static boolean isLeap(int year) {
        return Year.isLeap(year);
    }

    public static int getAge(LocalDate birthDate) {
        return Period.between(birthDate, LocalDate.now()).getYears();
    }

    static String[][] digits = {
            {" *** ", "*   *", "*   *", "*   *", " *** "}, //0
            {"  *  ", " **  ", "  *  ", "  *  ", " *** "}, //1
            {" *** ", "*   *", "   * ", "  *  ", "*****"}, //2
            {" *** ", "    *", " *** ", "    *", " *** "}, //3
            {"*   *", "*   *", "*****", "    *", "    *"}, //4
            {"*****", "*    ", "**** ", "    *", "**** "}, //5
            {" *** ", "*    ", "**** ", "*   *", " *** "}, //6
            {"*****", "    *", "   * ", "  *  ", "  *  "}, //7
            {" *** ", "*   *", " *** ", "*   *", " *** "}, //8
            {" *** ", "*   *", " ****", "    *", " *** "}  //9
    };

    public static void printDateWithStars(int day, int month, int year) {
        String date = String.format("%02d%02d%04d", day, month, year);

        for (int row = 0; row < 5; row++) {
            for (char c : date.toCharArray()) {
                int digit = c - '0';
                System.out.print(digits[digit][row] + " ");
            }
            System.out.println();
        }
    }
}