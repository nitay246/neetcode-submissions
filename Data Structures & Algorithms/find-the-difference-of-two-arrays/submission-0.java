class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> res1 = new HashSet<>();
        Set<Integer> res2 = new HashSet<>();
        for (int i = 0; i < nums1.length; i++){
            res1.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++){
            res2.add(nums2[i]);
        }
        Set<Integer> res11 = new HashSet<>(res1);
        Set<Integer> res22 = new HashSet<>(res2);

        for (int a : res1){
            if (res2.contains(a)) {
                res11.remove(a);
            } 
        }
        for (int a : res2){
            if (res1.contains(a)) {
                res22.remove(a);
            } 
        }
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<>(res11));
        result.add(new ArrayList<>(res22));
        return result; 
    }
}
