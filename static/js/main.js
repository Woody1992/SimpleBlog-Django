/* ===================================
--------------------------------------
  TheQuest - Gaming Magazine Template
  Version: 1.0
--------------------------------------
======================================*/
const size = 6 // AMOUNT OF RESULTS SHOWN IN SEARCH

const url = "http://127.0.0.1:8000/";
const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const resultsBox = document.getElementById("results-box");

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

const sendSearchData = (post) => {
  $.ajax({
    type: "POST",
    url:  "http://127.0.0.1:8000/search/",
    data: {
      csrfmiddlewaretoken: csrf,
      post: post,
    },
    success: (res) => {
      console.log(res.data);
      const list = res.data;
      const data = list.slice(0, size)
      if (Array.isArray(data)) {
        resultsBox.innerHTML = "";
        data.forEach((post) => {
          resultsBox.innerHTML += `
                        <a href="${url}${post.slug}" class="result-item">
                            <div class="result-raw">

                                <div class="search-result-single">
                                    <!-- <img src="${post.image}" class="search-game-img"> -->
                                    <h5 class="search-h5">${post.title}</h5>
                                    <a href="${url}${post.category_slug}"><p class="search-p">${post.category}<p></a>
                                </div>
                            </div>
                        </a>
                    `;

        });
        if (list.length > size) {
            resultsBox.innerHTML += `
                       <a href="#" class="result-item">Show all results</a>
            `;
        };
      } else {
        if (searchInput.value.length > 0) {
          resultsBox.innerHTML = `<b>${data} results found</b>`;
        } else {
          resultsBox.classList.add("not-visible");
        }
      }
    },
    error: (err) => {
      console.log(err);
    },

  });
};

searchInput.addEventListener("keyup", (e) => {
  console.log(e.target.value);

  if (resultsBox.classList.contains("not-visible")) {
    resultsBox.classList.remove("not-visible");
  }

  sendSearchData(e.target.value);
});

("use strict");

$(window).on("load", function () {
  /*------------------
		Preloder
	--------------------*/
  $(".loader").fadeOut();
  $("#preloder").delay(400).fadeOut("slow");
});

(function ($) {
  /*------------------
		Navigation
	--------------------*/
  $(".main-menu").slicknav({
    appendTo: ".header-section",
    allowParentLinks: true,
  });

  /*------------------
		Background Set
	--------------------*/
  $(".set-bg").each(function () {
    var bg = $(this).data("setbg");
    $(this).css("background-image", "url(" + bg + ")");
  });

  /*------------------
		Hero Slider
	--------------------*/
  var $slider = $(".hero-slider");
  var SLIDER_TIMEOUT = 10000;

  $slider.owlCarousel({
    items: 1,
    nav: false,
    dots: false,
    autoplay: true,
    autoplayTimeout: SLIDER_TIMEOUT,
    animateOut: "fadeOut",
    animateIn: "fadeIn",
    loop: true,
    onInitialized: ({ target }) => {
      var animationStyle =
        "-webkit-animation-duration" +
        SLIDER_TIMEOUT +
        "ms;animation-duration:" +
        SLIDER_TIMEOUT +
        "ms";
      var progressBar = $(
        '<div class="slider-progress-bar"><span class="progress" style=' +
          animationStyle +
          "></span></div>"
      );
      $(target).append(progressBar);
    },
    onChanged: ({ type, target }) => {
      if (type === "changed") {
        var $progressBar = $(target).find(".slider-progress-bar");
        var clonedProgressBar = $progressBar.clone(true);

        $progressBar.remove();
        $(target).append(clonedProgressBar);
      }
    },
  });

  /*------------------
		Video Popup
	--------------------*/
  $(".video-play").magnificPopup({
    type: "iframe",
  });

  /*------------------
		Testimonials
	--------------------*/
  $(".testimonial-slider").owlCarousel({
    items: 1,
    nav: false,
    dots: true,
    autoplay: true,
    loop: true,
    autoplayHoverPause: true,
    animateOut: "slideOutDown",
    animateIn: "slideInDown",
  });

  /*------------------
		Circle progress
	--------------------*/
  $(".circle-progress").each(function () {
    var cpvalue = $(this).data("cpvalue");
    var cpcolor = $(this).data("cpcolor");
    var cpid = $(this).data("cpid");

    $(this).append(
      '<div class="' +
        cpid +
        '"></div><div class="progress-value"><h3>' +
        cpvalue +
        "%</h3></div>"
    );

    if (cpvalue < 100) {
      $("." + cpid).circleProgress({
        value: "0." + cpvalue,
        size: 80,
        thickness: 4,
        fill: cpcolor,
        emptyFill: "rgba(0, 0, 0, 0)",
      });
    } else {
      $("." + cpid).circleProgress({
        value: 1,
        size: 80,
        thickness: 4,
        fill: cpcolor,
        emptyFill: "rgba(0, 0, 0, 0)",
      });
    }
  });
})(jQuery);
