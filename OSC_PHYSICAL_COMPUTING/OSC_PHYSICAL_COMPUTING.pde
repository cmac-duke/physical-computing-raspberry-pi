import oscP5.*;
import netP5.*;
String incomingValue; 
OscP5 oscP5;
NetAddress myRemoteLocation;
PFont f;

void setup() {
  size(1200, 800);
  frameRate(25);
  oscP5 = new OscP5(this,12000);
  myRemoteLocation = new NetAddress("127.0.0.1",12000);
}

void draw(){
  background(0); 
  textAlign(CENTER);
  textSize(80);
  if(incomingValue != null){
   fill(255);
   text(incomingValue, width/2, height/2);
   //img = list.getRandom();
  }
}


void oscEvent(OscMessage theOscMessage) {  
  if(theOscMessage.checkAddrPattern("/filter")==true) {
    incomingValue = theOscMessage.get(0).stringValue();
    println(" values: "+incomingValue);
    return;
  } 
  println("### received an osc message. with address pattern "+theOscMessage.addrPattern());
}