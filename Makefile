TARGET=code

.PHONY: test

all : $(TARGET).so test

$(TARGET).o :
	g++ -c -fPIC $(TARGET).cpp

$(TARGET)-py-c-interface :
	swig -c++ -python $(TARGET).i

$(TARGET).so: $(TARGET).o $(TARGET)-py-c-interface
	g++ -c -fPIC $(TARGET)_wrap.cxx  -I/usr/include/python3.6 -I/usr/lib/python3.6
	g++ -shared -Wl,-soname,_$(TARGET).so -o _$(TARGET).so $(TARGET).o $(TARGET)_wrap.o

test:
	./test.py