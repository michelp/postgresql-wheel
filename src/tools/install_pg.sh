if [[ $1 =~ refs/tags/([0-9]+\.[0-9]+).*$ ]];
then
    VERSION=${BASH_REMATCH[1]}
    echo "Building ${VERSION}"
else
    VERSION=13.4
fi

export DEBIAN_FRONTEND=noninteractive

sudo apt update
sudo apt install -y zlib1g-dev libreadline-dev libossp-uuid-dev libxml2-dev libxslt1-dev curl make gcc
curl -L -O https://ftp.postgresql.org/pub/source/v${VERSION}/postgresql-${VERSION}.tar.gz

tar -xzf postgresql-${VERSION}.tar.gz
cd postgresql-${VERSION}
./configure --prefix=`pwd`/../src/postgresql --with-ossp-uuid --with-libxml --with-libxslt
make -j 4 world-bin
make install-world-bin
cd ..

