Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <first>, <middle>, <last> and <nick>
  When I add the new contact to the list
  Then the new contact list is equal to the old list with the added contact

  Examples:
  | first  | middle  | last  | nick  |
  | first1 | middle1 | last1 | nick1 |
  | first2 | middle2 | last2 | nick2 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact

Scenario: Edit a contact
  Given a non-empty contact list
  Given a contact with <name>, <middlename>, <lastname>, <nickname>
  When I edit the contact from the list
  Then the new contact list is equal to the old list with the edited contact

  Examples:
  | name  | middlename  | lastname  | nickname  |
  | name1 | middlename1 | lastname1 | nickname1 |
