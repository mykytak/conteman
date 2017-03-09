#!/bin/sed -f

s/hostname: vagrant/hostname: NAME.dev/
s/name: vagrant/name: NAME/

/authorize/d

/keys: /d
/    - ~\/.ssh\/id_rsa/d

s/map: "\/vagrant"/map: "\/NAME"/
s/to: "\/home\/vagrant\/vagrant"/to: "\/home\/vagrant\/NAME"/

s/map: homestead.app/NAME.dev/
s/to: "\/home\/vagrant\/vagrant\/public"/to: "\/home\/vagrant\/NAME\/public"/
