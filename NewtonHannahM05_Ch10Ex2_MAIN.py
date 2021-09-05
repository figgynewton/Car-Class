Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_car = Car('Ford', '1967 Bronco')
>>> print('\033[4mTime (s)\033[0m    \033[4mSpeed (mph)\033[0m')
[4mTime (s)[0m    [4mSpeed (mph)[0m
>>> for i in range(5):
	my_car.accelerate()
	speed = my_car.get_speed()
	print(format(i+1, '4d'), format(speed, '13d'))

	
   1             5
   2            10
   3            15
   4            20
   5            25
>>> for i in range(5):
	my_car.brake()
	speed = my_car.get_speed()
	print(format(i+6, '4d'), format(speed, '13d'))

	
   6            20
   7            15
   8            10
   9             5
  10             0
>>> 
