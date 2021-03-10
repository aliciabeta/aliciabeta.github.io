<?php $page_title = "Alicia Beta"?>
<?php include("header.php");?>

<div class="container" id="gallery">
  <div class="row no-gutter">
    <div class="col-xs-12 col-sm-6 left">
<?php
  $file = fopen("gallery_left.txt", "r");
  while(!feof($file)) {
    $string = fgets($file);
    $name = strtok($string, '","');
    $img = strtok('","');
    
    echo '<div class="art">';
    echo '  <img class="img-responsive" src="' . $img . '" alt="' . $name . '" />';
    echo '  <div class="caption">' . $name . '</div>';
    echo '</div>';
  }
  fclose($file);
?>
    </div>
    <div class="col-xs-12 col-sm-6 right">
<?php
  $file = fopen("gallery_right.txt", "r");
  while(!feof($file)) {
    $string = fgets($file);
    $name = strtok($string, '","');
    $img = strtok('","');
    
    echo '<div class="art">';
    echo '  <img class="img-responsive" src="' . $img . '" alt="' . $name . '" />';
    echo '  <div class="caption">' . $name . '</div>';
    echo '</div>';
  }
  fclose($file);
?>
    </div>
  </div>
</div>

<?php include("footer.php");?>
