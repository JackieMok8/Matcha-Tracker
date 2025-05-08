public class Cafe {
    private int id;
    private String name;
    private String city;
    private String address;
    private String visitingDate;
    private String orderTaken;
    private double price;
    private double rating;
    private String notes;

    public Cafe(String name, String city, String address, String visitingDate,
                String orderTaken, double price, double rating, String notes) {
        this.name = name;
        this.city = city;
        this.address = address;
        this.visitingDate = visitingDate;
        this.orderTaken = orderTaken;
        this.price = price;
        this.rating = rating;
        this.notes = notes;
    }

    // GETTERS
    public String getName() { return name; }
    public String getCity() { return city; }
    public String getAddress() { return address; }
    public String getVisitingDate() { return visitingDate; }
    public String getOrderTaken() { return orderTaken; }
    public double getPrice() { return price; }
    public double getRating() { return rating; }
    public String getNotes() { return notes; }
}
