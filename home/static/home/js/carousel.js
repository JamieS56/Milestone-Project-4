var myCarousel = document.querySelector('#player-carousel')
var carousel = new bootstrap.Carousel(myCarousel, {
  interval: false,
  wrap: true
})

var myMobileCarousel = document.querySelector('#mobile-player-carousel')
var mobileCarousel = new bootstrap.Carousel(myMobileCarousel, {
  interval: false,
  wrap: true
})