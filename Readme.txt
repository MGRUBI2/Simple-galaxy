1.0 verzija
gravitacija radi otprilike kako bi tribala(uz bugove)
tjela znaju ponekad dobit ogromnu brzinu kad se previse puta vrte medusobno
collision je aktivan samo na zvijezdi, planeti se nece medusobno unistavat(za sad)

bez pygame biblioteke neradi skripta(za postavit biblioteku u cmd upisat "pip install pygame.py")

za pokretanje simulacije treba se samo pokrenit Simple galaxy.py

Kontrole:
    -na lijevi klik misa se stvaraju planeti(ili meteori ili.....nez)
    -na lijevi shift se povecava velicina planeta
    -na lijevi ctrl se smanjiva velicina planeta
    -na lijevi alt se zaustavlja planet u pokretu
    -na strijelicu gore se mjenja planet koji ce se modificirat
    -na space se stvara zvijezda koja je nepomicna (puno veca masa za razliku od planeta)
    -na backspace se brise zvijezda iz sustava

Savjet:
    -za stabilnu orbitu oko zvijezde stvarajte vise planeta oko sunca tako da utjecu jedno na drugo i pocnu kruzit oko sunca
    inace ce direktno bit povuceno u zvijezdu.
    -ako stvorite planet pre daleko od zvijezde, zvijezda ce taj planet vjv katapultirat izvan mape
    -sta se stvori vise planeta to se oni vise medusobno ubrzavaju (na nelogican nacin, ovo je bug)



