install_location="${PREFIX}/opt/auto/07p"

buildroot="${PWD}"
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
#
# Some ideas are taken from AUR:
# https://aur.archlinux.org/packages/auto-07p

make

# There is no "make install" so it has to be done manually:
mkdir --verbose --parents "${install_location}"
cp --verbose --archive --target-directory="${install_location}" .

# Install AUTO environment variable setup script:
# https://conda.io/docs/user-guide/tasks/manage-environments.html#macos-and-linux
activate_dir="${PREFIX}/etc/conda/activate.d"
mkdir --verbose --parents "${activate_dir}"
cp --verbose --target-directory="${activate_dir}" \
   "${RECIPE_DIR}/activate-auto.sh"

# Install auto-shim/auto.py as a proper Python package so that
# standard import "works":
cd "${buildroot}"
cp --verbose --recursive "${RECIPE_DIR}/auto-shim" .
cd auto-shim
"${PYTHON}" setup.py install \
    --single-version-externally-managed --record=record.txt
# https://conda.io/docs/user-guide/tutorials/build-pkgs.html
