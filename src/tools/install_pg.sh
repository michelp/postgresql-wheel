if [[ $1 =~ refs/tags/([0-9]+\.[0-9]+).*$ ]];
then
    VERSION=${BASH_REMATCH[1]}
    echo "Building ${VERSION}"
else
    VERSION=13.4
fi
JOBS_NUMBER=4
PROJ_VERSION=8.2.0
POSTGIS_VERSION=3.2.0

export DEBIAN_FRONTEND=noninteractive

sudo apt update
sudo apt install -y zlib1g-dev libreadline-dev libossp-uuid-dev libxml2-dev \
                    libxslt1-dev curl make gcc pkg-config libgeos-dev libxml2-utils \
                    libjson-c-dev proj-bin g++ libsqlite3-dev libtiff-dev \
                    libcurl4-gnutls-dev libprotobuf-c-dev libgdal-dev libsfcgal-dev

# Build Postgresql
curl -L -O https://ftp.postgresql.org/pub/source/v${VERSION}/postgresql-${VERSION}.tar.gz
tar -xzf postgresql-${VERSION}.tar.gz
cd postgresql-${VERSION}
./configure --prefix=`pwd`/../src/postgresql --with-ossp-uuid --with-libxml --with-libxslt
make -j ${JOBS_NUMBER} world-bin
make install-world-bin
cd ..

# Proj, need for PostGIS
curl -L -O https://download.osgeo.org/proj/proj-${PROJ_VERSION}.tar.gz
tar -xzvf proj-${PROJ_VERSION}.tar.gz
cd proj-${PROJ_VERSION}
./configure --prefix=`pwd`/../src/proj
make -j ${JOBS_NUMBER}
make install
cd ..

# PostGIS
curl -L -O https://download.osgeo.org/postgis/source/postgis-${POSTGIS_VERSION}.tar.gz
tar -xzvf postgis-${POSTGIS_VERSION}.tar.gz
cd postgis-${POSTGIS_VERSION}
./configure --with-pgconfig=`pwd`/../src/postgresql/bin/pg_config --with-projdir=`pwd`/../src/proj
make -j ${JOBS_NUMBER}
make install
cd ..
