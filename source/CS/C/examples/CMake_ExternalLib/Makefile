start: build_lib
	cmake -S . -B ./build 
	cmake --build ./build
	./build/HelloWorldEXE

build_lib:
	cmake -S ./lib -B ./lib/build
	cmake --build ./lib/build