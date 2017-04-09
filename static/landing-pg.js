"use strict"

// Mousover and turn picture to full-color
function eliminateFilter(evt) {
    $(this).css('filter', 'grayscale(0%)');
}

$('img.picture').on('mouseover', eliminateFilter);

// Mouseout and reset grayscale
function resetFilter(evt) {
    $(this).css('filter', 'grayscale(90%)');
}

$('img.picture').on('mouseout', resetFilter);
