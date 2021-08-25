yum install -y libreadline-devel zlib-devel

curl -L -O https://ftp.postgresql.org/pub/source/v13.4/postgresql-13.4.tar.gz

tar -xzf postgresql-13.4.tar.gz
cd postgresql-13.4
./configure --prefix=/usr/local
make -j 4
make install

cd ..

which ldconfig && ldconfig || true


