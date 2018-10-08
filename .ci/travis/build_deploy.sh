
conda install -q conda-build anaconda-client

pip install twine wheel
RC=$?
if [ "$RC" -eq 1 ]; then
    exit 1
fi

python .ci/travis/anaconda_build.py
RC=$?
if [ "$RC" -eq 1 ]; then
    exit 1
fi

python .ci/travis/anaconda_upload.py
RC=$?
if [ "$RC" -eq 1 ]; then
    exit 1
fi


python .ci/travis/pypi_build.py
RC=$?
if [ "$RC" -eq 1 ]; then
    exit 1
fi

python .ci/travis/pypi_upload.py
RC=$?
if [ "$RC" -eq 1 ]; then
    exit 1
fi
