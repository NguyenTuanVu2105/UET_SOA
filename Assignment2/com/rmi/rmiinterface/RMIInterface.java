package com.rmi.rmiinterface;
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RMIInterface extends Remote {
    public String getStudentInfor(String studentCode) throws RemoteException;
}