package com.rmi.rmiserver;
import java.rmi.*; 
import java.rmi.server.*;
import java.rmi.RemoteException;
import java.util.*;
import com.rmi.rmiinterface.RMIInterface;
import com.rmi.rmiserver.Student;
import com.rmi.rmiinterface.IStudent;

public class SearchStudent extends UnicastRemoteObject 
                         implements RMIInterface 
{ 
    SearchStudent() throws RemoteException 
    { 
        super(); 
        // declare a list of student information
        listStudent.put("16020111", new Student("Nguyen Van A", "16020111", "K61CB", "Ha Noi"));
        listStudent.put("16020112", new Student("Nguyen A B", "16020112", "K61CA", "HCM"));
        listStudent.put("17020111", new Student("Nguyen B C", "17020111", "K62T", "Da Nang"));
        listStudent.put("18020112", new Student("Nguyen C D", "18020112", "K63N", "Nha Trang"));
    } 
    
    static Map<String, IStudent> listStudent = new HashMap<String, IStudent>();

    //implementation of interface method
    public IStudent getStudentInfor(String studentCode) 
                       throws RemoteException 
    { 
        if (SearchStudent.isStudentCode(studentCode)) 
            if (listStudent.containsKey(studentCode) == true)
            {
                System.out.print("Name: " + listStudent.get(studentCode).getName()); 
                return listStudent.get(studentCode);
            }
            else
            {   
                // when studentCode not in database
                return new Student("Not Found");
            }
        else
        {
            // when studentCode is not double
            return new Student("Not Found");
        }
    } 
    
    private static boolean isStudentCode(String studentCode)
    {
        if (studentCode == null) 
        {
            return false;
        }

        try 
        {
            double d = Double.parseDouble(studentCode);
        } 
        catch (NumberFormatException nfe) 
        {
            return false;
        }
        return true;
    }
} 