Create a Guess The Number app that allows a user to guess a random number
between 1 and 10.


The user wins if they:
    - Guess the exact random number
    - Guess close to the exact random number


You should create 5 variables:
    - `max_num`: The maximum possible number (you'll use this in several places)
    - `random_number`: The random number (between 1 and your `max_num`)
    - `offset`: A number representing the accepted offset from the random number
    - `lower_bound`: The lowest number that gets a close guess 
        (`random_number` - offset)
    - `upper_bound`: The highest number that gets a close guess 
        (`random_number` + offset`)


Your app should:
    - Prompt the user for a number between 1 and your `max_num` and store this
    in a variable
    - Display the `random_number`
    - Check the result
        - If the user guessed the `random_number`
            - Print a message saying something like: "That's correct! You win $100!"
        - If the user guessed above the `lower_bound` __and__ below the 
        `upper_bound`
            - Print a message saying something like: "Pretty close! You get $50!"
        - For any other situation
            - Print a message saying something like: "Not even close!"



Example output (guessing the right answer):
-------------------------------------------------------
Guess a number between 1 and 10: 2
The random number is 2.
That's correct! You win $100!
-------------------------------------------------------


Example output (getting close to the right answer):
-------------------------------------------------------
Guess a number between 1 and 10: 3
The random number is 5.
Pretty close! You get $50!
-------------------------------------------------------

Example output (not close to the right answer):
-------------------------------------------------------
Guess a number between 1 and 10: 5
The random number is 1.
Not even close!
-------------------------------------------------------

