class DynamicArray {

    private int [] baseArr;
    private int length;
    private int curr;
    private int els;

    public DynamicArray(int capacity) {
       baseArr = new int[capacity];
       curr = -1;
       els = 0;
       length = capacity; 
    }

    public int get(int i) {
        return baseArr[i];
    }

    public void set(int i, int n) {
            baseArr[i] = n;
            if (i > curr) {
                curr = i;
            }
    }

    public void pushback(int n) {
        if(curr == length-1) {
            resize();
        }
        baseArr[++curr] = n;
        els++;
    }

    public int popback() {
        els--;
        return baseArr[curr--];
        
    }

    private void resize() {
        int[] replaceArr = new int[length*2];
        for(int i = 0; i< length; i++) {
            replaceArr[i] = baseArr[i];
        }
        length *= 2;
        baseArr = replaceArr;

    }

    public int getSize() {
        return els;
    }

    public int getCapacity() {
        return length;
    }
}
