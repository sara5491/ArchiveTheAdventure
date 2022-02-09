$(document).ready(function () {
    $(".sidenav").sidenav({edge: "right"});
    $(".collapsible").collapsible();
    $(".tooltipped").tooltip();
    $(".datepicker").datepicker({
        maxDate: new Date(),
        yearRange: [2010,2022],
        format: "dd mmmm, yyyy",
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
});