# Work done during the iteration

* Pick new item from the TODO list (parse input as date/time)
* Write failing tests
  * `test_date_time`
    * Fail:  ValueError: Invalid isoformat string: '2022-06-01 13:37'
    * Hmmm... aha I must use `datetime` (not `date`), change that...
    * Fix that in the `whenday` module
    * Fail: Both cases! (Regression?)
    * Fix test case expected values (adjusted for new time-part)
    * Green!
* No obvious refactoring at this stage
* Mark item on TODO-list as done