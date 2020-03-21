COMPILING
    - javac "com/rmi/rmiinterface/RMIInterface.java" 
    - javac "com/rmi/rmiserver/SearchStudent.java"
    - javac "com/rmi/rmiserver/ServerOperation.java" 
    - javac "com/rmi/rmiclient/ClientOperation.java"

HOW TO RUN
    - rmic com.rmi.rmiserver.SearchStudent 
    - start rmiregistry (on windows)
        or
            rmiregistry (on mac and linux (maybe???))
    - java com/rmi/rmiserver/ServerOperation
    - java com/rmi/rmiclient/ClientOperation
    - type a student code and ta-da

Ma sinh vien co trong database: 16020111, 16020112, 17020111, 18020112
Tra ve "Invalid student code format" khi nhan duoc ma sinh vien khong phai so
Tra ve "Not Found" neu khong tim thay ma sinh vien

