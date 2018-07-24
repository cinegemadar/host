nav: src/nav.cpp src/nav_extern.cpp
	g++ -Iheader -shared -Wl,-install_name,libnav.so -o lib/libnav.so -fPIC src/nav.cpp src/nav_extern.cpp -v
clean:
	rm -f lib/libnav.so
