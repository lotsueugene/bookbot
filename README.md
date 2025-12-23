<h1>📘 BookBot</h1>

<p>
BookBot is a simple Python command-line application that analyzes a text file (such as a book) and prints basic statistics about it. 
It reports the total word count and the frequency of each alphabetic character, sorted from most common to least common.
</p>

<h2>👨‍💻 Project Overview</h2>

<ul>
  <li>Reads a text file provided via the command line</li>
  <li>Counts the total number of words</li>
  <li>Counts how often each letter appears (case-insensitive)</li>
  <li>Sorts letters by frequency</li>
  <li>Displays a formatted report in the terminal</li>
</ul>

<h2>📂 Project Structure</h2>

<pre>
bookbot/
├── main.py
├── stats.py
├── books/
└── README.md
</pre>

<h2>🚀 How to Run</h2>

<p>Make sure you have <b>Python 3</b> installed.</p>

<p>From the project root, run:</p>

<pre>
python3 main.py &lt;path_to_book&gt;
</pre>

<p><b>Example:</b></p>

<pre>
python3 main.py books/frankenstein.txt
</pre>

<p>If no file path is provided, the program will display:</p>

<pre>
Usage: python3 main.py &lt;path_to_book&gt;
</pre>

<h2>📊 Example Output</h2>

<pre>
============ BOOKBOT ============
Analyzing book found at <p><path_to_book></p>...
----------- Word Count ----------
Found 78365 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
</pre>

<p>Only alphabetic characters are included in the character count.</p>

<h2>🧠 File Breakdown</h2>

<ul>
  <li><b>main.py</b><br/>
    Handles command-line arguments, reads the book file, calls analysis functions, sorts results, and prints the final report.
  </li>
  <br/>
  <li><b>stats.py</b><br/>
    Contains helper functions for counting words, counting letter frequencies, and sorting character data.
  </li>
</ul>

<h2>📝 Notes</h2>

<ul>
  <li>Letter counting is case-insensitive</li>
  <li>Punctuation and spaces are ignored</li>
  <li>The <code>books/</code> directory is typically excluded from version control</li>
</ul>

<h2>🎯 Learning Objectives</h2>

<ul>
  <li>Command-line interfaces (CLI)</li>
  <li>File input/output in Python</li>
  <li>Dictionaries and loops</li>
  <li>Sorting with custom keys</li>
  <li>Code organization across multiple files</li>
</ul>
