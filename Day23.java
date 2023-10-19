import java.util.ArrayList;
import java.util.List;

public class ManualStringSplit {
    public static void main(String[] args) {
        
        String inputString = "Hello ,World ,Java,Split,Example";
        char delimiter = ','; 

        List<String> substrings = new ArrayList<>();
        StringBuilder currentSubstring = new StringBuilder();

        for (char character : inputString.toCharArray()) {
            if (character == delimiter) {
                
                substrings.add(currentSubstring.toString());
                currentSubstring.setLength(0);  
                
            } else {
                
                currentSubstring.append(character);
            }
        }
        
        substrings.add(currentSubstring.toString());
        
        System.out.println("Original string: " + inputString);
        System.out.println("Split into substrings:");
        for (String substring : substrings) {
            System.out.println(substring);
        }
    }
}
