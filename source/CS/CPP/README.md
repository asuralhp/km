# C



## Basic
### stdlib
- std::any typically has a small inline buffer but its size is not guaranteed.

### Class
- Initializer List :
```
class Point {
private:
    int x;
    int y;
 
public:
    Point(int i = 0, int j = 0): x(i), y(j) {}
    /*  The above use of Initializer list is optional as the
        constructor can also be written as:
        Point(int i = 0, int j = 0) {
            x = i;
            y = j;
        }
    */
 
    int getX() const { return x; }
    int getY() const { return y; }
};
```