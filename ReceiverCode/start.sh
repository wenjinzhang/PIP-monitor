# g++ -g -std=gnu++0x -o pip_sense2.v2 pip_sense_layer.v2.cpp pip_socket.cpp -lusb -lssl -lcrypto
sudo stdbuf -o0 ./pip_sense2.v2 l l | stdbuf -o0 grep TX:03407