public class LinearSearch {

    public static void demo(Integer key) {
        System.debug('Linear search');
        
        List<Integer> lon = new List<Integer>();
        lon.add(3);
        lon.add(4);
        lon.add(5);
        lon.add(6);
        
        System.debug('List: ' + lon);
        
        Integer s = -1;
        
        for (Integer i = 0; i < lon.size(); i++) {
            if (key == lon[i]) {
                s = 1;
                break; // Break the loop once the element is found
            }
        }
        
        if (s == 1) {
            System.debug('Element Found');
        } else {
            System.debug('Element Not Found');
        }
    }
}
