<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

$letter = $_GET['letter'];

$w = 500;
$h = 500;

if ($letter == 'BigC' || $letter == 'M') { $w = 600; $h = 900; }

?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
<script src="https://code.jquery.com/jquery-1.10.2.js"></script>
</head>
<body>
<?php 
$max_pixels = 64;

class Pixel {
	public $i;
	public $x;
	public $y;
	public $rx;
	public $ry;
}

$xml=simplexml_load_string(file_get_contents('svg/'. $letter .'.svg')) or die("Error: Cannot create object");

$x = $xml->rect->attributes()['x'];
$y = $xml->rect->attributes()['y'];
$width = $xml->rect->attributes()['width'];
$height = $xml->rect->attributes()['height'];

// echo '[x: '. $x .', y: '. $y .', width: '. $width .', height: '. $height .']<br />';

$circles = $xml->g->g->circle;
$nbr_circles = count($circles);

// echo $nbr_circles .' pixels <br />';

$channels = array();

$nbr_channels = ceil($nbr_circles / $max_pixels);
for ($i = 0; $i < $nbr_channels; $i++) {
	if ($i == $nbr_channels - 1) {
		$channels[] = $nbr_circles - $max_pixels * $i;
	} else {
		$channels[] = $max_pixels;
	}
}

// echo $nbr_channels .' channels <br />';

// echo '<pre>';
// print_r($channels);
// echo '</pre>';

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

?>
<script>
$(document).ready(function(){
	var channels = [<?php echo implode(',', $channels); ?>];
	var c = 0;
	var p = 0;

    $('.pixel').click(function(e){
    	if ($(this).css("background-color") != "rgb(0, 0, 0)") {
    		return;
    	}

    	var pixel = $(this).attr('id');
    	$(this).css("background-color", "red");
    	$('#c'+ c +'p'+ p).text(pixel);
    	p += 1;
    	if (p >= channels[c]) {
    		c += 1;
    		p = 0;
    	}

    	$('#current_channel').text(channels[c] - p);
    });

    $('#clear_last').click(function(e){
    	p -= 1;

    	if (p < 0) { c -= 1; p = channels[c] - 1; }
    	if (c < 0) { c = 0; p = 0; }

    	var pixel = $('#c'+ c +'p'+ p).text();
    	$('#c'+ c +'p'+ p).text('');
    	$('#'+pixel).css("background-color", "black");

    	$('#current_channel').text(channels[c] - p);
    });
});
</script>
<div id="letter" style="width:<?php echo $w; ?>px; height:<?php echo $h; ?>px; background-color:gray; float: left;">
	<?php 
	foreach ($pixels as $pixel) {
		?><div class="pixel" id="<?php echo $pixel->i; ?>" style="width:14px; height:14px; background-color:black; position: absolute; left:<?php echo $pixel->rx * $w; ?>px; top:<?php echo $pixel->ry * $h; ?>px; border-radius: 7px;"></div><?php
	}
	?>
</div>
<div>
<div id="current_channel"><?php echo $channels[0]; ?></div>
	<?php 
		foreach ($channels as $k => $channel) {
			?>
			<div class="channel" id="c<?php echo $k; ?>"><?php echo $k; ?>(<?php echo $channel; ?>): 
				<?php 
					for ($i = 0; $i < $channel; $i++) {
						?><div class="channel_pixel" style="display: inline;" id="c<?php echo $k; ?>p<?php echo $i; ?>"></div> <?php
					}
				?>
			</div>
			<?php
		}
	?>
</div>
<button id="clear_last">Clear last pixel</button>
</body>
</html>
