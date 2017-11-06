from collections import OrderedDict
import xml.etree.ElementTree as etree


source= """
<blog>
    <topics>
        <entry ID="UUID98766"><title>first</title><body>more words</body></entry>
        <entry ID="UUID86543"><title>second</title><body>more words</body></entry>
        <entry ID="UUID64319"><title>third</title><body>more words</body></entry>
    </topics>
    <indices>
        <bytag>
            <tag text="#sometag">
                <entry IDREF="UUID98766"/>
                <entry IDREF="UUID86543"/>
            </tag>
            <tag text="#anothertag">
                <entry IDREF="UUID98766"/>
                <entry IDREF="UUID64319"/>
            </tag>
        </bytag>
        <bylocation>
            <location text="Somewhere">
                <entry IDREF="UUID98766"/>
                <entry IDREF="UUID86543"/>
            </location>
            <location text="Somewhere Else">
                <entry IDREF="UUID98766"/>
                <entry IDREF="UUID86543"/>
            </location>
        </bylocation>
    </indices>
</blog>
"""

doc = etree.XML(source)
topics = OrderedDict()
for topic in doc.findall('topics/entry'):
    topics[topic.attrib['ID']] = topic


for topic in topics:
    print(topic, topics[topic].find("title").text)


for tag in doc.findall('indices/bytag/tag'):
    print(tag.attrib['text'])
    for e in tag.findall('entry'):
        print(" ", e.attrib['IDREF'])
