import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.sql.*;
import java.util.Base64;
import java.util.Vector;


public class MySQLClient {

    public static Object texhnolyze(Connection connection) throws SQLException, IOException, ClassNotFoundException
    {
        PreparedStatement pstmt = connection.prepareStatement("select * from vampires");
        ResultSet rs = pstmt.executeQuery();

        Object deSerializedObject = null;

        while(rs.next())
        {
            System.out.println(rs.getString(1) + " " + rs.getString(2));

            byte decoded[] = Base64.getDecoder().decode(rs.getString(2));
            InputStream bb = new ByteArrayInputStream(decoded);

            ObjectInputStream objectIn = new ObjectInputStream(bb);
            deSerializedObject = objectIn.readObject();

            System.out.println("Java object de-serialized: "
                                + deSerializedObject + " ");
        }
        rs.close();
        pstmt.close();
        return deSerializedObject;
    }
    public static void main(String args[]){
        try{
            Class.forName("com.mysql.jdbc.Driver");
            Connection con = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/VAMPIRIC","edward","bella");

            Vector obj = new Vector();
            Vector objFromDatabase = (Vector) texhnolyze(con);

            System.out.println("did we crash");
            con.close();
        }catch(Exception e){ System.out.println(e);}
    }
}