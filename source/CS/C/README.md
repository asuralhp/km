# C


## Basic

### Preprocessor
#### Directive

  - `#define PI 3.1415`
  - ```
    #define SWAP(x, y) \
      int tmp = x; \
      x = y; \
      y = tmp;
    ```
  - Confitional flow :
    ```
    #if defined(CALC_MODE)
        typedef MyCalcClass ChosenClass;
    #elif defined(USER_MODE)
        typedef MyUserClass ChosenClass;
    #else
        #error "Define CALC_MODE or USER_MODE"
    #endif
    ```
    - `#ifdef MACRO` vs `#if defined(MACRO)`:
      - Condition : `#if defined(WIN32) && !defined(UNIX)`
  - Define identifier without token : make `MACRO` is defined



### Memory

#### Automatic Reources Management
 - RAII
 - Smart Pointers
   - `unique_ptr`
   - `shared_ptr`

#### C memory function
 - `malloc`
 - `free`


## Library

### Tips
- Difference of standard library
    `<cstdlib>` | `<stdlib.h>`
    --          | --
    C++ header with namespace | C header
