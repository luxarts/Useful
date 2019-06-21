/*  RGB_Led_Smooth
 *  Author: Lucas M. Bacelo (www.github.com/luxarts)
 *  Description: Change the color of RGB led with 3 PWM outputs with a linear smooth animation.
 *  It uses the linear equation y=m.x+b to calculate the step size in each iteration so the three colors reach the target value at same time.
 */
#define PIN_RED   14
#define PIN_GREEN 12
#define PIN_BLUE  4

#define COLOR_BLACK     0
#define COLOR_RED       1
#define COLOR_ORANGE    2
#define COLOR_YELLOW    3
#define COLOR_LIME      4
#define COLOR_GREEN     5
#define COLOR_AQUA      6
#define COLOR_CYAN      7
#define COLOR_LIGHTBLUE 8
#define COLOR_BLUE      9
#define COLOR_PURPLE    10
#define COLOR_MAGENTA   11
#define COLOR_PINK      12
#define COLOR_WHITE     13

#define MAX_STEPS  93
#define DELAY_BETWEEN_STEPS 5

const uint16_t colors[14][3]={
  {0,0,0},        //BLACK
  {1023,0,0},     //RED
  {1023,511,0},   //ORANGE
  {1023,1023,0},  //YELLOW
  {511,1023,0},   //LIME
  {0,1023,0},     //GREEN
  {0,1023,511},   //AQUA
  {0,1023,1023},  //CYAN
  {0,511,1023},   //LIGHTBLUE
  {0,0,1023},     //BLUE
  {511,0,1023},   //PURPLE
  {1023,0,1023},  //MAGENTA
  {1023,0,511},   //PINK
  {1023,1023,1023}//WHITE
};

void setup() {
  Serial.begin(115200);
}

void loop() {
  changeColor(random(0,13));
  delay(2000);
}

void changeColor(uint8_t color){
  static uint8_t currentColor=0;
  float rgbStep[3]={0,0,0};
  uint16_t pwmValues[3]={0,0,0};

  //Don't calculate if same color
  if(color == currentColor)return;

  //Get 'm' component for each color
  rgbStep[0] = (float)(colors[color][0]-colors[currentColor][0])/(float)MAX_STEPS;
  rgbStep[1] = (float)(colors[color][1]-colors[currentColor][1])/(float)MAX_STEPS;
  rgbStep[2] = (float)(colors[color][2]-colors[currentColor][2])/(float)MAX_STEPS;

  //This loop blocks execution, would be better to do in a state machine
  for(uint16_t currentStep = 0 ; currentStep<=MAX_STEPS ; currentStep++){
    //Calculate PWM values
    pwmValues[0] = rgbStep[0]*(float)currentStep + colors[currentColor][0];
    pwmValues[1] = rgbStep[1]*(float)currentStep + colors[currentColor][1];
    pwmValues[2] = rgbStep[2]*(float)currentStep + colors[currentColor][2];

    //Print the values
    Serial.print(pwmValues[2]); //Blue line in serial plotter is the first value received
    Serial.print(",");
    Serial.print(pwmValues[0]);
    Serial.print(",");
    Serial.println(pwmValues[1]);

    //Put the values in the PWM pins
    analogWrite(PIN_RED, pwmValues[0]);
    analogWrite(PIN_GREEN, pwmValues[1]);
    analogWrite(PIN_BLUE, pwmValues[2]);

    delay(DELAY_BETWEEN_STEPS);
  }

  currentColor = color;
}
