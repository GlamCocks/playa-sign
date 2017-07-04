<?php

header('Content-Type: text/yaml');

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);

class Pixel {
	public $i;
	public $x;
	public $y;
}

$letters = array('G', 'L', 'A', 'M', 'BigC', 'O', 'C', 'K', 'S');

$o_width = 8.9252;
$o_height = 3.27;
$o_x = 5;
$o_y = 6.1759;

$margin_left = $o_x - $o_width / 2;
$margin_top = $o_y - $o_height / 2;

$xs = array(1.1934, 2.2581, 3.2441, 4.0321, 5.8394, 6.4039, 7.2706, 8.223, 9.0527);
$ys = array(6.9525, 7.1124, 7.2189, 6.3963, 5.9079, 6.6062, 6.4268, 6.5233, 6.6229);
$widths = array(1.3119, 0.9502, 1.0887, 1.9743, 1.7639, 0.8407, 0.8319, 1.1518, 0.8198);
$heights = array(1.7167, 1.3969, 1.1839, 2.5835, 2.7341, 1.0526, 1.1686, 1.5926, 1.4107);

$all_pixels = array();

$n = 0;

foreach ($letters as $letter) {
	$blob = file_get_contents('blob/'. $letter .'.pix');
	$lines = explode(PHP_EOL, $blob);

	$xml=simplexml_load_string(file_get_contents('svg/'. $letter .'.svg')) or die("Error: Cannot create object");

	$x = $xml->rect->attributes()['x'];
	$y = $xml->rect->attributes()['y'];
	$width = $xml->rect->attributes()['width'];
	$height = $xml->rect->attributes()['height'];

	$circles = $xml->g->g->circle;
	$pixels = array();

	for ($i = 0; $i < count($circles); $i++) {
		$circle = $circles[$i];
		
		$scale_x = ($circle['cx'] - $x) / $width;
		$scale_y = ($circle['cy'] - $y) / $height;

		$origin_x = ($xs[$n] - $margin_left) - ($widths[$n] / 2);
		$origin_y = ($ys[$n] - $margin_top) - ($heights[$n] / 2);
		$scale_origin_x = $origin_x / $o_width;
		$scale_origin_y = $origin_y / $o_height;

		$pixel = new Pixel();
		$pixel->i = $i;
		$pixel->x = $scale_origin_x + $scale_x * ($widths[$n] / $o_width);
		$pixel->y = abs(($scale_origin_y + $scale_y * ($heights[$n] / $o_height)) - 1);
		$pixels[] = $pixel;
	}

	$c = 0;

	foreach ($lines as $line) {
		$items = explode(' ', $line);
		$channel = intval($items[0]);
		array_shift($items);

		foreach ($items as $k => $item) {
			$pixel = $pixels[$item];
			$pixel->i = $k + $channel * 64;
		}
	}
	$c++;

	$all_pixels = array_merge($pixels, $all_pixels);

	$n++;
}

function cmp($a, $b)
{
    return $a->i > $b->i;
}

usort($all_pixels, "cmp");

$output_pixels = array();
$last = -1;

foreach ($all_pixels as $pixel) {
	while ($pixel->i > $last + 1) {
	$output_pixels[] = '  -
    i: '. ($last+1) .'
    x: 0.0
    y: 0.0
';
		$last++;
	}

	$output_pixels[] = '  -
    i: '. $pixel->i .'
    x: '. $pixel->x .'
    y: '. $pixel->y .'
';
	$last = $pixel->i;
}

echo implode('', $output_pixels);

