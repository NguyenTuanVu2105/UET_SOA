package com.rmi.rmiserver;
import com.rmi.rmiinterface.IStudent;

public class Student implements IStudent{
    String fullName = "";
    String className = "";
    String address = "";
    String studentCode = "";
    String error = "";

    public Student(String name, String studentCode, String className, String address){
        this.fullName = name;
        this.studentCode = studentCode;
        this.className = className;
        this.address = address;
    }

    public Student(String error) {
        this.error = error;
    }

    public String getName(){
        return this.fullName;
    }

    public String getStudentClass(){
        return this.className;
    }

    public String getAddress(){
        return this.address;
    }

    public String getStudentCode(){
        return this.studentCode;
    }

    public String getError(){
        return this.error;
    }

    @Override
    public String toString() {
        if (this.error == ""){
            return this.fullName + ", " + this.className + ", " + this.address + ", " + this.studentCode; 
        }
        else {
            return this.error;
        }
    }
}