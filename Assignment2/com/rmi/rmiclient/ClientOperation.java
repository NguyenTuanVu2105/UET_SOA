package com.rmi.rmiclient;

import java.net.MalformedURLException;
import java.rmi.Naming;
import java.rmi.NotBoundException;
import java.rmi.RemoteException;
import com.rmi.rmiclient.ClientStudent;
import com.rmi.rmiinterface.IStudent;
import javax.swing.JOptionPane;

import com.rmi.rmiinterface.RMIInterface;

public class ClientOperation {
	private static RMIInterface look_up;

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {
		
		look_up = (RMIInterface) Naming.lookup("rmi://localhost:2020"+ 
                          "/search-student");
		String studentCode = JOptionPane.showInputDialog("What is your student code?");
			
		IStudent istudent = look_up.getStudentInfor(studentCode);
		
		System.out.print("Name: " + istudent.getName() + "\n"); 
		System.out.print("Code: " + istudent.getStudentCode() + "\n"); 
		System.out.print("Class: " + istudent.getStudentClass() + "\n"); 
		System.out.print("Address: " + istudent.getAddress() + "\n"); 
		System.out.print("Error: " + istudent.getError() + "\n"); 

		ClientStudent student_response = new ClientStudent(istudent);
		JOptionPane.showMessageDialog(null, "Name: " + student_response.getName() + "\n" +
											"Code: " + student_response.getStudentCode() + "\n" +
											"Class: " + student_response.getStudentClass() + "\n" +
											"Address: " + student_response.getAddress() + "\n" +
											"Error: " + student_response.getError() + "\n" +
											"Summary: " + student_response.toString());
	}
}
