$( setup );

function setup() {
    // tunes, man
    var playfirst = $("ul.playlist li:first-child");
    var audiop = $("#aplay").get(0);

    audiop.volume=.5;
    // autoplay
    // playThis(playfirst);

    // keep going man
    $("#aplay").on('ended',playNext);

    // player controls
    $("#pause").click(function() {
        audiop.pause();
    });
    $("#play").click(function() {
        audiop.play();
    })
    $("#playnext").click(playNext);
    $("#playprev").click(playPrev);

    $(".playlist_entry a").click(function(e) {
        e.preventDefault();
    });

    $("li.playlist_entry").click(function() {
        var file_link = $(this).children('a');
        playThis(file_link);
    });


    // load initial filebrowser
    filterFiles($('input[name=filter_files]').val());

    // hotkeys
    $(document).bind('keypress','z', playPrev);

    $(document).bind('keypress','x', function() {
        audiop.play();
    });

    $(document).bind('keypress','c', function() {
        audiop.pause();
    });

    $(document).bind('keypress','v', function() {
        audiop.pause();
    });

    $(document).bind('keypress','b', playNext);


    // file browser filter
    $('input[name=filter_files]').change(function() {
        filterFiles($(this).val())
    });

}

function filterFiles(query) {
    query = query || "."
    $.getJSON("filebrowser_json", function(data) {
        var ites = []
        $.each(data, function(index, obj) {
            var track_info = [obj.fields.artist, obj.fields.album, obj.fields.title]
            var listing = (track_info).join(' - ')
            var patt = RegExp(query, 'i');
            if (patt.test(listing)) {
                ites.push('<li class="filebrowser_entry"><a href="file/' + obj.pk + '">' + listing + '</a></li>');
            }
        });

        $('ul.filebrowser_list').html(ites.join(''));
        
    });
}


//closey
function retCurrentSong() {
    return undefined;
}

function current_song(args)  
{  
    if (args == undefined) {
        retCurrentSong();
    } else {
        retCurrentSong = function () {
            return(args);
        }
    }
}   

function nowPlaying(pl_item) {
    //var playing_now = retCurrentSong();
    var playing_now = pl_item;
    var text = playing_now.html();
    $("#now_playing").html(text);
    $(".playlist_selected").removeClass('playlist_selected');
    var parley = playing_now.parent();
    //alert(parley.html());
    parley.addClass('playlist_selected');
}

function playThis(item) {
    var audiop = $("#aplay");
    var track_src = item.attr('href');
    $(audiop.attr('src',track_src));
    current_song(item);
    nowPlaying(item);
}

function playNext() {
    var playing = retCurrentSong();
    var next_up = playing.parent().next().children('a');
    if (next_up != undefined) {
        playThis(next_up);
    } else {
        display_error('<span class="minorerror">No more tracks</span><br />');
    }
}
    
function playPrev() {
    var playing = retCurrentSong();
    var prev_up = playing.parent().prev().children('a');
    if ($(prev_up).length) {
        playThis(prev_up);
    } else {
        display_error('<span class="minorerror">Cannot go any further previous</span><br />');
    }
}

function display_error(msg) {
    $("#errors").html(msg);
    $("#errors").slideDown('fast');
    $("#errors").delay(2000);
    $("#errors").slideUp('fast');
}


