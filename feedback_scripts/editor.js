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

  function initialize_exercises(editor) {
    exercises = new Array();
    var x = {};
    x["prompt"] = "Write a function called test_print that returns the number 100";
    x["hint"] = "The syntax for writing a function that returns the number 200 is \r\n def function_name():\r\n\r\treturn 200";
    x["append"] = "print (test_print() * 10) == 1000";
    x["print"] = "True";
    exercises[0] = x;

    x = {};
    x["prompt"] = "Write a function called test_print that returns the number 500";
    x["hint"] = "The syntax for writing a function that returns the number 200 is \r\n def function_name():\r\n\r\treturn 200";
    x["append"] = "print (test_print() * 10) == 5000";
    x["print"] = "True";
    exercises[1] = x;

    current_index = 0;
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
    document.getElementById("prompt").innerHTML = current["prompt"];
    editor.setCode("");
    document.getElementById("hint").innerHTML = current["hint"];
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
      display_exercise(current);
    } else if (output.trim() == "") {
      alert("Sorry your code does not compile");
    } else {
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
     document.getElementById("output").innerHTML = err.toString();
    }
  });

});
