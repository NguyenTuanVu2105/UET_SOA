package com.rmi.rmiserver;
import java.rmi.*; 
import java.rmi.server.*;
import java.rmi.RemoteException;
import java.util.*;
import com.rmi.rmiinterface.RMIInterface;

public class SearchStudent extends UnicastRemoteObject 
                         implements RMIInterface 
{ 
    SearchStudent() throws RemoteException 
    { 
        super(); 
        // declare a list of student information
        listStudent.put("16020111","Nguyen Van A, 16020111, K61CB");
        listStudent.put("16020112","Nguyen Van B, 16020112, K61CD");
        listStudent.put("17020111","Nguyen Tan B, 17020111, K61CCLC");
        listStudent.put("18020112","Nguyen Thi C, 18020112, K61CA");
    } 
    
    static Map<String, String> listStudent = new HashMap<String, String>();

    //implementation of interface method
    public String getStudentInfor(String studentCode) 
                       throws RemoteException 
    {
        String result; 
        if (SearchStudent.isStudentCode(studentCode)) 
            if (listStudent.containsKey(studentCode) == true)
            {
                return listStudent.get(studentCode);
            }
            else
            {   
                // when studentCode not in database
                return "Not Found";
            }
        else
        {
            // when studentCode is not double
            result = "Invalid studentCode format";
        }
        return result; 
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