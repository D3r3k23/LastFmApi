if [ ! -d test/venv ]; then scripts/setuptest.sh; fi

cd test

echo Running tests without cache
venv/bin/python3 test --use_src
ret_code=$?

if [ $ret_code -eq 0 ]; then
    echo Running tests with cache
    venv/bin/python3 test --use_src --use_cache
    ret_code=$?
fi

cd ..

if [ $ret_code -eq 0 ]; then
    echo Tests passed
else
    echo Tests failed
fi
exit $ret_code
