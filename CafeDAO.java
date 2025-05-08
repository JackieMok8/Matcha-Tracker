import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class CafeDAO {
    public void addCafe(Cafe cafe) {
        String sql = "INSERT INTO cafes (name, city, address, visiting_date, order_taken, price, rating, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";

        try (Connection conn = DBConnection.getConnection();
             PreparedStatement stmt = conn.prepareStatement(sql)) {

            stmt.setString(1, cafe.getName());
            stmt.setString(2, cafe.getCity());
            stmt.setString(3, cafe.getAddress());
            stmt.setDate(4, Date.valueOf(cafe.getVisitingDate()));
            stmt.setString(5, cafe.getOrderTaken());
            stmt.setDouble(6, cafe.getPrice());
            stmt.setDouble(7, cafe.getRating());
            stmt.setString(8, cafe.getNotes());

            stmt.executeUpdate();
            System.out.println("Café toegevoegd!");
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    public List<Cafe> getAllCafes() {
        List<Cafe> cafes = new ArrayList<>();
        String sql = "SELECT * FROM cafes";

        try (Connection conn = DBConnection.getConnection();
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {

            while (rs.next()) {
                Cafe cafe = new Cafe(
                    rs.getString("name"),
                    rs.getString("city"),
                    rs.getString("address"),
                    rs.getDate("visiting_date").toString(),
                    rs.getString("order_taken"),
                    rs.getDouble("price"),
                    rs.getDouble("rating"),
                    rs.getString("notes")
                );
                cafes.add(cafe);
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return cafes;
    }
}
