# Work done during the iteration

* Pick new item: Echo diff relative "now" as raw time
  * Want to move forward with core function - robustness can wait
* Hard to test with "actual now" - let `now` be an argument (of `datetime` type)
* Adjust previous tests to provide the expected (parsed) time as second argument (`now`)
  * Expected output is 0 (`datetime.timedelta(0)`)
  * Fail: (2x) TypeError: whenday() takes 1 positional arguments but 2 were given
  * Add handling of `now` argument and return "input-time - now"
  * Green!
  * But... `pylint` warning in the "if __name__ == '__main__'" part
    * Not covered by our tests... Hmmm... Will probably never be...
    * Fix by using actual "now" (`datetime.today()`) 
* No obvious refactoring at this stage
* Mark item on TODO-list as done
