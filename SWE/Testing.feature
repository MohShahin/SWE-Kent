Feature: Test Historical Fuguries at britannica

Scenario: leonardo da vinci an  artist
    Given that we have gone to www.wikipedia.org
     When we search for "leonardo da vinci"
     Then we find that they worked as "artist"
      And we find that they worked as "Engineer"

Scenario: al-Jazarī an inventor
    Given that we have gone to www.wikipedia.org
     When we search for "al-Jazari"
     Then we find that they worked as "inventor"

Scenario Outline: concatenate various things
    Given that we have gone to www.wikipedia.org
     When we search for "<Person>"
     Then we find that they worked as "<Occupation>"

 Examples: Various Art works
   | Person  |Occupation|
   | Raphael |painter|
   | Napoleon|emperor|
   | Ghandi  |lawyer|
