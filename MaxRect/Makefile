TARGET=MaxRect

.PHONY: test

all : $(TARGET).so test

$(TARGET).o :
	g++ -c -fPIC $(TARGET).cpp -o $(TARGET).o

$(TARGET)_wrap.cxx:
	swig -c++ -python $(TARGET).i

$(TARGET).so: $(TARGET).o $(TARGET)_wrap.cxx
	g++ -c -fPIC $(TARGET)_wrap.cxx  -I/usr/include/python3.6 -I/usr/lib/python3.6
	g++ -shared -Wl,-soname,_$(TARGET).so -o _$(TARGET).so $(TARGET).o $(TARGET)_wrap.o

test:
	g++ test.cpp $(TARGET).cpp -o test-cpp
	@echo
	@echo "Testing cpp code..." 
	@./test-cpp
	@echo "Done!"
	@echo
	@echo "Test py-cpp wrapper..." 
	@./test.py
	@echo "Done!"


clean: 
	rm *wrap*
	rm *.o
	rm __pycache__ -rf
	rm $(TARGET).py
	rm *.so
	rm test-cpp