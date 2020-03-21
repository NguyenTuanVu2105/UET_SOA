package com.rmi.rmiserver;
import java.rmi.*; 
import java.rmi.registry.*; 
import com.rmi.rmiinterface.RMIInterface;

public class ServerOperation 
{ 
    public static void main(String args[]) 
    { 
        try
        { 
            RMIInterface obj = new SearchStudent(); 
            LocateRegistry.createRegistry(2020); 
            Naming.rebind("rmi://localhost:2020"+ 
                          "/search-student", obj); 
        } 
        catch(Exception ae) 
        { 
            System.out.println(ae); 
        } 
    } 
} 