#GPIO Pins
#by Meg Gist
#Stolen by Rowan

declare -i c=10
#"declare -i" is needed for int variables
gpio mode 0 out

while [ $c -gt 0 ]
#while loops in bash have dumb formatting
do
gpio write 0 1
sleep 0.5
gpio write 0 0
sleep 0.5
#this turns the LEDs on and off each loop
declare -i c=c-1
#redeclare the counter variable each time
#and subtract by 1 so it works 10 times
done
