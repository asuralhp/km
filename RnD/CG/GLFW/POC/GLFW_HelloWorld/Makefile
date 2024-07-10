C = clang++
APP_NAME = main
BUILD_DIR = ./bin
C_FILES = ./*.cpp

APP_DEFINES:=
APP_INCLUDES:= -I../GLFW/include/
APP_LINKERS:= -L../GLFW/lib/ -lglfw3 -framework Cocoa -framework IOKit

build:
	$(C) $(C_FILES) -o $ $(BUILD_DIR)/$(APP_NAME) $(APP_INCLUDES) $(APP_LINKERS)
	
run: build
	./bin/main