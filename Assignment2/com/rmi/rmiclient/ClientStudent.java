package com.rmi.rmiclient;
import com.rmi.rmiinterface.IStudent;

public class ClientStudent implements IStudent{
    String fullName;
    String studentClass;
    String address;
    String studentCode;
    String error;

    ClientStudent(IStudent student){
        this.fullName = student.getName();
        this.studentClass = student.getStudentClass();
        this.address = student.getAddress();
        this.studentCode = student.getStudentCode();
        this.error = student.getError();
    }
    
    public String getName(){
        if (this.error.isEmpty()){
            return this.fullName + "_client";
        }
        else {
            return "";
        }
    }

    public String getStudentClass(){
        if (this.error.isEmpty()){
            return this.studentClass + "_client";
        }
        else {
            return "";
        }
    }

    public String getAddress(){
        if (this.error.isEmpty()){
            return this.address + "_client";
        }
        else {
            return "";
        }
    }

    public String getStudentCode(){
        if (this.error.isEmpty()){
            return this.studentCode + "_client";
        }
        else {
            return "";
        }
    }

    public String getError(){
        return this.error;
    }

    @Override
    public String toString() {
        if (this.error.isEmpty()){
            return this.fullName + ", " + this.studentClass + ", " + this.address + ", " + this.studentCode; 
        }
        else {
            return this.error;
        }
    }

}