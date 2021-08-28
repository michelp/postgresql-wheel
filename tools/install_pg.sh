if [[ $1 =~ refs/tags/([0-9]+\.[0-9]+).*$ ]];
then
    VERSION=${BASH_REMATCH[1]}
    echo "Building ${VERSION}"
else
    exit -1
fi

yum install -y zlib-devel readline-devel
curl -L -O https://ftp.postgresql.org/pub/source/v13.4/postgresql-${VERSION}.tar.gz

tar -xzf postgresql-${VERSION}.tar.gz
cd postgresql-${VERSION}
./configure --prefix=`pwd`/../postgresql/binary
make -j 4
make install
cd ..

