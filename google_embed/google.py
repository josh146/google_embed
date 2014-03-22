# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from docutils import nodes
from docutils.parsers.rst import directives, Directive
from pelican import signals

def content_object_init(instance):

    try:
        GMAPS_KEY = instance.settings['GMAPS_KEY']
    except:
        GMAPS_KEY = ""

    class GPlusCard(Directive):
        required_arguments = 1
        optional_arguments = 0

        final_argument_whitespace = True
        has_content = True

        def run(self):
            url = self.arguments[0].strip()

            scriptHTML = "<script type='text/javascript' src='https://apis.google.com/js/plusone.js'></script>"
            linkHTML = "<div class='g-post' data-href='{}'></div>".format(url)

            return [nodes.raw('', scriptHTML, format='html'),
                    nodes.raw('', linkHTML, format='html')]


    class GMapsCard(Directive):

        def align(argument):
            return directives.choice(argument, ('left', 'center', 'right'))

        def mode(argument):
            return directives.choice(argument, ('place', 'search'))

        def maptype(argument):
            return directives.choice(argument, ('roadmap', 'satellite'))

        required_arguments = 0
        optional_arguments = 1
        option_spec = {
            'mode': mode,
            'width': directives.positive_int,
            'height': directives.positive_int,
            'maptype': maptype,
            'align': align
        }

        final_argument_whitespace = True
        has_content = True

        def run(self):
            location = '+'.join(self.arguments[0].split())
            mode = "place"
            maptype = "roadmap"
            width = 600
            height = 400
            align = 'center'

            if 'mode' in self.options:
                mode = self.options['mode']
            if 'maptype' in self.options:
                maptype = self.options['maptype']
            if 'width' in self.options:
                width = self.options['width']
            if 'height' in self.options:
                height = self.options['height']
            if 'align' in self.options:
                align = self.options['align']

            if align == 'center':
                alignCSS = "display: block;margin: 0 auto;"
            elif align == 'right':
                alignCSS = "float:right;"
            elif align == 'left':
                alignCSS = ""                

            linkHTML="""
                <iframe
                  width="{3}"
                  height="{4}"
                  frameborder="0" style="border:0;{6}"
                  src="https://www.google.com/maps/embed/v1/{0}?key={1}&q={2}&maptype={5}">
                </iframe>
                """.format(mode,GMAPS_KEY,location,width,height,maptype,alignCSS)

            return [nodes.raw('', linkHTML, format='html')]


    class GMapsDirections(Directive):

        def mode(argument):
            return directives.choice(argument, ('driving',
                'walking',
                'bicycling',
                'transit',
                'flying'))

        def maptype(argument):
            return directives.choice(argument, ('roadmap', 'satellite'))

        def align(argument):
            return directives.choice(argument, ('left', 'center', 'right'))

        required_arguments = 0
        optional_arguments = 1
        option_spec = {
            'mode': mode,
            'width': directives.positive_int,
            'height': directives.positive_int,
            'maptype': maptype,
            'origin': directives.unchanged,
            'destination': directives.unchanged,
            'waypoints': directives.unchanged,
            'align': align
        }

        final_argument_whitespace = True
        has_content = True

        def run(self):
            mode = ""
            waypoints = ""
            maptype = "roadmap"
            width = 600
            height = 400
            align = 'center'

            if 'mode' in self.options:
                mode = self.options['mode']

            if 'maptype' in self.options:
                maptype = self.options['maptype']

            if 'width' in self.options:
                width = self.options['width']

            if 'height' in self.options:
                height = self.options['height']

            if 'origin' in self.options:
                origin = '+'.join(self.options['origin'].split())

            if 'destination' in self.options:
                destination = '+'.join(self.options['destination'].split())

            if 'align' in self.options:
                align = self.options['align']

            if align == 'center':
                alignCSS = "display: block;margin: 0 auto;"
            elif align == 'right':
                alignCSS = "float:right;"
            elif align == 'left':
                alignCSS = ""

            if 'waypoints' in self.options:
                waypoints = '+'.join(self.options['waypoints'].split())
                linkHTML="""
                    <iframe
                      width="{1}"
                      height="{2}"
                      frameborder="0" style="border:0;{8}"
                      src="https://www.google.com/maps/embed/v1/directions?key={0}&origin={4}&destination={5}&waypoints={6}&maptype={3}&mode={7}">
                    </iframe>
                    """.format(GMAPS_KEY,width,height,maptype,origin,destination,waypoints,mode,alignCSS)
            else:
                linkHTML="""
                    <iframe
                      width="{1}"
                      height="{2}"
                      frameborder="0" style="border:0;{7}"
                      src="https://www.google.com/maps/embed/v1/directions?key={0}&origin={4}&destination={5}&maptype={3}&mode={6}">
                    </iframe>
                    """.format(GMAPS_KEY,width,height,maptype,origin,destination,mode,alignCSS)


            return [nodes.raw('', linkHTML, format='html')]


    class StaticMap(Directive):

        def maptype(argument):
            return directives.choice(argument, ('roadmap', 'satellite', 'hybrid', 'terrain'))

        def align(argument):
            return directives.choice(argument, ('left', 'center', 'right'))

        required_arguments = 0
        optional_arguments = 1
        option_spec = {
            'width': directives.positive_int,
            'height': directives.positive_int,
            'zoom': directives.positive_int,
            'maptype': maptype,
            'markers': directives.unchanged,
            'align': align
        }

        final_argument_whitespace = True
        has_content = True

        def run(self):
            center = '+'.join(self.arguments[0].split())
            maptype = "roadmap"
            width = 600
            height = 300
            zoom = 12
            markers = ""
            align = 'center'

            if 'maptype' in self.options:
                maptype = self.options['maptype']
            if 'width' in self.options:
                width = self.options['width']
            if 'height' in self.options:
                height = self.options['height']
            if 'zoom' in self.options:
                zoom = self.options['zoom']
            if 'markers' in self.options:
                markers = ''.join(['&markers=' + '|'.join(i.split()) for i in self.options['markers'].split('&')])
            if 'align' in self.options:
                align = self.options['align']

            if align == 'center':
                alignCSS = "display: block;margin: 0 auto;"
            elif align == 'right':
                alignCSS = "float:right;"
            elif align == 'left':
                alignCSS = ""

            linkHTML = """
                <img border=0
                  src="http://maps.googleapis.com/maps/api/staticmap?center={0}&zoom={1}&size={2}x{3}&sensor=false&maptype={4}&API={5}{6}"
                  alt="{0}"
                  style="{7}"/>
            """.format(center, zoom, width, height, maptype, GMAPS_KEY, markers, alignCSS)

            return [nodes.raw('', linkHTML, format='html')]


    class StreetView(Directive):

        def align(argument):
            return directives.choice(argument, ('left', 'center', 'right'))

        required_arguments = 0
        optional_arguments = 1
        option_spec = {
            'width': directives.positive_int,
            'height': directives.positive_int,
            'align': align
        }

        final_argument_whitespace = True
        has_content = True

        def run(self):
            location = '+'.join(self.arguments[0].split())
            align = 'center'
            width = 600
            height = 300

            if 'width' in self.options:
                width = self.options['width']
            if 'height' in self.options:
                height = self.options['height']
            if 'align' in self.options:
                align = self.options['align']

            if align == 'center':
                alignCSS = "display: block;margin: 0 auto;"
            elif align == 'right':
                alignCSS = "float:right;"
            elif align == 'left':
                alignCSS = ""

            linkHTML = """
                <img border=0
                  src="http://maps.googleapis.com/maps/api/streetview?location={0}&size={1}x{2}&sensor=false&API={3}"
                  alt="{0}"
                  style="{4}"/>
            """.format(location, width, height, GMAPS_KEY, alignCSS)

            return [nodes.raw('', linkHTML, format='html')]


    directives.register_directive('gplus', GPlusCard)
    directives.register_directive('gmaps', GMapsCard)
    directives.register_directive('directions', GMapsDirections)
    directives.register_directive('static-map', StaticMap)
    directives.register_directive('streetview', StreetView)

def register():
    signals.content_object_init.connect(content_object_init)

