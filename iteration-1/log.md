# Work done during the iteration

* Pick first item on the TODO list (parse input as date/time)
  * Actually two items (w, w/o time) - put time on TODO-list and focus on pure date 
* Realized that the tool must be robust w.r.t. no/incorrect input
  * Add to TODO-list
* Write failing tests
  * `test_date_only`
    * Fail: TypeError: whenday() takes 0 positional arguments but 1 was given
    * Just echo input as output
    * Fail: AssertionError: assert 'datetime.date(2022, 6, 1)' == '2022-06-01' 
    * Parse using `date.fromisoformat`
    * Fail: AssertionError: assert 'datetime.date(2022, 6, 1)' == datetime.date(2022, 6, 1)
    * Wrap returned object in `repr()`
    * Green!
* No obvious refactoring at this stage
* Mark item on TODO-list as done