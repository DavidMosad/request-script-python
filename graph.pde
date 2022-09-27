JSONObject json;

void setup() {
  size(3000, 1000);
  background( random (254), random (254), random (254));
  json = loadJSONObject("./data.json");
  frameRate(1);
}

void draw() {
  
    String[] keys;
    keys = (String[]) json.keys().toArray(new String[json.size()]);
  
    stroke(255, 153, 230);
    strokeWeight(6);

//abscisse
    line(50, height-50, width-50, height-50);
    line(width-50,height-58,width-50,height-43);
    line(width-50,height-58,width-40,height-51);
    line(width-50,height-43,width-40,height-51);
//ordonnée
    line( 50, height-50, 50, 50);
    line( 45, 50, 55, 50);
    line( 45, 50, 50, 40);
    line( 55, 50, 50, 40);
  
  
  for (int i=0; i < json.size(); i++) {
    stroke(random(254), random(254), random(254));
    strokeWeight(2);
    JSONObject xhandled = json.getJSONObject(keys[i]);
    String[] timekeys;
    timekeys = (String[]) xhandled.keys().toArray(new String[xhandled.size()]);
    int timeweight = int(timekeys[0]);
    noFill();
    beginShape();
    for (int j=0; j < (xhandled.size()); j++){
      /*String timestamp = timekeys[j];
      int iterf = (height-(xhandled.getInt(timekeys[j])*((height-100)/6)));
      int iters = (height-(xhandled.getInt(timekeys[j+1])*((height-100)/6)));
      int xf = (int(timekeys[j])-timeweight);
      int xs = (int(timekeys[j+1])-(int(timekeys[j])));
      line( xf+50,iterf,xs+50,iters);
      */
      int y = (height-(xhandled.getInt(timekeys[j])*((height-100)/6)));
      int x = (int(timekeys[j])-timeweight);
      vertex(x,y);
      timeweight = int(timekeys[j]);
      print(" x=");
      print(timeweight);
    }
    endShape();
  }
}
