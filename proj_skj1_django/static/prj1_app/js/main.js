$(function () {
  // Cache variables for increased performance on devices with slow CPUs.
  var flexContainer = $('div.flex-container')
  var searchBox = $('.search-box')
  var searchClose = $('.search-icon-close')
  var searchInput = $('#search-input')

  // Menu Settings
  $('.menu-icon, .menu-icon-close').click(function (e) {
    e.preventDefault()
    e.stopPropagation()
    flexContainer.toggleClass('active')
  })

  // Click outside of menu to close it
  flexContainer.click(function (e) {
    if (flexContainer.hasClass('active') && e.target.tagName !== 'A') {
      flexContainer.removeClass('active')
    }
  })

  // Press Escape key to close menu
  $(window).keydown(function (e) {
    if (e.key === 'Escape') {
      if (flexContainer.hasClass('active')) {
        flexContainer.removeClass('active')
      } else if (searchBox.hasClass('search-active')) {
        searchBox.removeClass('search-active')
      }
    }
  })

  // Search Settings
  $('.search-icon').click(function (e) {
    e.preventDefault()
    searchBox.toggleClass('search-active')
    searchInput.focus()

    if (searchBox.hasClass('search-active')) {
      searchClose.click(function (e) {
    		e.preventDefault()
    		searchBox.removeClass('search-active')
    	})
    }
  })
});
//
// $(function() {
//   var pre = document.getElementsByTagName('pre'),
//     pl = pre.length;
//   for (var i = 0; i < pl; i++) {
//     pre[i].innerHTML = '<span class="line-number"></span>' + pre[i].innerHTML + '<span class="cl"></span>';
//     var num = pre[i].innerHTML.split(/\n/).length;
//     for (var j = 0; j < (num - 1); j++) {
//       var line_num = pre[i].getElementsByTagName('span')[0];
//       line_num.innerHTML += '<span>' + (j + 1) + '</span>';
//     }
//   }
// });