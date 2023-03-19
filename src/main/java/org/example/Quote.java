package org.example;

import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.ArrayList;

public class Quote {
    public ArrayList<Double> close;
    public ArrayList<Double> high;
    public ArrayList<Integer> volume;
    @JsonProperty("open")
    public ArrayList<Double> myopen;
    public ArrayList<Double> low;
}
