# GoKeyBruter

**Basic Usage**
```
┌─[ParthSharma@HackBox] - [~/Tools/GoKeyBruter]
└─[2] python ~/Tools/GoKeyBruter/GoKeyBuster.py -g ~/GoProgs/bin/gokey -r google.com -p 6n,_Da5WYv -w /home/Parth/Tools/SecLists/Passwords/top_shortlist.txt 
[+] Found the master password! - test
```

**Setting the Verbosity Level**
```
┌─[ParthSharma@HackBox] - [~/Tools/GoKeyBruter] 
└─[0] python ~/Tools/GoKeyBruter/GoKeyBuster.py -g ~/GoProgs/bin/gokey -r google.com -p 6n,_Da5WYv -w /home/Parth/Tools/SecLists/Passwords/top_shortlist.txt  -v1
[*] Trying Password - password

[*] Trying Password - 123456

[*] Trying Password - 12345678

[*] Trying Password - abc123

[*] Trying Password - querty

[*] Trying Password - monkey

[*] Trying Password - letmein

[*] Trying Password - dragon

[*] Trying Password - 111111

[*] Trying Password - baseball

[*] Trying Password - iloveyou

[*] Trying Password - trustno1

[*] Trying Password - 1234567

[*] Trying Password - sunshine

[*] Trying Password - master

[*] Trying Password - 123123

[*] Trying Password - welcome

[*] Trying Password - shadow

[*] Trying Password - ashley

[*] Trying Password - footbal

[*] Trying Password - jesus

[*] Trying Password - michael

[*] Trying Password - ninja

[*] Trying Password - mustang

[*] Trying Password - password1

[*] Trying Password - test123

[*] Trying Password - test

[+] Found the master password! - test
```

**Brute Forcing the Realm and Password**
```
┌─[ParthSharma@HackBox] - [~/Tools/GoKeyBruter] 
└─[1] python ~/Tools/GoKeyBruter/GoKeyBuster.py -g ~/GoProgs/bin/gokey -r google.com -p "6n,_Da5WYv" -w /home/Parth/Tools/SecLists/Passwords/top_shortlist.txt  -v1 --brute-realm 1 --realm-list ./realm-list.txt  


[*] Trying Realm - google
[*] Trying Realm - gmail
[*] Trying Realm - gmail.com
[*] Trying Realm - google.com
[*] Trying Password - password1

[*] Trying Realm - google
[*] Trying Realm - gmail
[*] Trying Realm - gmail.com
[*] Trying Realm - google.com
[*] Trying Password - test123

[*] Trying Realm - google
[*] Trying Realm - gmail
[*] Trying Realm - gmail.com
[*] Trying Realm - google.com
[*] Trying Password - test

[*] Trying Realm - google
[*] Trying Realm - gmail
[*] Trying Realm - gmail.com
[*] Trying Realm - google.com
[+] Found the master password! [6n,_Da5WYv:google.com]
```

