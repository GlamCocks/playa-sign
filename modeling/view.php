<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<?php 

$letter = $_GET['letter'];

$w = 500;
$h = 500;

if ($letter == 'BigC' || $letter == 'M') { $w = 600; $h = 900; }

$blob = file_get_contents('blob/'. $letter .'.pix');

$colors = array('red', 'blue', 'yellow', 'green', 'orange', 'pink', 'purple', 'cyan');
$t_colors = array('black', 'white', 'black', 'lime', 'black', 'black', 'white', 'black');

$lines = explode(PHP_EOL, $blob);

$max_pixels = 64;

class Pixel {
	public $i;
	public $x;
	public $y;
	public $rx;
	public $ry;
	public $color;
	public $t_color;
}

$xml=simplexml_load_string(file_get_contents('svg/'. $letter .'.svg')) or die("Error: Cannot create object");

$x = $xml->rect->attributes()['x'];
$y = $xml->rect->attributes()['y'];
$width = $xml->rect->attributes()['width'];
$height = $xml->rect->attributes()['height'];


$circles = $xml->g->g->circle;
$nbr_circles = count($circles);

$channels = array();

$nbr_channels = ceil($nbr_circles / $max_pixels);
for ($i = 0; $i < $nbr_channels; $i++) {
	if ($i == $nbr_channels - 1) {
		$channels[] = $nbr_circles - $max_pixels * $i;
	} else {
		$channels[] = $max_pixels;
	}
}


$pixels = array();

for ($i = 0; $i < $nbr_circles; $i++) {
	$circle = $circles[$i];
	
	$cx = $circle['cx'] - $x;
	$cy = $circle['cy'] - $y;

	$pixel = new Pixel();
	$pixel->i = $i;
	$pixel->x = $cx;
	$pixel->y = $cy;
	$pixel->rx = $cx / $width;
	$pixel->ry = $cy / $height;
	$pixels[] = $pixel;
}

$c = 0;

foreach ($lines as $line) {
	$items = explode(' ', $line);
	array_shift($items);

	foreach ($items as $k => $item) {
		$pixel = $pixels[$item];
		$pixel->i = $k;
		$pixel->color = $colors[$c];
		$pixel->t_color = $t_colors[$c];
	}
	$c++;
}

?>
<div id="letter" style="width:<?php echo $w; ?>px; height:<?php echo $h; ?>px; background-color:gray; float: left;">
	<?php 
	foreach ($pixels as $pixel) {
		?><div class="pixel" style="width:16px; height:16px; background-color:<?php echo $pixel->color; ?>; position: absolute; left:<?php echo $pixel->rx * $w; ?>px; top:<?php echo $pixel->ry * $h; ?>px; border-radius: 8px; text-align: center; font-size: 10pt; color: <?php echo $pixel->t_color; ?>"><b><?php echo $pixel->i; ?></b></div><?php
	}
	?>
</div>
<div>
	<?php 
		foreach ($channels as $k => $channel) {
			echo $k .': '. $channel . ' <br />';
		}
	?>
</div>

</body>
</html>
