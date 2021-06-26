$(document).ready(function($) {
    $("span.counter").counterUp({
      delay: 10, /* The delay in milliseconds per number count up */
      time: 1000, /*The total duration of the count up animation */
      offset: 100, 
      /*The viewport percentile from which the counter starts (by default it's 100, meaning it's triggered at the very moment the element enters the viewport) */
    });
  });
  