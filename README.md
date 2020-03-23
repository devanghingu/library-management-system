# library-management-system
library management system for practice

```

Number of Model 
_______________________
Profile
    Address
    mobile number
    totol book issued 

_______________________    
Book Category
    id
    category name
    book_count
_______________________
Book Information
    id
    title
    auther      (name may be future it will be connected with [auther model])
    quantity    number of quantity of specific book
    book category -> to book category
    available   required [how manfy book available]
    issued      default 0
    
_______________________
Transation
    id
    book_id     [ref to book table]
    issue_by    [to user table]
    waiting     [True if books not available/ default false]
    issue date
    due date
    
    returned_date
    retuend     [true | False()]
    
 ```
