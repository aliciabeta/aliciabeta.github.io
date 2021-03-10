<?php
error_reporting( E_ALL );
ini_set( 'display_errors', 1 );

if (isset($_POST["submit"])) {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    $human = intval($_POST['human']);
    $headers = 'From: alicia@aliciabeta.com' . '\r\n' .
      'Reply-To: ' . $email . "\r\n" .
      'X-Mailer: PHP/' . phpversion();
    $to = 'alicia@aliciabeta.com';
    $subject = 'Website Message from  ' . $name;

    $body ="From: $name\n E-Mail: $email\n Message:\n $message";
}

// Check if name has been entered
if (!isset($_POST) || !key_exists('name', $_POST)) {
    $errName = 'Please enter your name';
}

// Check if email has been entered and is valid
if (!isset($_POST) || !key_exists('email', $_POST) || !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
    $errEmail = 'Please enter a valid email address';
}

//Check if message has been entered
if (!isset($_POST) || !key_exists('message', $_POST)) {
    $errMessage = 'Please enter your message';
}
//Check if simple anti-bot test is correct
if (!isset($human) || $human !== 5) {
    $errHuman = 'Your anti-spam is incorrect';
}
// If there are no errors, send the email
if (!isset($errName) && !isset($errEmail) && !isset($errMessage) && !isset($errHuman)) {
    $result = mail($to, $subject, $body, $headers);
    if (isset($result)) {
        $result = '<div class="alert alert-success">Thank You! I will be in touch</div>';
    } else {
        $result = '<div class="alert alert-danger">Sorry there was an error sending your message. Please try again later.</div>';
    }
}

function showPost($name) {
    if (isset($_POST[$name])) {
        echo htmlspecialchars($_POST[$name]);
    }
}

?>

<?php $page_title = "Alicia Beta - About"?>
<?php include("../header.php");?>

<div class="container" id="contact">
  <div class="row no-gutter">
    <div class="col-sm-10 col-sm-offset-1">
      <h3 class="text-center">Contact</h3>
        <form class="form-horizontal" role="form" method="post" action="index.php">
          <div class="form-group">
            <label for="name" class="col-sm-2 control-label">Name</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" id="name" name="name" placeholder="First & Last Name" value="<?php showPost('name'); ?>">
              <?php
                if (isset($errName) && isset($_POST["submit"])) {
                  echo "<p class='text-danger'>$errName</p>";
                }
              ?>
            </div>
          </div>
          <div class="form-group">
            <label for="email" class="col-sm-2 control-label">Email</label>
            <div class="col-sm-10">
              <input type="email" class="form-control" id="email" name="email" placeholder="example@domain.com" value="<?php showPost('email'); ?>">
              <?php
                if (isset($errEmail) && isset($_POST["submit"])) {
                  echo "<p class='text-danger'>$errEmail</p>";
                }
              ?>
            </div>
          </div>
          <div class="form-group">
            <label for="message" class="col-sm-2 control-label">Message</label>
            <div class="col-sm-10">
              <textarea class="form-control" rows="4" name="message"><?php showPost('message');?></textarea>
              <?php
                if (isset($errMessage) && isset($_POST["submit"])) {
                  echo "<p class='text-danger'>$errMessage</p>";
                }
              ?>
            </div>
          </div>
          <div class="form-group">
            <label for="human" class="col-sm-2 control-label">2 + 3 = ?</label>
            <div class="col-sm-10">
              <input type="text" class="form-control" id="human" name="human" placeholder="Your Answer" value="<?php showPost('human'); ?>">
              <?php
                if (isset($errHuman) && isset($_POST["submit"])) {
                  echo "<p class='text-danger'>$errHuman</p>";
                }
              ?>
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-10 col-sm-offset-2">
              <input id="submit" name="submit" type="submit" value="Send" class="btn btn-primary">
            </div>
          </div>
          <div class="form-group">
            <div class="col-sm-10 col-sm-offset-2">
              <?php if (isset($result)) {echo $result;} ?>
            </div>
          </div>
        </form> 
      </div>
    </div>
</div>

<?php include("../footer.php");?>



