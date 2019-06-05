# Markdown
Refactor a Markdown parser.

The markdown exercise is a refactoring exercise. There is code that parses a given string with Markdown syntax and returns the associated HTML for that string. 

##### *Note:-*
1. You need to create a file by the name of "**markdown.py**"
2. Create a function by the name of "**parse_markdown()**" which should take markdown syntax as a string and convert it to equivalent HTML as mentioned below:-

**e.g.:-** 
- parse_markdown('This will be a paragraph') should return **\<p>This will be a paragraph\</p>**
- parse_markdown('\_This will be italic\_') should return **\<p>\<em>This will be italic\</em>\</p>**
- parse_markdown('\_\_This will be bold\_\_') should return **\<p>\<strong>This will be bold\</strong>\</p>**
- parse_markdown('This will \_be\_ \_\_mixed\_\_') should return **\<p>This will \<em>be\</em> \<strong>mixed\</strong>\</p>**
- parse_markdown('# This will be an h1') should retrun **\<h1>This will be an h1\</h1>**
- parse_markdown('## This will be an h2') should return **\<h2>This will be an h2\</h2>**
- parse_markdown('###### This will be an h6') should retrun **\<h6>This will be an h6\</h6>**
- parse_markdown('* Item 1') should return **\<ul>\<li>Item 1\</li>\</ul>**
- parse_markdown('# Header!\n* \_\_Bold Item\_\_\n* \_Italic Item\_') should return **\<h1>Header!\</h1>\<ul>\<li>\<strong>Bold Item\</strong>\</li>
            \<li>\<em>Italic Item\</em>\</li>\</ul>**
