import xml.etree.ElementTree as ET
from xml.dom import minidom

def create_layered_svg(filename="layered_design.svg"):
    """
    Generates a simple SVG file with multiple layers (groups) and elements,
    demonstrating programmatic creation of structured design assets.
    This concept aligns with preparing editable layers for modern design tools.
    """
    # Create the root SVG element
    svg = ET.Element("svg", {
        "width": "400",
        "height": "300",
        "viewBox": "0 0 400 300",
        "xmlns": "http://www.w3.org/2000/svg"
    })

    # Layer 1: Background Rectangle
    # This represents a base layer in a design, using an SVG <g> element.
    layer1 = ET.SubElement(svg, "g", {"id": "background_layer"})
    ET.SubElement(layer1, "rect", {
        "x": "0", "y": "0", "width": "400", "height": "300",
        "fill": "#f0f0f0"
    })

    # Layer 2: Shape Layer
    # This represents a layer containing primary design shapes, also a <g> element.
    layer2 = ET.SubElement(svg, "g", {"id": "shape_layer"})
    ET.SubElement(layer2, "circle", {
        "cx": "150", "cy": "150", "r": "80",
        "fill": "#ffcc00", "stroke": "#cc9900", "stroke-width": "5"
    })
    ET.SubElement(layer2, "rect", {
        "x": "200", "y": "100", "width": "100", "height": "100",
        "fill": "#66ccff", "stroke": "#3399cc", "stroke-width": "3"
    })

    # Layer 3: Text Layer
    # This represents a layer for textual content, allowing easy selection and editing of text.
    layer3 = ET.SubElement(svg, "g", {"id": "text_layer"})
    text_element = ET.SubElement(layer3, "text", {
        "x": "50", "y": "50",
        "font-family": "Arial, sans-serif", "font-size": "24", "fill": "#333333"
    })
    text_element.text = "Hello, Figma World!"

    text_element2 = ET.SubElement(layer3, "text", {
        "x": "50", "y": "250",
        "font-family": "Verdana, sans-serif", "font-size": "18", "fill": "#666666"
    })
    text_element2.text = "Editable Layers Example"

    # Pretty print the XML
    rough_string = ET.tostring(svg, 'utf-8')
    reparsed_string = minidom.parseString(rough_string)
    pretty_xml_as_string = reparsed_string.toprettyxml(indent="  ")

    # Save to file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(pretty_xml_as_string)
    print(f"Generated {filename} with layered SVG content.")

if __name__ == "__main__":
    create_layered_svg()
