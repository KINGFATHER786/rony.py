import os, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from enc1 import main

    main()

elif bit == '32bit':

    from enc2 import main

    main()
