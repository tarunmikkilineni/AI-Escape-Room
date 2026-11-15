
# AI Escape Room — Test Cases

## Testing Objective

Verify that both versions handle player actions correctly
and that Version 2 prevents players from skipping puzzles.

| ID | Test Case | Expected Result | Observed Result | Status |
|---|---|---|---|---|
| TC01 | Enter incorrect drawer code 1234 | Drawer remains locked | Drawer remained locked | PASS |
| TC02 | Enter correct drawer code 4729 | Receive Brass Key | Brass Key added; progress 50% | PASS |
| TC03 | Try opening exit door without Brass Key | Door remains locked | Door locked; progress 0% | PASS |
| TC04 | Use incorrect door password SUN | Door remains locked | Door remained locked | PASS |
| TC05 | Guess MOON without examining painting in Version 2 | Door remains locked | Door locked; progress 50% | PASS |
| TC06 | Examine painting, then use Brass Key and MOON | Escape successfully | Congratulations; progress 100% | PASS |

## Adversarial Testing

### Test 1: Claiming to Have an Item

A player entered an action claiming to use the Brass Key
without actually having it in their inventory.

Version 2 rejected the action because the inventory
did not contain the Brass Key.

### Test 2: Guessing a Password Early

A player obtained the Brass Key and entered MOON without
examining the painting.

Version 2 rejected the escape attempt because
password_discovered was False.

After examining the painting, the same password was
accepted and the player escaped.

## Version 1 vs Version 2

Version 1 checks whether the player has the Brass Key
and enters the correct password.

Version 2 additionally checks whether the painting
clue has been discovered.

This improves puzzle integrity by preventing players
from skipping the painting puzzle.

## Testing Conclusion

The six documented gameplay tests passed during manual
testing. Version 2 successfully blocked the tested
shortcut attempts while allowing legitimate gameplay.
