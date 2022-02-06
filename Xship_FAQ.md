# Xship für Kodi -Deutsche Anleitung/ FAQ

![Xship logo](https://raw.githubusercontent.com/watchone/repository.xship/master/zips/repository.xship/icon.png)

- [1. Allgemeines zum Addon](#1-allgemeines-zum-addon)
    - [1.1 Verfügbare Webseiten](#11-verfügbare-webseiten)
    - [1.2 Rechtliche Konsequenzen bei Nutzung](#12-rechtliche-konsequenzen-bei-nutzung)
   
   
- [2. Installation und Konfiguration](#2-installation-und-konfiguration)
    - [2.1 Bezugsquellen zur Installation](#21-bezugsquellen-zur-installation)
    - [2.2 Allgemeine Einstellungen und Wiedergabe](#22-allgemeine-einstellungen-und-wiedergabe)
    - [2.3 Index Seiten Aktivieren und Deaktivieren](#23-index-seiten-aktivieren-und-deaktivieren)
    - [2.4 Hosterwahl](#24-hosterwahl)
    - [2.5 Konten](#25-konten)
    - [2.6 Downloads](#26-downloads)
    - [2.7 Resolver Konfiguration](#27-resolver-konfiguration)
    - [2.8 Gesehen Status in Xship ](#28-gesehen-status-in-xship)
    - [2.9 Plugin Video Themoviedb Helper](#29-plugin-video-themoviedb-helper)
    
- [3. Bekannte Probleme](#3-bekannte-probleme)
    - [3.1 Fehler bei der Installation](#31-fehler-bei-der-installation)
    - [3.2 Resolver Fehler](#32-resolver-fehler)
    - [3.3 Beobachtungen und Fehler im Betrieb](#33-beobachtungen-und-fehler-im-betrieb)
  
- [4. Fehlerbericht über Log-Datei](#4-fehlerbericht-über-log-datei)
    - [4.1 Allgemeines zur Log-Datei](#41-allgemeines-zur-log-datei)
    - [4.2 Speicherort der Log Datei](#42-speicherort-der-log-datei)
    - [4.3 Erstellen und Hochladen der Log-Datei](#43-erstellen-und-hochladen-der-log-datei)

    
- [5. Python Dateien](#5-python-dateien)
    - [5.1 Allgemeines zur .py-Datei](#51-allgemeines-zur-py-datei)
    - [5.2 Bearbeiten einer .py-Datei](#52-bearbeiten-einer-py-datei)
    - [5.3 Speicherort der einzelnen Webseiten (.py Dateien)](#53-speicherort-der-einzelnen-webseiten-py-dateien)




# 1. Allgemeines zum Addon

Dies Anleitung bezieht sich auf das Addon Xship

Xship ist ein Video Addon für die Media-Center-Software Kodi

Mit Xship ist es möglich über eine einfache Benutzeroberfläche mehrere Streaming-Seiten zu benutzen, um Filme und Serien anzuschauen

Dabei ist die wichtigste Eigenschaft von Xship, die Schnelligkeit der Suche und der Menünavigation

Xship greift bei Film/Serienauswahl oder einer Suche, zuerst auf eine Filmdatenbank zu (tmdb) zu und zeigt ein Ergebnis an

Erst nach der getroffenen Auswahl werden die Anbieter & Hoster durchsucht

Der Menüaufbau von Xship ist eigentlich selbsterklärend

Die Menüsprache von Xship ist Deutsch.

**Der Schwerpunkt von Xship liegt darin, die Indexseiten auf funktionierendem Stand zu Halten. Neue Funktionen wird es nicht geben, ausser das Team entschließt isch dazu**

Bei Problemen usw. kann über Issues Kontakt aufgenommen werden

Einstellungen welche in Xship gemacht werden, sind in einer sogenannten settings.xml gespeichert

Diese kann von einem System auf ein anderes kopiert werden um auch dort die gleichen Einstellungen (Konten usw.) zu haben

Die settings.xml von Xship findet man hier:

....kodi/userdata/addon_data/plugin.video.Xship

Der .kodi Ordner ist ein versteckter Ordner und muss in Windows  und Android erst sichtbar gemacht werden

Weiter Pfade stehen im Kap. 4.2

Bei Probleme hilft es sehr oft, den Kodi Cache zu löschen

## 1.1 Verfügbare Webseiten

Die Funktion der folgenden Seiten ist auf Grund fehlender Entwickler nicht immer gewährleistet

| Name           | Domain            | 
|:-------------- |:----------------- | 	
|Alleserien 	 |alleserien.com     | 
|FilmPalast      |filmpalast.to      | 
|Kinofox         |kinofox.de	     |
|Kinoger         |kinoger.to	     |
|Kinomax         |kinomax.me	     |
|Kinox		 |kinox.to	     |
|KKiste	         |kkiste.movie 	     |   
|Movie4k         |movie4k.one        | 
|Movietown  	 |movietown.org      |
|Netzkino	 |netzkino.de	     |
|Serienstream	 |serienstream.to    | 
|Streamworld	 |streamworld.in     |
|XCine		 |xcine.me	     |

Für die Verwendung von Serienstream.to, ist auf deren Homepage das Anlegen eines Benutzer Kontos erforderlich

Als E-Mailadresse kann auch eine Wegwerf-EMail-Adresse verwendet werden

## 1.2 Rechtliche Konsequenzen bei Nutzung

Der Europäische Gerichtshof hat ein Urteil gefällt: 
 
 - Der Nutzer muss sich in Anbetracht des neuen EuGH-Urteils stets über das zur Nutzung vorgesehene Angebot (Portal, Webseite) informieren – der Nutzer muss prüfen, ob das Angebot rechtswidrig ist oder sein könnte. 

 - Streamingseiten, die etwa brandaktuelle Kinofilme kostenlos anbieten, die man nicht mal bei den Bezahlanbietern zu sehen bekommt – hier hat man es wahrscheinlich mit einer „offensichtlich rechtswidrigen Vorlage“ zu tun. 
 
Wer sich hier Streams anschaut, macht sich strafbar und kann sich nicht auf das Recht auf Privatkopie berufen.

 - Zukünftige Streaming-Abmahnungen sind also durchaus möglich,eine neue Abmahnwelle ist dennoch nicht zu befürchten
Nutzer können nur über ihre IP-Adressen zurückverfolgt werden Genau diese IP-Adresse ist jedoch nur dem illegalen Portal bekannt, welches meist anonym operiert und oft keine IP-Adressen speichert

Die meisten Streaming-Seiten speichern keine Zugriffsdaten

Solltet Ihr einen Premium Dienst auf diversen Seiten nutzen, könnt Ihr natürlich leicht(er) gefunden werden

Hier ist ein Video von Rechtsanwalt Christian Solmecke, der über das Thema rechtlich aufklärt: Stand 26.April 2017


[![EuGH: Streaming| Rechtsanwalt Christian Solmecke](https://i.ytimg.com/vi/uzOA09gomn0/hqdefault.jpg)](https://www.youtube.com/watch?v=uzOA09gomn0&feature=youtu.be)

[![Jura Basics: Streaming](https://i.ytimg.com/vi/Efje_W9lo8E/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==&rs=AOn4CLCgeCmSb-HD6nPLKSWjVaQ-Uq6q9.jpg)](https://www.youtube.com/watch?v=Efje_W9lo8E)

# 2. Installation und Konfiguration

## 2.1 Bezugsquellen zur Installation

**Das hinzufügen von Xship über "als Quelle hinzufügen" in Kodi ist NICHT möglich!!!**

**!!!Wird das Xship Repository installiert, so ist man immer auf dem neusten Stand und alle Updates erfolgen darüber!!!**

**Info:** Das Deutsche Xship Project sucht Entwickler zur Pflege der Index Seiten, Kenntnisse Programmiersprache Python (.py) erforderlich

Updates werden über den bekannten Weg verteilt

Wollt Ihr nicht bis zu einem Update warten, kann in Xship die ~nightly Update Funktion verwendet werden

**Es wird Gujal00 als Quelle für den Resolver verwendet**

Von dort beziehen auch wir die Informationen

Xship und xStream verwenden den gleichen Resolver

**Installation erfolgt über das Kodi Menü:**

1. Addons - 'Aus Zip-Datei installieren'
2. repository.xship-1.x.zip auswählen und installieren 
3. Menüpunkt 'Aus Repository installieren' und xShip Repository auswählen
4. unter *Video-Addons* ist Xship dann zu finden

## 2.2 Allgemeine Einstellungen und Wiedergabe

Wenn gesehene Filme auf einmal weg sind, liegt das an den Einstellungen im Seitenmenü. 

Hier die Markierung „gesehene Filme“ deaktivieren!

In Xship  Kategorie *WERKZEUGE* öffnen

Hier werden alle Xship Einstellungen angezeigt

**Xship: Suchverlauf leeren**

Hierbei wird der gesamte Suchverlauf, bei Serien/Filme gelöscht

Möchte man nur einen Sucheintrag löschen, so ist dies über das Kontextmenü möglich, gewünschten Sucheintrag wählen und löschen

**Suche**

Die Suche in Xship ist eine Globale Suche

Das heißt, es werden immer alle Anbieter/Hoster durchsucht

Wird ein Ergebnis angezeigt, so bedeutet das noch nicht, dass auch ein Stream vorhanden ist (denn Xship durchsucht eine Datenbank)

Wird kein Ergebnis gefunden, so wird die Suche beendet und "Nichts gefunden" angezeigt

Es kann vorkommen, dass eine Serie/ein Film nicht gefunden wird, näheres dazu siehe Kapitel 3.3

**Nach welcher Logik werden Filme unter "neue Filme" aufgelistet**

Dort kommen nicht neueste Filme zuerst und nach hinten werden sie immer älter, sondern neue Filme stehen teilweise einfach irgendwo weiter unten in der Liste

Warum können Neuerscheinungen nicht einfach immer chronologisch von vorne ergänzt werden? 

*Antwort:*

Es zeigt die Filme des letztes Jahres (mit einer 60 tägigen Verzögerung, weil ein Film der heute ins Kino gekommen ist bringt meistens recht wenig)

Geordnet ist es nach Moviemeter

Wie genau das zusammen gesetzt ist kann bei IMDB nachgelesen werden

### Einstellungen Xship

**Allgemein**

***Standard Aktion:***

***Autoplay***

Es ist in der Xship möglich,  dass nach Ende der abgespielten Folge automatisch die nächste Folge abspielt wird

Hier für muss Autoplay eingestellt sein

Dann eine Folge nur markieren (noch nicht starten) und über das Kontext-Menü "Ab hier abspielen" wählen

So wird nach Ende der gewählten Folge, direkt die nächste gestartet

Es ist auch möglich z.B. den Film zu Starten und Autoplay macht den Rest, keine Hosterwahl nötug

***Verzeichnis/Dialog***

Hier ändert sich nur die Ansicht, wie die Anbieter/Hosterliste angezeigt wird. Manche Funktionen sind nur in der Verzeichnis Ansicht verfügbar (z.B. Kontextmenü)

***Zeitlimit für Index Seiten:***

*Standard (default):* 35 Sekunden

Ist die Zeit, wie lange Xship die Anbieter durchsuchen soll  bevor das Suchergebniss , als Liste zur Auswahl  angezeigt  wird

Wenn Ihr Schwierigkeiten habt Streams zu finden, kann dieser Wert erhöht werden

***Status Gesehen/Ungesehen***

*Standard (default):*beides aktiviert

Der gesehen Status wird innerhalb von Xship behandelt

***Fanart verwenden***

*Standard (default):* aktiviert

Wenn Ihr Probleme mit dieser Funktion habt, solltet Ihr überlegen diese zu deaktivieren um zu sehen, ob sich dadurch die Leistung verbessert

Dadurch verliert Ihr natürlich die Bilder und Kosmetische Aspekte. Aber es könnte zur Leistungsverbesserung beitragen

**Untertitel**

*Standard (default):* deaktiviert

Um Untertitel zu verwenden, wähle Untertitel aktivieren

Hauptsprache und Zweitsprache wählen

(Es ist jedoch möglich, dass diese Einstellung Funktionslos bleibt)

Während der Stream läuft könnt Ihr nun am unteren Rand, die Untertitel ein/ausschalten

**Updates /Wartung**

***Nightly Update***

Unter Werkzeuge - Einstellungen - Updates /Wartung findet Ihr die Funktion Nightly Updates

Diese Nightly Updates aktualisieren Xship und den URLResolver

Die ~Nightly ist eine Entwickler Version und kann auch Fehler beinhalten

### Einstellungen Wiedergabe

**Fortschrittsdialog**

Vordergrund: 

nach Streamauswahl wird das Info-Fenster, groß in der mitte des Bildschirmes dargestellt

Hintergrund: 

nach Streamauswahl wird das Info-Fenster, klein am Rand des Bildschirmes dargestellt

***Streamsuche vorzeitig abbrechen***

Wenn aktiviert, wird die Suche nach Streams bei dem eingestellten Wert abgebrochen

*Abbruch-Limit Streamsuche*

Hier wird eingestellt, nach wie vielen Hostern die Streamsuche abgebrochen wird.

Es zählt die höchste eingestellte Qualität

Beispiel 720p: Wird z.b. 5 eingestellt,so wird die Streamsuche nach 5 Quelle mit 720p abgebrochen

**Bei Wiedergabe-Start**

***Fortsetzen***

Wenn ein Stream gestoppt wird, wird automatisch  ein Fortsetzungspunkt gespeichert/erstellt (aber erst ab einer Wiedergabezeit von 3 Minuten )

*Option Wiedergabe fortsetzten EIN:*

Es erscheint bei Fortsetzung des Streams eine  Anzeige  wo gewählt werden kann: 

Fortsetzen oder Vom Anfang abspielen an, egal welcher Hoster dabei gewählt wird

*Option Wiedergabe fortsetzten AUS:*

Stream startet immer vom Anfang (auch wenn Ihr eine advancedsettings.xml verwendet)

***Automatisch Fortsetzen***

Angespielte Streams werden automatisch an der Stelle fortgesetzt, wo sie zuvor gestoppt wurden

**Dateianbieter-Filter**

***Höchste Qualität:***

4k, 1440p, 1080p, 720p und 480p stehen zur Auswahl

Das was hier engestellt wird, ist die max. Auflösung nach der die Index-Seiten durchsucht werden. 

Ist auch die max. Auflösung, welche bei Autoplay verwendet wird

Bei Seriesever ist 4k verfügbar, aber nur mit einem Premium Account (Bezahlung)

***Index-Seiten bei Serien nach Priorität sortieren***

Wenn aktiviert werden Anbieter welche nur Serien anbiten (z.B. Serienstream) oben angezeugt

***Index-Seiten nach Anbieter sortieren***

Wenn aktiviert, werden die Anbieter Alphabetsch gereit

## 2.3 Index Seiten Aktivieren und Deaktivieren

*Standard:* Alle Index Seiten aktiviert, außer die Seiten wo ein Benutzerkonto erforderlich ist (Serienstream)

In Xship, unter dem Menüpunkt Werkzeuge, *Index-Seiten*, besteht die Möglichkeit bestimmte Seiten an bzw. auszuschalten, wenn kein Interesse an bestimmten Seiten besteht

Diese werden dann auch nicht in der Suche angezeigt

*Anmerkung:*

Wenn Ihr Probleme mit Indexseiten Erreichbarkeit habt, hilft es wenn Ihr Eure DNS (z.B. auf die von Google 8.8.8.8) Adresse ändert

Manche Seiten werden von den Internet Providern geblockt 

Nache einem Xship Update werden auch neu hinzugefügte Seiten automatisch angezeigt

## 2.4 Hosterwahl

Wenn Ihr im Menü z.B. Filme- Jahr- 2017- beliebigen Film auswählen- klickt, werden alle verfügbaren Anbieter/Hoster durchsucht.

Auch nachdem eine Suche gestartet wurde, werden alle verfügbaren Anbieter/ Hoster angezeigt. 

Die Anzeige sieht wie Folgt aus:

Serienstream | VOE | HD | 5.1

(Anbieter | Hoster | Qualität|z.B Audio, optionale Zusatzinfo)

Die Qualität des Streams (als optionale Zusatzinfo) kann sein:  4k, HD, SD, CAM usw.

Wie lange das durchsuchen der Hoster dauert hängt von der Einstellung *Zeitlimit für Index Seiten* ab

*Wenn Ihr einen Film/Serie angewählt habt, könnt Ihr ein zusätzliches Menü (Kontexmenü) öffnen:*

am PC: rechte Maus Taste

am Handy/Tablet: langer Druck auf den Film

am FireTV: die Menü Taste drücken

Ist der von Euch gewählte Anbieter/Hoster nicht verfügbar, nimmt Xship AUTOMATISCH den nächsten, bis ein lauffähiger gefunden wird

***Anmerkung zu  Hostern mit Pairing z.B. Flashx:***

Wenn Ihr einen dieser Hoster zum Streamen auswählt, erscheint ein Fenster, welches Euch auffordert Eure Gerät zu Pairen

Das könnt ihr mit ruhigen Gewissen machen

Ihr müsst im selben WLAN sein wie das zu Pairende Gerät (z.B. FireTV, Apple TV usw.)

Für Flashx müsst Ihr Euch auf Flashx.tv/Flashx.sx ein Benutzerkonto anlegen, dafür kann auch eine Wegwerf E-Mailadresse verwendet werden

Öffnet am Handy/Tablet/PC einen Browser mit der angezeigten Adresse von z.B flashx (https://www.flashx.tv/pair oder www.flashx.sx/pair)

(Klickt in dem Kasten bei “Ich bin kein Roboter”)

Dann ganz runter und klick auf “Pair”

Das wars

Dieser Vorgang muss immer wieder Wiederholt werden (nach 3-4 Stunden oder 5 Streams)

*Warum ist das "pairen" nötig?*

Auf der Homepage muss immer eine Werbung betrachet werden

Da wir ja die Homepage des Hostbetreibers nicht besuchen müssen, entgehen dem Betreiber Werbeeinnahmen. 

Damit dies nicht der Fall ist und die Hoster Xship so arbeiten lassen, wurde mit den Betreibern diese "pair" Funktion vereinbart.

Durch den klick auf "pair" bekommen die Hoster Ihre Werbeeinnahme.

Für Euch entstehen dadurch KEINE Kosten!!

## 2.5 Konten

In dieser Einstellung, können Benutzerdaten von Webseiten eingetragen (z.B. Serienstream)

Voraussetzung ist natürlich, dass ein Konto vom jeweiligen Anbieter vorhanden ist

Bei vielen Anbietern, kann zur Registrierung eine Wegwerf E-Mailadresse verwendet werden, ggf. mehrere Anbieter probieren

Premiumdienste wie zum Beispiel RealDebrid, Premiumize usw. werden im URLResolver konfiguriert und in Xship dann farblich dargestellt

In Xship kann über *URLResolver Einstellungen-Universelle Resolver* darauf zugegriffen werden

**Fanart tv**

Auf der Homepage [https://fanart.tv/](https://fanart.tv/), durch klick auf Register, ein Benutzerkonto erstellen

Es kann auch eine Wegwerf/Einmal E-Mailadresse verwendet werden

An die angegebene E-Mailadresse wird ein Bestätigungslink geschickt

Nach dem Klick auf den Link, erfolgt eine Aufforderung, ein neues Passwort einzugeben. Durchführen und Klick auf *Reset Passwort*

Zurück zur Homepage und Einloggen

Am unteren Ende der Homepage steht API und *Create API Key*, auswählen

Klick auf *Generate Personal API Key*

Es wird nun der Fanart API Key angezeigt, welcher dann in Xship eingetragen wird

**Opensubtitles**

Für die Verwendung von Untertiteln in Xship, ist ein kostenloses Benutzerkonto von [www.opensubtitles.org ](www.opensubtitles.org)nötig

Die Webseite besuchen, ein Benutzerkonto erstellen und im Anschluss Benutzername und Passwort in den Xship Konto Einstellungen eintragen

**TMDB (The Movie Database)**

Auf [https://www.themoviedb.org/](https://www.themoviedb.org/) Registrieren und ein Benutzerkonto anlegen, Captcha lösen, fertig

Es kann eine Wegwerf E-Mailadresse verwendet werden, ggf mehrere Anbieter probieren

Es wird dann ein Bestätigungslink an die angegebene E-Mailadresse gesendet

Den Link in der E-Mail, in den Browser kopieren und Anmelden, Fertig

Das TMDB Konto ist nun erstellt

Xship verwendet einen allgemeinen TMDB API-Key, den ALLE User verwenden

Es kann jeder User einen persönlichen TMDB API-Key anfordern und diesen in Xship eintragen (z.B. wenn es Probleme mit den Artwork Bildern gibt)

*TMDB API-Key anfordern:*

- Mit Eurem Konto anmelden und rechts oben auf das "Benutzerssymbol" klicken

- Einstellungen wählen

- unter Settings, am linken Rand, API wählen

- auf "Create" klicken

- Developer wählen

-  Approve Terms of Use (AGB's), ganz unten Akzeptieren

- Es öffnet sich nun ein Fenster: API Schlüssel anfordern, wo die Eingabefelder mit erfundenen Daten ausgefüllt werden (somit gibt es keinen Bezug zu Eurer wahren Identität)

- im Anschluss auf "Erstellen" klicken

- nun wird unter Einstellungen - Settings - API - Details der  *API Schlüssel (v3 auth)* angezeigt. Dieser wird nun in Xship eingefügt

- unter "Stats" ist ersichtlich, wie viele Zugriffe es mit diesem API-Key gegeben hat

Dieser API Key kann auch im Metahandler eingetragen werden, wenn Ihr es möchtet (siehe weiter unten TVDB Konto)

## 2.6 Downloads

Diese Funktion ist mit/in der Bibliothek NICHT verfügbar (liegt an Kodi), bitte Suche verwenden oder aus den Favouriten

Unter Einstellungen - Wiedergabe muss bei Standard Aktion *Verzeichnis* eingestellet werden/sein damit Downloads angezeigt wird und funktioniert

Kategorie *Werkzeuge-Einstellungen-Downloads*

Herunterladen aktivieren

Speicherplatz Ordner muss für Filme UND Serien angelegt werden

Zurück zur Film/Serien Auswahl

Einen Film/Serie suchen, Film auswählen.

Wenn dann die Anbieter/Hoster angezeigt werden, das Kontexmenü öffnen

Download wählen

Es öffnet sich ein Fenster, wo der Name des Films und die Dateigröße angezeigt wird

Nach Klick auf Confirm, starte der Download

Es wird kurz: *Download* angezeigt

Während des Downloads wird in unregelmäßigen Abständen der Downloadfortschritt angezeigt (ca. 3-5 mal bis zum Ende)

Ihr findet den Film/die Serie dann in Eurem Download Ordner

**Xship Download Serien Ordner & Filme Ordner zur Bibliothek hinzufügen**

**Serien**

*Gehe zu:*

 - Kategorie Videos-Dateien
 
   Videos hinzufügen 
 
   Videoquelle hinzufügen: klicke auf *Durchsuchen*

   Suche jetzt den oben angeführten Pfad für die Serien
  
   Dann gib im unteren Feld einen Namen ein und klick OK

*Inhalt festlegen:*

hier wird eingestellt, ob es eine Serie oder ein Film ist

*Dieser Ordner beinhaltet:*

wähle aus was du brauchst, z.B. Serien

*Bitte Informationsquelle wählen:*

The TVDB

*Einstellungen:*

Aktiviere Fanart: aktivieren

Sprache: de

Get rating from: The TVDB wählen

OK

Inhalt Scanning Einstellungen kann man alles deaktiviert lassen

**Filme**

*Gehe zu:*

- Kategorie Videos- Dateien

  Videos hinzufügen 

  Videoquelle hinzufügen: klicke auf *Durchsuchen*
   
  Suche jetzt den oben angeführten Pfad für Filme
  
  Dann gib im unteren Feld einen Namen ein und klick OK

*Inhalt festlegen:*

hier wird eingestellt, ob es eine Serie oder ein Film ist

*Dieser Ordner beinhaltet:*

wähle aus was du brauchst, z.B. Filme

*Bitte Informationsquelle wählen:*

The Movie Database

*Einstellungen:*

Verwende Original Titel: kann deaktiviert werden

Aktiviere Fanart: aktivieren

Aktiviere Trailer: wenn gewünscht, EIN

Sprache: de

Altersbewertung: de

Lade die Bewertung von: TMDb oder IMDb wählen

OK

*Inhalt Scanning Einstellungen:* 

Rekursives Scannen aktivieren

(damit die Unterordner ordentlich eingelesen werden)

Filme liegen in getrennten Ordnern, die dem Filmtitel entsprechen aktivieren

Fertig

Serien & Filme werden jetzt im Kodi Menü Serien bzw. Filme angezeigt

Solltet Ihr jetzt Eure Filme/Serien noch nicht sehen, dann das “Seitenmenü” (Optionen) öffnen und Bibliothek aktualisieren klicken, oder wie oben beschrieben

## 2.7 Resolver Konfiguration

Es besteht die Möglichkeit, in den Einstellungen des URL Resolvers die Priorität der Hoster festzulegen also welche Hoster als ersters angezeigt bzw. verwendet werden sollen.

Diese Einstellungen werden in der settings.xml gespeichert.

Diese befindet sich hier und kann auch auf ein anderes System kopiert werden:

 ....kodi/userdata/addon_data/script.module.resolveurl

**Jedoch aufgrund der Arbeitsweise von Xship wird diese Einstellung im Xship Addon nicht unbedingt berücksichtigt**

*Da Xship & Xstream den gleichen Resolver verwenden, hat diese Einstellung auch Auswirkung auf beide Addons!!*

Xship probiert automatisch alle verfügbaren Hoster aus, bis ein Stream abgespielt werden kann

Die Auswahlreihenfolge der Hoster richtet sich nach deren Priorität

Diese kann unter “Resolver Settings” angepasst werden.

***Niedrige Werte werden vor hohen Werten gewählt***

Sind Eure Priorisierten (Lieblings) Hoster nicht nicht verfügbar, nimmt Xship den nächsten Hoster der funktioniert

Den Resolver findet Ihr in Kodi:

Optionen - Einstellungen - Addons - System Addons - Abhängigkeiten - ResolveUrl:  Konfigurieren


## 2.8 Gesehen Status in Xship

Der geshen Status wird vom Addon selbst gesetzt

Die Datenbank befindet sich unter:  

.....kodi/userdata/addon_data/plugin.video.Xship/playcount.db

Ihr könnt den "gesehen Status" (wached state) auch exportieren und auf einem anderen System importieren

Ihr müsst dann also nur die oben genannte *playcount.db* auf ein anderes System übertragen

Manuell ist möglich, den gesehen Status, über das Kontextmenü für Filme, Serien, Staffeln und Episoden selbst zu setzen


## 2.9 Plugin Video Themoviedb Helper

Das Addon [plugin.video.themoviedb.helper](https://github.com/jurialmunkey/plugin.video.themoviedb.helper) ist ein eigenständiges Addon und dient als Erweiterung für Xship

Damit ergeben sich neue Möglichkeiten im Bezug auf Nutzung von Trakt, TMDB und der lokalen Bibliothek

Bei Nutzung dieses Addons dient Xship nur noch zum Suchen der Hoster/Indexseiten. Alles andere wird direkt von diesem Addon erledigt

Es sind keine weiteren Addons notwendig, bei Verwendung von Trakt mit plugin.video.themoviedb.helper


**Installation:**

Das Addon befindet sich in der Kodi Repo und kann direkt in Kodi installiert werden. Dazu folgende Schritte durchführen:

Addons - Addon Browser (Schachtel links oben) - Suchen - helper eintragen

Nun auf TheMovieDbHelper klicken und installieren

Das Addon kann auch aus obigem Link herunterladen und in Kodi mit "aus .zip Installieren", installiert werden

Nach der Installation muss mindestens eine Einstellung gemacht werden, damit der entsprechende Ordner angelegt wird 

**Einrichtung**

Das Addon ist unter Addons - Video Addons zu finden

Auswählen, das Kontextmenü öffnen und Einstellungen wählen

*Allgemein*

Language and Country auf German stellen

Im Anschluss Kodi verlassen und am PC / Android zu folgendem Ordner navigieren:

- Windows
	- `C:\Users\BENUTZERNAME\AppData\Roaming\Kodi\userdata\addon_data\plugin.video.themoviedb.helper`    (AppData ist ein versteckter Ordner)

- Android 
	- `/Android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/plugin.video.themoviedb.helper`
	
	- `/sdcard/Android/data/org.xbmc.kodi/files/.kodi/userdata/addon_data/plugin.video.themoviedb.helper`  (.kodi ist ein versteckter Ordner)

Hier eine Ordner mit dem Namen *players* erstellen (......./plugin.video.themoviedb.helper/players)

Nun von unserem [Github](https://github.com/watchone/Downloads) die xship.json herunterladen und in den players Ordner kopieren

Im Anschluss daran, Kodi starten und das Addon weiter einrichten

*Accounts*

Hier kann eine Verbindung zu [Trakt.tv](www.trakt.tv) hergestellt werden, kostenloses Benutzerkonto erforderlich

Wenn erwünscht kann hier noch *Get watched indicators from Trakt* (importiere gesehen Status von Trakt) aktiviert werden

**Themoviedb Helper & Autoplay**

In xShip muss die Option Download abgeschaltet sein und die Auswahl Autoplay muss in den xShip Éinstellungen aktiviert werden

**Trakt Konto einrichten:**

Trakt.tv bietet viele Möglichkeiten, wie z.B. das Synchronisieren des Fortsetzungspunktes auf deren Server

Auf Trakt.tv ein Konto erstellen

In der Kategorie *Accounts* - *Trakt API* auf *Authenticate Trakt Account* klicken

*Es wird ein Infofenster angezeigt:*

Webseite besuchen: https://trakt.tv/activate

Dort werdet Ihr dann aufgefordert den Code (der in Kodi angezeigt wird)  einzugeben, Continue

Allow Trakt Helper to use Your Accout (Erlaube Trakt Helper die Verwendung Deines Kontos), YES

WooHoo! Your device is now connected and will automatically refresh in a few seconds (Dein Gerät ist jetzt verbunden und wird in wenigen Sekunden automatisch aktualisiert)

Zurück in plugin.video.themoviedb.helper wird nun zusätzlich die Kategorie Trakt angezeigt

Der Trakt Service kann ab jetzt genutzt weren

Nachdem nun im Addon eine Suche durchgeführt wurde und das Ergebnis angezeigt wird, kann das Kontextmenü geöffnet werden und hier *Trakt options*

Im folgendem Menü gibt es eine Anzahl an verschiedenen Trakt Möglichkeiten wie zum Beispiel "Add to Watchlist". Wird hier etwas gespeichert, ist das quasi die Trakt Merkliste, was man später mal anschauen möchte

Zu finden ist das Ganze dann im Menüpunkt Trakt z.B. unter Serien Watchlist

Startet man nun etwas aus der Watchlist, verschwindet es von dort und ist unter dem Eintrag *Your Recently Watched Serien/Filme* zu finden mit aktuellem gesehen Status

Dieser Menüpunkt kann dann für einen schnellen Zugriff als Kodi Favoriten gespeichert werden

*Players*

*Default Player for Movies* und *Default Player for Episodes* öffnen und hier Play with Xship wählen

Sonst sind hier keine Einstellungen notwendig

*API Keys*

Auf [Fanart.tv](www.fanart.tv) kann ein kostenloses Benutzerkonto erstellt werden und hier dann der persönliche API Key bei *Fanart.tv client key* eingetragen werden, wenn erwünscht

*Bibliothek*

Filme und Serien können mit diesem Addon auch in die Kodi Bibliothek integriert werden. Die Speicherpfade dafür sind schon vorgegeben und befinden sich hier:

*....userdata/addon_data/plugin.video.themoviedb.helper/movies*

*....userdata/addon_data/plugin.video.themoviedb.helper/tvshows*

Diese Ordner erscheinen erst, wenn ein Film bzw. eine Serie zur Bibliothek hinzugefügt wurde

Um etwas zur Kodi Bibliothek hinzuzufügen, wird nach Anzeige des Suchergebnis das Kontextmenü geöffnte und daraus der Eintrag *Zur Bibliothek hinzufügen* ausgewählt

Es werden nun lokale .strm Dateien in obigem Ordner abgelegt

Der obige Ordner muss in Kodi noch für die Bibliothek entsprechend eingerichtet werden, wie das geht steht in Kap.2.6


# 3. Bekannte Probleme

## 3.1 Fehler bei der Installation

**Bei der Installation von Xship erscheint folgende Fehlermeldung**

Installation fehlgeschlagen --> Installation der Abhängigen fehlgeschlagen

In diesem Fall die Installation wiederholen

Auf Windows 10 eventuell "Als Administrator ausführen" zum Kodi Starten wählen

## 3.2 Resolver Fehler

Sollte dies der Fall sein, bitte den aktuellste Version des "Resolver" über dier folgende Bezugsquellen beziehen:

[Download](https://github.com/streamxstream/xStreamRepo/tree/master/script.module.resolveurl)

## 3.3 Beobachtungen und Fehler im Betrieb

**Serienstream (s.to) "Geschützter Inhalt" wird angezeigt obwohl Benutzerdaten eingetragen sind**

Benutzerdaten von s.to unter Konten eingetragen sind kommt bei Auswahl eines s.to Streams immer die Meldung "Geschützter Inhalt"

*Dafür gibt es eigentlich nur 2 Möglichkeiten warum das so ist:*

1.Ihr teilt Euch ein Konto mit andern Usern (nicht zu empfehlen)

2.Ihr habt zu oft in zu kurzem Zeitabstand versucht  s.to Streams  abzuspielen

Wenn jedoch innerhalb kurzer Zeit zu viele Anfragen vom selben Benutzer kommen, sperrt s.to den Zurgriff für eine bestimmte Zeit

Später nocheinmal probieren und auf jeden Fall ein eigenes (Fake) Konto bei s.to ertsellen lösen diese Probleme


**Resolver Einstellungen werden nach Update gelöscht**

Lösung: die Option *"Cache-Funktion benutzen"* ausgeschaltet, befindet sich in den Resolver Einstellungen

Wenn das nicht helfen sollte, dann bitte wie folgt:

Da nach einem Resolver Update die Einstellungen (settings) weg sind, solltet Ihr diese vor einem Update sichern, damit Ihr nicht alles neu einrichten müsst

Nach dem Update, dann wieder in das Verzeichnis einfügen

Es ist nach dem URLResolver Update KEINE settings.xml vorhanden!!

Ihr findet die settings.xml hier: ....kodi/userdata/addon_data/script.module.resolveurl

**Real Debrid (RD) Links werden mit VPN übersprungen/nicht angespielt**

Versuch es mal mit einem VPN-Server in Deinem Heimatland, damit sollte es funktionieren

Aus dem Ausland fragt RD ein Captcha ab, wenn Du Dich anmeldest. Deshalb überspringt Xship die Links

(Eventuell TCP auf UDP umstellen)

**Suche liefert kein Ergebnis, Suche zeigt kein Ergebnis an**

Xship findet eine Serie oder einen Film bei der Suche nicht,obwohl auf thetvdb die Infos vorhanden sind.

Ein Beispiele: Die Biene Maja 2012

*Wie kann ich die Serien in Xship finden??*

Die Suche basiert auf Trakt.tv., Trakt nutzt thevdb & imdb Datenbank

Wenn auf Trakt.tv der Film oder die Serie gefunden wird,  findet es auch Xship

Der Film oder die Serie kann dabei in der Datenbank auch einen Englischen Namen enthalten/haben

Das Beispiel Biene Maja:  wird gefunden wenn es "Maya" geschrieben wird

Auch wenn Trakt nicht genutzt wird in/mit Xship, benutzt Xship trotzdem die Suche von Trakt.tv

Des weiteren, könnt Ihr auf der Homepage von Trakt.tv, Filme&Serien selbst zur Datenbank hinzufügen/nachtragen, wenn diese nicht vorhanden sind

Dazu benötigt Ihr die Film oder Serien ID Nummer, welche Euch auf thevdb.com angezeigt wird

Am unteren Ende der Trakt Homepage, findet Ihr das Import Menü für Filme (Import Movie) und Serien (Import TV Show), hier müsst Ihr die ID Nummer eingeben

**Abbruch der Streams/Buffern der Streams während der Wiedergabe**

Gehört eigentlich nicht hier in diese Kategorie, da es kein Fehler von Xship ist

Aber da es oft gefragt wird, bzw. öfters vorkommt steht es eben hier

Wenn der Stream an Kodi übergeben hat, ist die die Sache für Xship durch/erledigt

Wenn Streams abbrechen/buffern oder ähnliches, ist das ein Problem von Kodi und nicht von Xship

Was das verursacht müsste man genauer klären, eventuell hilft eine
advancedsettings.xml

**Fehlermeldung: "Kein Stream verfügbar"**

Xship greift bei der Suche, Film/Serienauswahl zuerst auf eine Filmdatenbank zu (IMDB), fragt diese nach Infos zum Film, zur Serie ab und zeigt diese dann an

In dieser Datenbank sind also nur Informationen zu Filmen/Serien gespeichert und hat noch nichts mit der Verfügbarkeit des Streams/Hoster zu tun

Daher kommt es immer wieder mal vor, dass z.B. die Episode einer Serie (in Deutsch) angezeigt wird und wenn der Stream gestarte werden soll,kommt die Fehlermeldung:

"In Xship kein Stream verfügbar"

Das ist KEIN Fehler von & in Xship!!

**Fehlende Artworks (Serien/Filmcover)**

Kann verschieden Ursachen haben, z.B. weil der TMDB-Key veraltet ist

Eine Lösung ist dann ein Update von uns

Ebenso kann auch folgendes sehr oft helfen, falls die Artworks nicht angezeigt werden:

1. plugin.video.Xship deinstallieren

2. Kann generell oft bei Artwork Problemen helfen:

Löschen des kompletten thumbnails Ordners (wird bei Kodi Neustart wieder neu angelegt):

...kodi/userdata/thumbnail

und löschen der Textures13.db:

...kodi/userdata/Database/Texture13.db

3.plugin.video.Xship neu installieren (eventuell vorher noch *Kodi* Cache löschen)

Bei neueren Artwork kann es helfen, sich bei Fanart.tv einen API-Key zu besorgen und den in den Konten-Einstellungen einzutragen

Noch besser dort einen Premium-acc anlegen, dann bekommt man die Bilder schneller

TitanSkin und Artwork Probleme sind bekann, liegt am TitanSkin

# 4. Fehlerbericht über Log-Datei


## 4.1. Allgemeines zur Log-Datei

In dem log File werden alle Aktivitäten/Programmabläufe von Kodi protokolliert und gespeichert

Wenn man nun Probleme mit Kodi hat, ist es sehr hilfreich, dieses Log File im Forum zu Posten

Nur so kann eine schnelle und Zielgerichtete Lösung erfolgen.


## 4.2 Speicherort der Log Datei

Den Speicherpfad von Kodi anzeigen lassen – Scroll weiter runter zum Punkt Debug_Logging und folgen den Beschreibungen.

Das ist immer vom Betriebssystem abhängig

Im Folgenden werden bekannte Ordnerstrukturen der jeweiligen Betriebssysteme aufgelistet

Anstelle von "xbmc" kann in den Ordnern auch "kodi" stehen

(die Ordnerstruktur kann jedoch auch leicht von dieser Anleitung abweichen):

- Windows XP
   - `Documents and Settings\<your_user_name>\Application Data\Kodi`
- Vista/Windows 7
    - `C:\Users\<your_user_name>/%APPDATA%/Roaming/Kodi/Kodi.log`
- Mac OS X
    - `/Users/<username>/Library/Logs/ oder`
    - `/Users/<your_user_name>/Library/Application Support/Kodi/userdata`
- iOS
    - `/private/var/mobile/Library/Preferences`
- Linux, OpenElec, Raspberry Pi 1-3
    - `$HOME/.kodi/temp/`
    - `$HOME/.kodi/userdata/temp/xbmc.log`
    - `$HOME/.kodi/userdata`
- Android
    - `/android/data/org.xbmc.Kodi/files/.kodi/temp`
    - `data/data/org.xbmc.Kodi/cache/temp`

Die Ordner sind meist versteckt und müssen sichtbar gemacht werden, im Windows Explorer oder auf Android mit dem ESDateiexplorer.

Das Log File kann am besten mit Notepad++  unter Windows oder gedit unter Linux betrachtet werden

Auch der normale Texteditor unter Windows geht, Notepad ist aber übersichtlicher

Auf Android einen Texteditor verwenden zum Betrachten

Übrigens die Kodi „log.old“ ist die Logdatei vom letzten Neustart/Crash. Also wenn man keine mehr erstellen kann, dann diese nehmen.


## 4.3. Erstellen und Hochladen der Log-Datei

Kodi hat Standardmäßig die beiden wichtigen Log Addons integriert (eines zum Lesen der Log, das andere zum Hochladen). 

Damit ist das Erstellen der Log Datei und Posten im Forum sehr viel einfacher

In Kodi gehe zu:

- Addons

- Suche

In die Zeile "log" ein und Klicks auf Fertig.

Folgende Addons auswählen und installieren diese:

Log Viewer für Kodi (nur zum Lesen der Log-Datei)

Kodi Log Uploader (zum Auslesen & Uploaden der Log-Datei)

Mit dem LogViewer kann man die Log Datei ansehen, mit dem LogUploaded das Log-File auf den angezeigten Homepage-Link hochladen, die Anweisungen der Anzeige befolgen

Bei der Installation eine E-Mail Adresse angeben. An diese wird dir dann nach dem LogUpload ein Link zur Log Datei geschickt.

Diesen Link im Forum Posten oder alles in einen Texteditor koperien, Die Datei speicherun und im Forum hochladen.

Debug-Logging (Kodi GUI):

Manchmal ist es gut das Debug Logging in Kodi zu aktivieren um noch mehr Informationen zu erhalten

(geht nur wenn, wenn es nicht schon in der advancedsettings.xml akttiviert wurde)

Folgendes Ausführen:

 Desktop-Optionen
 
- Einstellungen

- System

- Debugging

- "Debug-Logging aktivieren" anklicken

Fertig

Es wird nun am oberen Rand eine Statuszeile eingeblendet mit Infos, **Hier ist auch der Speicherort der Log-Datei zu sehen!**

Starte Kodi neu und öffne das Addon welches einen Fehler verursacht. Erstellen dann sofort eine Log-Datei (dann ist der Fehler leichter herauszulesen).

Das Debug-Logging kann im Anschluss wieder deaktiviert werden.

Unter dem Punkt  Komponentenspezifische Protokollierung kann man bei der Kategorie "Konfiguration der Komponentenspezifischen Protokollierung" noch Einstellen was alles im Debug-Log Protokolliert werden soll.


# 5. Python Dateien


## 5.1. Allgemeines zur .py-Datei

Eine .py Datei ist eigentlich eine Textdatei

Die Endung .py verweist auf die Programmiersprache Python, welche in Kodi zur Anwendung kommt

Diese .py Dateien werden in sämtlichen/den meisten Addons verwendet
 
 
## 5.2 Bearbeiten einer .py-Datei

Manchmal werdet Ihr lesen z.B. Wechsel die .py Datei in dem Ordner „xyz“, oder ändere den Eintrag in Zeile 134.

Öffnen könnt Ihr die Datei mit vielen Programmen z.B. Notepad++ (Freeware) oder Texteditor. 

In Notepad werden Euch die Zeilen-Nummern angezeigt und ist somit übersichtlicher, aber es geht auch mit dem Editor

Mit Notepad++ könnt Ihr die .py Datei sofort öffnen und wieder speichern

Bei Verwendung des Text-Editors müsst Ihr die Endung vorher von .py auf .txt ändern

Dann könnt Ihr die Datei öffnen und Änderungen vornehmen

Im Anschluss bitte „Speichern unter“ wählen und bei „Dateityp“ alle wählen, und wieder als .py Datei speichern


## 5.3 Speicherort der einzelnen Webseiten (.py Dateien)

In den folgenden Ordnern findet Ihr alle Addons von Kodi

Das Addon Xship wird unter plugin.video.Xship installiert

Die Index-Seiten .py Dateien findet Ihr unter ....kodi/addons/plugin.video.Xship/scrapers/scrapers_sources/de

- Android 
	- `/Android/data/org.xbmc.kodi/files/.kodi/addons/`
	- `/sdcard/Android/data/org.xbmc.kodi/files/.kodi/addons/`  (.kodi ist ein versteckter Ordner)
- iOS
	- `/private/var/mobile/Library/Preferences/Kodi/addons/`
- Linux 
	- `~/.kodi/addons/`
- Mac 
	- `/Users/<your_user_name>/Library/Application Support/Kodi/addons/`
- OpenELEC 
	- `/storage/.kodi/addons/`
- Windows
	- `C:\Users\BENUTZERNAME\AppData\Roaming\Kodi\addons`    (AppData ist ein versteckter Ordner)

