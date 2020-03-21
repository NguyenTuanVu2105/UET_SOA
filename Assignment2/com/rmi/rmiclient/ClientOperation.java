package com.rmi.rmiclient;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

import javax.swing.JOptionPane;

import com.rmi.rmiinterface.RMIInterface;

public class ClientOperation {
	private static RMIInterface look_up;

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		
		look_up = (RMIInterface) Naming.lookup("rmi://localhost:2020"+ 
                          "/search-student");
		String studentCode = JOptionPane.showInputDialog("What is your student code?");
			
		String response = look_up.getStudentInfor(studentCode);
		JOptionPane.showMessageDialog(null, response);
	}
}
