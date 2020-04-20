package com.rmi.rmiinterface;
import java.io.Serializable;

public interface IStudent extends Serializable{
    public String getError();
    public String getName();
    public String getStudentClass();
    public String getAddress();
    public String getStudentCode();
}