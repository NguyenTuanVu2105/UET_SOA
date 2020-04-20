package com.rmi.rmiinterface;
import java.rmi.Remote;
import java.rmi.RemoteException;
import com.rmi.rmiinterface.IStudent;

public interface RMIInterface extends Remote {
    public IStudent getStudentInfor(String studentCode) throws RemoteException;
}