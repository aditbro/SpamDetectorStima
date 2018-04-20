<!DOCTYPE html>
<html lang=en>
  <head>
    <meta charset="UTF-8">
    <title>Spam Detector</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link href="https://fonts.googleapis.com/css?family=Montserrat" rel="stylesheet">
    <script src="js/jquery.js"></script>
    <script src="js/bootstram.min.js"></script>
  </head>
  <style>
    *{
      font-family:'Montserrat', sans-serif;
    }

    .row{
      margin-top:40px;
    }
  </style>
  <body>
    <div class="container-fluid">
      <div class="row">
        <div class="col-sm-12">
          <h2 class="text-center">Spam Detector Stima</h2>
        </div>
      </div>
      <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>" method="GET">
        <div class="row">
          <div class="col-sm-4 offset-sm-4">
            <label>Keyword</label>
            <p style="font-size:0.8em">the keywords are separated by semicolon, to escape semicolon use '\'</p>
            <input type="text" name="keyword" class="form-control" required>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4 offset-sm-4">
            <label>Algoritma</label>
            <div class="form-check" style="margin-top:10px">
              <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios1" value="option1" checked>
              <label class="form-check-label" for="exampleRadios1">
                KMP
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios2" value="option2">
              <label class="form-check-label" for="exampleRadios2">
                Boyer-Moore
              </label>
            </div>
            <div class="form-check">
              <input class="form-check-input" type="radio" name="exampleRadios" id="exampleRadios3" value="option3">
              <label class="form-check-label" for="exampleRadios3">
                Regex
              </label>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-4 offset-sm-4">
            <button type="submit" class="btn btn-primary">Submit</button>
          </div>
        </div>
        <div class="row">
          <div class="col-sm-6 offset-sm-3">
            <?php
              error_reporting(0);
              try{
                foreach($_POST["spamString"] as $spam){
                  echo "<p>$spam</p>";
                }
              }catch(Exception $e){
                echo "$e";
              }
            ?>
          </div>
        </div>
      </form>
    </div>
  </body>
</html>