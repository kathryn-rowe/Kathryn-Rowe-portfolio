"use strict"


function eliminateFilter(evt) {
    $(this).css('filter', 'grayscale(0%)');
}

function resetFilter(evt) {
    $(this).css('filter', 'grayscale(90%)');
}

$('img.picture').on('mouseover', eliminateFilter);

$('img.picture').on('mouseout', resetFilter);