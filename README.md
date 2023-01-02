# Projet_GeCo_2022
Ce répertoire contient l'ensemble des codes et fichiers nécessaires pour la réalisation d'une analyse comparative entre Petrotoga mobilis, Petrotoga miotherma, Petrotoga halophila, Marinitoga piezophila et Marinitoga hydrogenitolerans.
 

<hr>
<b>Dossiers "genus-sp name" :</b>
<p> 
Les fichiers FTP décrits dans le rapport de Petrotoga mobilis, Petrotoga miotherma, Petrotoga halophila, Marinitoga piezophila et Marinitoga hydrogenitolerans sont contenus dans les dossiers au noms de ces dernieres (dossier nommé "ftp" disponnible dans chaque dossier).
Ces dossiers contiennent aussi, les sorties des outils cusp, compseq et cai du package emboss (fichiers "outfile cusp", "outfile compseq" et "outfile cai" respectivement) et un dossier "eggnog2" qui contient les resultats de EggNogMapperV2 
RQ:
Pour la bactérie d'interet (Petrotoga mobilis) on trouve à part les dossier "ftp" et "eggnog2", <b>2 autres dossiers en plus</b>:
Un dossier nommé "cog ncbi result" contenant le résultat de cog pour la bactérie d'interet petrotoga mobilis + Un dossier nommé "D-GENIES_RESULTS"
<hr>
<b>Dossier "Scripts" :</b>
<p>Contient les fichiers et les scripts pour réaliser les stats pour la signature génomique (dossier "Programs") Et un fichier nommé "COG_Stats_Script.py" qui est un script python pour realiser des stats sur les resultats eggnog</p>
 
<hr>
<b>Dossier "Blast" :</b>
<p>
 Ce dossier contient lui-meme 2 dossiers : 
 <br>
- Le dossier nommé "BLASTn" contient les fichiers cds_from_genomic.fasta de chaque espèces (origine: FTP) et qui vont servir à la réalisation d'un blastn en ligne de commande (70% id min et 70% min coverage) pour chacunes d'entre elles + calcul de l'ANI (fichier ANI.py) <br>
- Le dossier nommé "BLASTp" contient les fichiers protein.fasta (origine: FTP) de chaque espèces et qui vont servir à la réalisation d'un blastp en ligne de commande (30% id min et 80% min coverage) pour chacunes d'entre elles + calcul de l'AAI cette fois-ci (fichier AAI.py) </p>
<b>IMPORTANT :</b> codes_utilisés.txt dans chaque dossier contient les lignes de commandes nécessaires pour cette partie.
<hr>
<b>Dossier "OrthoVenn_res_files" :</b>
<p>Ce dossier contient les resultats de sortie de l'outil orthovenn2 en images : résumé (fichier : "summary.png"), tableau récapitulatif des clusters (fichier : "allclusters.png") et le diagramme de Venn (fichier : "JVenn_chart.png")</p>



# Author
Aimen CHERIF - M2DLAD
