install_location="${PREFIX}/opt/auto/07p"

cd 07p

./configure \
    --with-optimization-flags=-std=legacy \
    --prefix="${install_location}"

# * The Fortran flag -std=legacy has to be specified to workaround the
#   error "dummy argument larger than actual argument":
#   https://gcc.gnu.org/bugzilla/show_bug.cgi?id=25071
#
# * FFLAGS=-std=legacy didn't work.
#
# * The option --prefix is passed anyway even though there is no "make
#   install" target.  It may be used somewhere in the code (see AUR).

make

# There is no "make install" so it has to be done manually:
mkdir --verbose --parents "${install_location}"
cp --verbose --archive --target-directory="${install_location}" .

# Some ideas are taken from AUR:
# https://aur.archlinux.org/packages/auto-07p
