echo "======== DJANGO: TEST HELLO WORLD ========"

wrk -d3s -t4 -c64 http://127.0.0.1:8000/hello/ | grep 'Requests/sec'

echo "======== FASTAPI: TEST HELLO WORLD ========"

wrk -d3s -t4 -c64 http://127.0.0.1:8000/api/hello | grep 'Requests/sec'

echo "======== DJANGO: TEST FETCH DATABASE ========"

wrk -d3s -t4 -c64 http://127.0.0.1:8000/fetch/ | grep 'Requests/sec'

echo "======== FASTAPI: TEST FETCH DATABASE ========"

wrk -d3s -t4 -c64 http://127.0.0.1:8000/api/fetch | grep 'Requests/sec'