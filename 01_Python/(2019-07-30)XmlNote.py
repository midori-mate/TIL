
"""XmlNote

Create XML text in Python script!

Basically...
- Create top level DOM.
    - xml.dom.minidom.Document()
- Create node and add it to the DOM as a child
    - dom.createElement(name)
    - dom.appendChild(node)
- Create XML
    - dom.toprettyxml()

To create a node with full attribute
(<name attr_key='attr_value'>text</name>)
    - node = dom.createElement(name)
    - attr = dom.createAttribute(attr_key)
    - attr.value = attr_value
    - node.setAttributeNode(attr)
    - node.appendChild(dom.createTextNode(text))
"""

import xml.dom.minidom

# Create DOM object
dom = xml.dom.minidom.Document()

def create_node(name, attr_key=None, attr_value='', text=None):
    """Create this.
    <name attr_key='attr_value'>text</name>"""
    node = dom.createElement(name)
    if attr_key:
        attr = dom.createAttribute(attr_key)
        attr.value = attr_value
        node.setAttributeNode(attr)
    if text:
        node.appendChild(dom.createTextNode(text))
    return node

# a b c d e f g
available_codes = map(lambda x:x, 'abcdefg')

urlset = create_node('urlset',
                     attr_key='xmlns',
                     attr_value='http://www.sitemaps.org/schemas/sitemap/0.9')
for code in available_codes:
    url = create_node('url')
    loc      = create_node('loc', text=f'https://www.mate.org/{code}')
    priority = create_node('priority', text='0.8')
    lastmod  = create_node('lastmod', text='2019-07-30')
    for n in [loc, priority, lastmod]:
        url.appendChild(n)
    urlset.appendChild(url)

# Convert to xml.
dom.appendChild(urlset)
print(dom.toprettyxml())

'''
<?xml version="1.0" ?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.mate.org/a</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/b</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/c</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/d</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/e</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/f</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
    <url>
        <loc>https://www.mate.org/g</loc>
        <priority>0.8</priority>
        <lastmod>2019-07-30</lastmod>
    </url>
</urlset>
'''
