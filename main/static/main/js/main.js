$(function() {
  // Owl Carousel
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    items: checking(),
    margin: 10,
    loop: true,
    nav: true
  });
});

function checking() {
  if (self.innerWidth <= 400) {
    return items = 1;
  }
  else {
    return items = 3
  }
}


