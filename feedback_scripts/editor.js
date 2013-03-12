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
    exercises[0] = x;

    x = {}
    x["prompt"] = "Print the number 6 and then print the number 7 on the next line"
    x["hint"] = "The syntax to print the string 5 is <br><pre> print '5' </pre>";
    x["append"] = "";
    x["print"] = "6\n7";
    exercises[1] = x;


    x = {}
    x["prompt"] = "Write a function called return_number that returns the number 100";
    x["hint"] = "The syntax for writing a function that returns the number 200 is <br><pre> def function_name():\n\treturn 200</pre>";
    x["append"] = "print (return_number() * 10) == 1000";
    x["print"] = "True";
    exercises[2] = x;

    x = {};
    x["prompt"] = "Write a function called return_number that returns the number 500";
    x["hint"] = "The syntax for writing a function that returns the number 200 is <br><pre> def function_name():\n\treturn 200</pre>";
    x["append"] = "print (return_number() * 10) == 5000";
    x["print"] = "True";
    exercises[3] = x;

    x = {};
    x["prompt"] = "Write a function called multiply_by_10 that takes a number as an argument and returns the number multiplied by 10";
    x["hint"] = "The syntax for writing a function that takes a number as an argument and returns the number divided by 10 is <br><pre> def some_function_name(x):\n\treturn x / 10</pre>";
    x["append"] = "print (multiply_by_10(5) * 10) == 500";
    x["print"] = "True";
    exercises[4] = x;

    x = {};
    x["prompt"] = "Write a function called add_5 that takes a number as an argument and returns the number + 5";
    x["hint"] = "The syntax for writing a function that takes a number as an argument and returns the number divided by 10 is <br><pre> def some_function_name(x):\n\treturn x / 10</pre>";
    x["append"] = "print (add_5(20) * 10) == 250";
    x["print"] = "True";
    exercises[5] = x;

    x = {};
    x["prompt"] = "Write a function called add_three_numbers that takes in 3 numbers as its arguments and returns the three numbers added together"
    x["hint"] = "The syntax for writing a function that takes in 2 numbers as its arguments and returns the two numbers added together is <br><pre> def some_function_name(a, b):\n\treturn a + b</pre>";
    x["append"] = "print (add_three_numbers(1, 2, 3) * 10) == 60";
    x["print"] = "True";
    exercises[6] = x;
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
