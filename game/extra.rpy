init -5 python:
    class MusicItem:
        def __init__(self, name, file, length, about):
            self.name = name
            self.file = file
            self.length = length
            self.about = about
            self.refresh_audio()

        def refresh_audio(self):
            if not renpy.seen_audio(self.file):
                self.is_locked = True
            else:
                self.is_locked = False


    music_list= []
    music_list.append(MusicItem(_("Party Ambience{#song title}"),audio.party,1.57,_("Ambiance theme.{#about the track}")))
    music_list.append(MusicItem(_("Confessions from a Poltergeist{#song title}"),audio.echo,2.40,_("Echo's theme.{#about the track}")))
    music_list.append(MusicItem(_("Possessed by a Poltergeist{#song title}"),audio.echo_bad,1.36,_("One Step Too Far.{#about the track}")))
    music_list.append(MusicItem(_("The Vlallad of Chadimir{#song title}"),audio.chad,3.24,_("Chadimir's theme.{#about the track}")))
    music_list.append(MusicItem(_("A Spiky Little Buckeroo{#song title}"),audio.moth,2.10,_("Mothman's theme.{#about the track}")))
    music_list.append(MusicItem(_("Welcome to Franky's Eldritch Abominations{#song title}"),audio.franky,2.03,_("Franky's Theme.{#about the track}")))


init python:
    def notify_music():
        for i in music_list:
            if i.file == renpy.music.get_playing('music'):
                renpy.show_screen("notify_music",song=i.name[:-13])
