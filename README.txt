fix-gp5.exe sert à corriger les pistes batteries mal enregistrées par les anciennes versions de
TuxGuitar. C'est un programme à lancer en ligne de commande qui s'utilise de la manière suivante :

    fix-gp5.exe fichier-à-corriger.gp5

Il est également possible de demander au programme de faire une copie corrigée du fichier plutôt
que de modifier le fichier source de la manière suivante :

    fix-gp5.exe fichier-à-corriger.gp5 -o fichier-corrigé.gp5

fix-gp5.exe cherche les pistes batterie à partir d'une liste de noms de pistes présente dans le
fichier drums-tracks.json du même dossier. Il est possible de rajouter des noms de pistes de
percussions à cette liste au besoin. Il est également possible de lui demander de chercher une
piste spécifique à corriger de la manière suivante :

    fix-gp5.exe fichier-à-corriger.gp5 -t NomDeLaPisteÀCorriger

C'est tout pour aujourd'hui ; si vous avez des questions, go Discord que c'est.
