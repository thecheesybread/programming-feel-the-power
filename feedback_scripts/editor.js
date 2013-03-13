$(document).ready(function() {

  var editor = CodeMirror.fromTextArea('code', {
    parserfile: ["parsepython.js"],
    stylesheet: "css/pythoncolors.css",
    path: "js/",
    lineNumbers: true,
    textWrapping: false,
    indentUnit: 4,
    height: "160px",
    fontSize: "9pt",
    autoMatchParens: true,
    parserConfig: {'pythonVersion': 2, 'strictErrors': true},
    initCallback: initialize_exercises
  });

  function getParameterByName(name)
  {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regexS = "[\\?&]" + name + "=([^&#]*)";
    var regex = new RegExp(regexS);
    var results = regex.exec(window.location.search);
    if(results == null)
      return "";
    else
      return decodeURIComponent(results[1].replace(/\+/g, " "));
  }

  function initialize_exercises(editor) {
    exercises = new Array();
    var x = {};
    x = {}
    x["prompt"] = "Print the number 5"
    x["hint"] = "The syntax to print the string 5 is <br><pre> print '5' </pre>";
    x["append"] = "";
    x["print"] = "5";
    x["topic"] = "Printing"
    exercises[0] = x;

    x = {}
    x["prompt"] = "Print the number 6 and then print the number 7 on the next line"
    x["hint"] = "The syntax to print the string 5 is <br><pre> print '5' </pre>";
    x["append"] = "";
    x["print"] = "6\n7";
    x["topic"] = "Printing"
    exercises[1] = x;


    x = {}
    x["prompt"] = "Write a function called return_number that returns the number 100";
    x["hint"] = "The syntax for writing a function that returns the number 200 is <br><pre> def function_name():\n\treturn 200</pre>";
    x["append"] = "print (return_number() * 10) == 1000";
    x["print"] = "True";
    x["topic"] = "Functions"
    exercises[2] = x;

    x = {};
    x["prompt"] = "Write a function called return_number that returns the number 500";
    x["hint"] = "The syntax for writing a function that returns the number 200 is <br><pre> def function_name():\n\treturn 200</pre>";
    x["append"] = "print (return_number() * 10) == 5000";
    x["print"] = "True";
    x["topic"] = "Functions"
    exercises[3] = x;

    x = {};
    x["prompt"] = "Write a function called multiply_by_10 that takes a number as an argument and returns the number multiplied by 10";
    x["hint"] = "The syntax for writing a function that takes a number as an argument and returns the number divided by 10 is <br><pre> def some_function_name(x):\n\treturn x / 10</pre>";
    x["append"] = "print (multiply_by_10(5) * 10) == 500";
    x["print"] = "True";
    x["topic"] = "Functions"
    exercises[4] = x;

    x = {};
    x["prompt"] = "Write a function called add_5 that takes a number as an argument and returns the number + 5";
    x["hint"] = "The syntax for writing a function that takes a number as an argument and returns the number divided by 10 is <br><pre> def some_function_name(x):\n\treturn x / 10</pre>";
    x["append"] = "print (add_5(20) * 10) == 250";
    x["print"] = "True";
    x["topic"] = "Functions"
    exercises[5] = x;

    x = {};
    x["prompt"] = "Write a function called add_three_numbers that takes in 3 numbers as its arguments and returns the three numbers added together"
    x["hint"] = "The syntax for writing a function that takes in 2 numbers as its arguments and returns the two numbers added together is <br><pre> def some_function_name(a, b):\n\treturn a + b</pre>";
    x["append"] = "print (add_three_numbers(1, 2, 3) * 10) == 60";
    x["print"] = "True";
    x["topic"] = "Functions"
    exercises[6] = x;

    x = {};
    x["prompt"] = "Write a for loop that prints out the numbers 0 through 9 line by line"
    x["hint"] = "The syntax for printing out numbers 4 through 12 line by line is  <br><pre>for x in range(4, 13):\n\tprint x</pre>";
    x["append"] = "";
    x["print"] = "0\n1\n2\n3\n4\n5\n6\n7\n8\n9";
    x["topic"] = "For loops"
    exercises[7] = x;

    x= {};
    x["prompt"] = "Write a for loop that prints the square of the number 0 through 9 line by line";
    x["hint"] = "if x is a number then <pre> x*x </pre> is the square of that number.";
    x["append"] = "";
    x["print"] = "0\n1\n4\n9\n16\n25\n36\n49\n64\n81";
    x["topic"] = "For loops"
    exercises[8] = x;



    x= {};
    x["prompt"] = "Create a list and name it my_list. Using append add 1, 2, 3, 4, 5 to my_list in that order.";
    x["hint"] = "To help you get started. <br><pre>my_list = []\nmy_list.append(1)\nmy_list.append(2)</pre>";
    x["append"] = "print my_list";
    x["print"] = "[1, 2, 3, 4, 5]";
    x["topic"] = "lists"
    exercises[9] = x;

    x= {};
    x["prompt"] = "Create a list and name it my_list2. Using a for loop add the numbers 1 through 100 to my_list2";
    x["hint"] = "This would add the numbers 1 through 9 to a_list. <br><pre>a_list = []\nfor number in range(1, 10):\n\ta_list.append(number)</pre>";
    x["append"] = "print my_list2";
    x["print"] = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]";
    x["topic"] = "lists"
    exercises[10] = x;

    x= {};
    x["prompt"] = "You don't actually need a for loop in the previous assignment. How would you make my_list2 contain all the number 1 through 100 in just one line?";
    x["hint"] = "This code is equivalent to my_list2 = [1, 2, 3, 4, 5] <br><pre>my_list2 = range(1, 6)</pre>";
    x["append"] = "print my_list2";
    x["print"] = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]";
    x["topic"] = "lists"
    exercises[11] = x;

    x= {};
    x["prompt"] = "Write a function called return_nums that takes in a number x as an argument and returns a list with all of the numbers from 0 to x line by line.";
    x["hint"] = "The syntax for writing a for loop that prints out the numbers 0 through 9 line by line is <br> <pre>for number in range(0, 10):\n\tprint x</pre> Now create a list outside of the for loop and use append inside the for loop. If you're clever about it you can even avoid using af or loop!";
    x["append"] = "return_nums(5)";
    x["print"] = "[1, 2, 3, 4, 5]";
    x["topic"] = "lists"
    exercises[12] = x;


    x= {};
    x["prompt"] = "";
    x["hint"] = "";
    x["append"] = "";
    x["print"] = "";
    x["topic"] = ""
    exercises[8] = x;


    x= {};
    x["prompt"] = "";
    x["hint"] = "";
    x["append"] = "";
    x["print"] = "";
    x["topic"] = ""
    exercises[8] = x;


    x= {};
    x["prompt"] = "";
    x["hint"] = "";
    x["append"] = "";
    x["print"] = "";
    x["topic"] = ""
    exercises[8] = x;


    x= {};
    x["prompt"] = "";
    x["hint"] = "";
    x["append"] = "";
    x["print"] = "";
    x["topic"] = ""
    exercises[8] = x;




    current_index = parseInt(getParameterByName('exercise'));
    if (!current_index) {
      current_index = 0;
    }
    current = exercises[current_index];
    display_exercise(current);
    output = "";
    hide_hint();
  }

  function reveal_hint() {
    $('#show_hint').hide();
    $('#hint_wrapper').show(300);
  }
  function hide_hint() {
    $('#hint_wrapper').hide();
    $('#show_hint').show();
  }
  $('#show_hint').click(function() {
    reveal_hint()
  });

  function finish_exercises() {
    document.getElementById("prompt").innerHTML = "Congrats! You have finished all the exercises";
    editor.setCode("");
    hide_hint();
    document.getElementById("hint").innerHTML = "";
  }
  function display_exercise(prompt_obj) {
    hide_hint();
    document.getElementById("prompt").innerHTML = current["prompt"];
    editor.setCode("");
    document.getElementById("hint").innerHTML = current["hint"];
    editor.focus();
  }
  function next_exercise() {
    window.location.href = "crammit-feedback.html?exercise=" + current_index;
  }

  function outf(text) {
    var mypre = document.getElementById("output");
    mypre.innerHTML = mypre.innerHTML + text;
  }


  function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
      throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
  }

  function runit() {
    var output = ""
    var prog = editor.getCode();
    var mypre = document.getElementById("output");
    mypre.innerHTML = '';
    Sk.pre = "output";
    Sk.configure({output:outf, read:builtinRead});
    eval(Sk.importMainWithBody("<stdin>",false,prog));
  }

  function test_output(text) {
    output += text;
  }

  function check_output() {
    console.log(current);
    if (output.trim() == current["print"]) {
      alert("Nice job");
      current_index += 1;
      if (current_index >= exercises.length) {
        finish_exercises();
        return;
      }
      current = exercises[current_index];
      //display_exercise(current);
      next_exercise();
    } else {
      console.log(output.trim());
      alert("Sorry wrong output");
    }
  }

  function testit() {
    output = ""
    var prog = editor.getCode() + '\r\n' + current["append"];
    var mypre = document.getElementById("output");
    Sk.pre = "output";
    Sk.configure({output:test_output, read:builtinRead});
    eval(Sk.importMainWithBody("<stdin>",false,prog));
  }

  $('#run_code').click(function() {
    try {
      runit();
      testit();
      check_output();
    } catch (err) {
      if (err.toString().trim() == "TypeError: Cannot read property 'constructor' of null") {
        document.getElementById("output").innerHTML = "Your function does not have return value. Your function needs a return value.";
      } else {
        document.getElementById("output").innerHTML = err.toString();
      }
    }
  });

});
