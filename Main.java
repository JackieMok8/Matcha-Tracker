import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CafeDAO dao = new CafeDAO();
        boolean running = true;

        System.out.println("🎋 Welkom bij Matcha Tracker!");

        while (running) {
            System.out.println("\nWat wil je doen?");
            System.out.println("1. Nieuw café toevoegen");
            System.out.println("2. Alle cafés bekijken");
            System.out.println("3. Afsluiten");
            System.out.print("> ");

            String keuze = scanner.nextLine();

            switch (keuze) {
                case "1":
                    System.out.println("➕ Nieuw café toevoegen:");

                    System.out.print("Naam café: ");
                    String name = scanner.nextLine();

                    System.out.print("Stad: ");
                    String city = scanner.nextLine();

                    System.out.print("Adres: ");
                    String address = scanner.nextLine();

                    System.out.print("Bezoekdatum (YYYY-MM-DD): ");
                    String visitingDate = scanner.nextLine();

                    System.out.print("Wat heb je genomen: ");
                    String orderTaken = scanner.nextLine();

                    System.out.print("Prijs (€): ");
                    double price = Double.parseDouble(scanner.nextLine());

                    System.out.print("Rating (1-10): ");
                    double rating = Double.parseDouble(scanner.nextLine());

                    System.out.print("Opmerkingen: ");
                    String notes = scanner.nextLine();

                    Cafe nieuwCafe = new Cafe(name, city, address, visitingDate, orderTaken, price, rating, notes);
                    dao.addCafe(nieuwCafe);
                    break;

                    case "2":
                    System.out.println("\n📋 Alle cafés:");
                    List<Cafe> alleCafes = dao.getAllCafes();
                
                    System.out.printf("%-20s %-15s %-10s %-10s\n", "Naam", "Stad", "Prijs (EUR)", "Rating");
                    System.out.println("-------------------------------------------------------------");
                
                    for (Cafe cafe : alleCafes) {
                        System.out.printf("%-20s %-15s %-10.2f %-10.1f\n",
                                cafe.getName(), cafe.getCity(), cafe.getPrice(), cafe.getRating());
                    }
                    break;
                
                case "3":
                    running = false;
                    System.out.println("Tot de volgende café-hop!");
                    break;

                default:
                    System.out.println("Ongeldige keuze, probeer het opnieuw.");
            }
        }

        scanner.close();
    }
}
