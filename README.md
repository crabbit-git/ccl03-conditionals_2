# What's this then?

This was part of the first module of taught coursework for a software development course I'm doing at the moment. The aim seems to have been to use flowcharts to help understand how logic can be structured in code, specifically in Python 3.


# Right... but what does it do?

It's really basic, just converting a flowchart into code, pertaining to the process of making a cup of tea. I didn't write the logic, I just wrote the code to mirror what was in the flowchart. That's it. There's no front end, just one .py file that runs in a terminal.

I took a small amount of creative licence with the shopping list: rather than simply asking the user if they have stuff on it near the end of the flow and responding to their answer, I instead actually created a shopping list (which starts off empty), added stuff to it if required based on the user inputs, then printed it out if there was anything on it. Apart from that, this is more or less exactly what was asked for and laid out in the flowchart.

Personally, I'd structure the logic a bit differently. First off, I'd prefer to account for the user typing something other than "y" or "n" in the terminal, but that'd add a reasonable amount of complexity to this really basic code, so I didn't this time (I did in other exercises). Secondly, I'd do it in a way that avoids potentially double-asking the questions about the user's milk and sugar preferences. However, I wanted to keep this one pretty close to the actual parameters set in the instructions, so for now, it follows the flowchart and instructions very closely overall.