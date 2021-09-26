
var imageSliderIndices = {};
initializeImageSlider();

function initializeImageSlider() {
    var sliders = document.getElementsByClassName("image-slider-container");
    var i;
    
    for (i = 0; i < sliders.length; i++) {
        var sliderName = sliders[i].classList[1];
        imageSliderIndices[sliderName] = 1;
    }

    console.log(imageSliderIndices);
    showSlides();
}

// Next/previous controls
function plusSlides(imageSlider, n) {
    showSlides(imageSliderIndices[imageSlider] += n);
}

// Thumbnail image controls
function currentSlide(imageSlider, n) {
    showSlides(imageSliderIndices[imageSlider] = n);
}

function showSlides() {
    for (var imageSlider in imageSliderIndices) {
        var i;
        var slides = document.getElementsByClassName("image-slider-image image-fade " + imageSlider);
        var dots = document.getElementsByClassName("image-slider-dot " + imageSlider);
    
        if (imageSliderIndices[imageSlider] > slides.length) {
            imageSliderIndices[imageSlider] = 1
        }

        if (imageSliderIndices[imageSlider] < 1) {
            imageSliderIndices[imageSlider] = slides.length
        }
    
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
    
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" image-active", "");
        }
    
        slides[imageSliderIndices[imageSlider] - 1].style.display = "block";
        dots[imageSliderIndices[imageSlider] - 1].className += " image-active";

        console.log(imageSlider + " -> " + imageSliderIndices[imageSlider])
    }
    console.log("---")
} 
