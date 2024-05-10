public class LinearSearchExample {
    // Method to perform a linear search in an array
    public static Integer linearSearch(List<Integer> data, Integer target) {
        for (Integer i = 0; i < data.size(); i++) {
            if (data[i] == target) {
                return i;  // Return the index of the target element
            }
        }
        return -1;  // Return -1 if the target is not found
    }

    // Example usage of the linearSearch method
    public static void testLinearSearch() {
        List<Integer> numbers = new List<Integer>{10, 20, 30, 40, 50};
        Integer target = 30;
        Integer index = linearSearch(numbers, target);
        System.debug('Index of ' + target + ': ' + index);  // Should output: Index of 30: 2
    }
}
