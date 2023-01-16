# Projet IML

Membre de groupe: Mohamed OUTLOUHOU & Ndeye-Maguette DIAGNE

## Description des objectifs

L’objectif de notre projet est de créer un robot interactif qui peut explorer une zone, un lieu en éxécutant des commandes vocales, au lieu d'un joystick. Exemple: « Aller tout droit » le robot doit aller tout droit de sa position. 

## Description de haut niveau

Pour ce faire, le fait de passer des commandes vocales, nous permet d’interagir avec le robot. Ce dernier doit identifier les mot, les verbes pour faire ce qu’on lui demande avec le traitement automatique de la langue naturelle. Puis un noeuds réstitue à partir de la séquence des mots l'action demandé, et la transmettre pour l'execution.

https://user-images.githubusercontent.com/74309471/212469031-63905d19-0c53-4ca7-80bd-d0aab75eb935.mp4

## Défis

Notre premier défis était de choisir un sujet. On a visité les sites de projet d’IA comme Kaggle pour avoir un sujet. Les sujets étaient intéressants soit on avait pas beaucoup de temps soit le sujet était complexe. Du coup on a du pour chaque aspect du projet trouver un sujet et à la fin en former un.
Pour traiter automatiquement le langage, on a eu des problèmes de version pour installer les bibliothèques SpeechRecognition et Pyttsx3. On a du changer notre version de pip et installer une autre bibliothèque intermediaire PyAudio pour que ça fonctionne.
Un deuxième défis était de connecter les deux parties; SpeechRecognition et Navigation. Pour cette dernière nous avons rencontré beaucoup de problème avec l'outil "TheConstructsim", pour simuler le robot. Et donc on choisi de remplacer l'outil de control "twist_keyboard" par contrôl par la voix.

 ## Travaux futurs

Le robot arrive à identifier les commandes vocales mais n’arrive pas à ce déplacer et exécuter les commandes. Si on avait plus de temps, on aurait du atteindre notre objectif de telle sorte que le robot puisse exécuter les commandes. Et dans un autre niveau spécifier au robot une distination et lui même y aller sans commande direct en donant des actions directes.

Retenues

* Le travail en groupe, le fait de pouvoir se diviser les taches et que chacun puisse faire dont il se sent à l’aise.
* Travailler en présentiel est beaucoup mieux pour communiquer avec ses co-équpiers, et aider les uns les autres pour atteindre l'objectif
