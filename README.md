# XML Data Extractor

This Python script extracts data from an XML file based on a specified root path and a list of nodes.

## Installation

This script requires Python 3 and the `xmltodict` library. To install `xmltodict`, run the following command:

`pip install xmltodict`

## Usage
To use the script, run the following command in the terminal:

`python extract_data.py ROOT_PATH NODE1 NODE2 ...`

- `ROOT_PATH` is the root path of the XML document, specified as a series of node names separated by slashes ("/"). For example, if the root element of the XML document is `<root>`, and you want to extract data from its child element `<parent>`, which in turn has a child element `<child>`, you would specify the root path as `"root/parent/child"`.
- `NODE1`, `NODE2`, etc. are the names of the nodes you want to extract data from. These should be specified as separate arguments after the root path. For example, if you want to extract the values of the `name` and `age` nodes from the XML document, you would specify the nodes as `"name"` and `"age"`, respectively.

The script will output the values of the specified nodes for each occurrence of the root path in the XML document. If a specified node does not exist for a given occurrence of the root path, the output will be `"N/A"`.

## Example

Suppose you have an XML file `data.xml` with the following contents:

```xml
<root>
    <parent>
        <child>
            <name>John</name>
            <age>30</age>
        </child>
        <child>
            <name>Jane</name>
            <age>25</age>
        </child>
    </parent>
</root>
```

To extract the values of the name and age nodes for each occurrence of the path "root/parent/child", you would run the following command:

```python extract_data.py root/parent/child name age```

The output would be:

```
John,30
Jane,25
```

