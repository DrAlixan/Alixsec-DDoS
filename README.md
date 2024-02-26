usage: alixsec-DDoS.py [-h] [-method METHOD] [-example EXAMPLE] m u p t r

positional arguments:
  m                 METHOD
  u                 ENTER TARGET WITH HTTP , HTTPS
  p                 ENTER PORT [HTTP = 80 HTTPS = 443]
  t                 THREADS | MAX = UNLIMITED
  r                 RPC | MAX = UNLIMITED

options:
  -h, --help        show this help message and exit
  -method METHOD    METHODS || kill , kill+
  -example EXAMPLE  example : python alixsec-DDoS.py kill http://example.com 80
                    1000 1000
