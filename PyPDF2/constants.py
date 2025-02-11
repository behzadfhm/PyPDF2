"""
See Portable Document Format Reference Manual, 1993. ISBN 0-201-62628-4.

See https://ia802202.us.archive.org/8/items/pdfy-0vt8s-egqFwDl7L2/PDF%20Reference%201.0.pdf

PDF Reference, third edition, Version 1.4, 2001. ISBN 0-201-75839-3.

PDF Reference, sixth edition, Version 1.7, 2006.
"""


class Core:
    """Keywords that don't quite belong anywhere else."""

    OUTLINES = "/Outlines"
    PAGE = "/Page"
    PAGES = "/Pages"
    CATALOG = "/Catalog"


class TrailerKeys:
    ROOT = "/Root"
    ENCRYPT = "/Encrypt"
    ID = "/ID"
    INFO = "/Info"
    SIZE = "/Size"


class CatalogAttributes:
    NAMES = "/Names"
    DESTS = "/Dests"


class EncryptionDictAttributes:
    """
    Additional encryption dictionary entries for the standard security handler.

    TABLE 3.19, Page 122
    """

    R = "/R"  # number, required; revision of the standard security handler
    O = "/O"  # 32-byte string, required
    U = "/U"  # 32-byte string, required
    P = "/P"  # integer flag, required; permitted operations
    ENCRYPT_METADATA = "/EncryptMetadata"  # boolean flag, optional


class Ressources:
    """TABLE 3.30 Entries in a resource dictionary."""

    EXT_G_STATE = "/ExtGState"  # dictionary, optional
    COLOR_SPACE = "/ColorSpace"  # dictionary, optional
    PATTERN = "/Pattern"  # dictionary, optional
    SHADING = "/Shading"  # dictionary, optional
    XOBJECT = "/XObject"  # dictionary, optional
    FONT = "/Font"  # dictionary, optional
    PROC_SET = "/ProcSet"  # array, optional
    PROPERTIES = "/Properties"  # dictionary, optional


class PagesAttributes:
    """Page Attributes, Table 6.2, Page 52."""

    TYPE = "/Type"  # name, required; must be /Pages
    KIDS = "/Kids"  # array, required; List of indirect references
    COUNT = "/Count"  # integer, required; the number of all nodes und this node
    PARENT = "/Parent"  # dictionary, required; indirect reference to pages object


class PageAttributes:
    """TABLE 3.27 Entries in a page object."""

    TYPE = "/Type"  # name, required; must be /Page
    PARENT = "/Parent"  # dictionary, required; a pages object
    LAST_MODIFIED = (
        "/LastModified"  # date, optional; date and time of last modification
    )
    RESOURCES = "/Resources"  # dictionary, required if there are any
    MEDIABOX = "/MediaBox"  # rectangle, required; rectangle specifying page size
    CROPBOX = "/CropBox"  # rectangle, optional; rectangle
    BLEEDBOX = "/BleedBox"  # rectangle, optional; rectangle
    TRIMBOX = "/TrimBox"  # rectangle, optional; rectangle
    ARTBOX = "/ArtBox"  # rectangle, optional; rectangle
    BOX_COLOR_INFO = "/BoxColorInfo"  # dictionary, optional
    CONTENTS = "/Contents"  # stream or array, optional
    ROTATE = "/Rotate"  # integer, optional; page rotation in degrees
    GROUP = "/Group"  # dictionary, optional; page group
    THUMB = "/Thumb"  # stream, optional; indirect reference to image of the page
    B = "/B"  # array, optional
    DUR = "/Dur"  # number, optional
    TRANS = "/Trans"  # dictionary, optional
    ANNOTS = "/Annots"  # array, optional; an array of annotations
    AA = "/AA"  # dictionary, optional
    METADATA = "/Metadata"  # stream, optional
    PIECE_INFO = "/PieceInfo"  # dictionary, optional
    STRUCT_PARENTS = "/StructParents"  # integer, optional
    ID = "/ID"  # byte string, optional
    PZ = "/PZ"  # number, optional
    TABS = "/Tabs"  # name, optional
    TEMPLATE_INSTANTIATED = "/TemplateInstantiated"  # name, optional
    PRES_STEPS = "/PresSteps"  # dictionary, optional
    USER_UNIT = "/UserUnit"  # number, optional
    VP = "/VP"  # dictionary, optional


class StreamAttributes:
    """Table 4.2."""

    LENGTH = "/Length"  # integer, required
    FILTER = "/Filter"  # name or array of names, optional
    DECODE_PARMS = "/DecodeParms"  # variable, optional -- 'decodeParams is wrong


class FilterTypes:
    """
    Table 4.3 of the 1.4 Manual.

    Page 354 of the 1.7 Manual
    """

    ASCII_HEX_DECODE = "/ASCIIHexDecode"  # abbreviation: AHx
    ASCII_85_DECODE = "/ASCII85Decode"  # abbreviation: A85
    LZW_DECODE = "/LZWDecode"  # abbreviation: LZW
    FLATE_DECODE = "/FlateDecode"  # abbreviation: Fl, PDF 1.2
    RUN_LENGTH_DECODE = "/RunLengthDecode"  # abbreviation: RL
    CCITT_FAX_DECODE = "/CCITTFaxDecode"  # abbreviation: CCF
    DCT_DECODE = "/DCTDecode"  # abbreviation: DCT


class FilterTypeAbbreviations:
    """Table 4.44 of the 1.7 Manual (page 353ff)."""

    AHx = "/AHx"
    A85 = "/A85"
    LZW = "/LZW"
    FL = "/Fl"  # FlateDecode
    RL = "/RL"
    CCF = "/CCF"
    DCT = "/DCT"


class LzwFilterParameters:
    """Table 4.4."""

    PREDICTOR = "/Predictor"  # integer
    COLUMNS = "/Columns"  # integer
    COLORS = "/Colors"  # integer
    BITS_PER_COMPONENT = "/BitsPerComponent"  # integer
    EARLY_CHANGE = "/EarlyChange"  # integer


class CcittFaxDecodeParameters:
    """Table 4.5."""

    K = "/K"  # integer
    END_OF_LINE = "/EndOfLine"  # boolean
    ENCODED_BYTE_ALIGN = "/EncodedByteAlign"  # boolean
    COLUMNS = "/Columns"  # integer
    ROWS = "/Rows"  # integer
    END_OF_BLOCK = "/EndOfBlock"  # boolean
    BLACK_IS_1 = "/BlackIs1"  # boolean
    DAMAGED_ROWS_BEFORE_ERROR = "/DamagedRowsBeforeError"  # integer


class ImageAttributes:
    """Table 6.20."""

    TYPE = "/Type"  # name, required; must be /XObject
    SUBTYPE = "/Subtype"  # name, required; must be /Image
    NAME = "/Name"  # name, required
    WIDTH = "/Width"  # integer, required
    HEIGHT = "/Height"  # integer, required
    BITS_PER_COMPONENT = "/BitsPerComponent"  # integer, required
    COLOR_SPACE = "/ColorSpace"  # name, required
    DECODE = "/Decode"  # array, optional
    INTERPOLATE = "/Interpolate"  # boolean, optional
    IMAGE_MASK = "/ImageMask"  # boolean, optional


class ColorSpaces:
    DEVICE_RGB = "/DeviceRGB"
    DEVICE_CMYK = "/DeviceCMYK"
    DEVICE_GRAY = "/DeviceGray"


class TypArguments:
    """Table 8.2 of the PDF 1.7 reference."""

    LEFT = "/Left"
    RIGHT = "/Right"
    BOTTOM = "/Bottom"
    TOP = "/Top"


class TypFitArguments:
    """Table 8.2 of the PDF 1.7 reference."""

    FIT = "/Fit"
    FIT_V = "/FitV"
    FIT_BV = "/FitBV"
    FIT_B = "/FitB"
    FIT_H = "/FitH"
    FIT_BH = "/FitBH"
    FIT_R = "/FitR"


class FieldDistionaryAttributes:
    """TABLE 8.69 Entries common to all field dictionaries (PDF 1.7 reference)."""

    FT = "/FT"  # name, required for terminal fields
    Parent = "/Parent"  # dictionary, required for children
    Kids = "/Kids"  # array, sometimes required
    T = "/T"  # text string, optional
    TU = "/TU"  # text string, optional
    TM = "/TM"  # text string, optional
    Ff = "/Ff"  # integer, optional
    V = "/V"  # text string, optional
    DV = "/DV"  # text string, optional
    AA = "/AA"  # dictionary, optional


class DocumentInformationAttributes:
    """TABLE 10.2 Entries in the document information dictionary."""

    TITLE = "/Title"  # text string, optional
    AUTHOR = "/Author"  # text string, optional
    SUBJECT = "/Subject"  # text string, optional
    KEYWORDS = "/Keywords"  # text string, optional
    CREATOR = "/Creator"  # text string, optional
    PRODUCER = "/Producer"  # text string, optional
    CREATION_DATE = "/CreationDate"  # date, optional
    MOD_DATE = "/ModDate"  # date, optional
    TRAPPED = "/Trapped"  # name, optional


class PageLayouts:
    """Page 84, PDF 1.4 reference."""

    SINGLE_PAGE = "/SinglePage"
    ONE_COLUMN = "/OneColumn"
    TWO_COLUMN_LEFT = "/TwoColumnLeft"
    TWO_COLUMN_RIGHT = "/TwoColumnRight"


class GraphicsStateParameters:
    """Table 4.8 of the 1.7 reference."""

    TYPE = "/Type"  # name, optional
    LW = "/LW"  # number, optional
    # TODO: Many more!
    FONT = "/Font"  # array, optional
    S_MASK = "/SMask"  # dictionary or name, optional


class CatalogDictionary:
    """Table 3.25 in the 1.7 reference."""

    TYPE = "/Type"  # name, required; must be /Catalog
    VERSION = "/Version"  # name
    PAGES = "/Pages"  # dictionary, required
    PAGE_LABELS = "/PageLabels"  # number tree, optional
    NAMES = "/Names"  # dictionary, optional
    DESTS = "/Dests"  # dictionary, optional
    VIEWER_PREFERENCES = "/ViewerPreferences"  # dictionary, optional
    PAGE_LAYOUT = "/PageLayout"  # name, optional
    PAGE_MODE = "/PageMode"  # name, optional
    OUTLINES = "/Outlines"  # dictionary, optional
    THREADS = "/Threads"  # array, optional
    OPEN_ACTION = "/OpenAction"  # array or dictionary or name, optional
    AA = "/AA"  # dictionary, optional
    URI = "/URI"  # dictionary, optional
    ACRO_FORM = "/AcroForm"  # dictionary, optional
    METADATA = "/Metadata"  # stream, optional
    STRUCT_TREE_ROOT = "/StructTreeRoot"  # dictionary, optional
    MARK_INFO = "/MarkInfo"  # dictionary, optional
    LANG = "/Lang"  # text string, optional
    SPIDER_INFO = "/SpiderInfo"  # dictionary, optional
    OUTPUT_INTENTS = "/OutputIntents"  # array, optional
    PIECE_INFO = "/PieceInfo"  # dictionary, optional
    OC_PROPERTIES = "/OCProperties"  # dictionary, optional
    PERMS = "/Perms"  # dictionary, optional
    LEGAL = "/Legal"  # dictionary, optional
    REQUIREMENTS = "/Requirements"  # array, optional
    COLLECTION = "/Collection"  # dictionary, optional
    NEEDS_RENDERING = "/NeedsRendering"  # boolean, optional


PDF_KEYS = (
    PagesAttributes,
    PageAttributes,
    Ressources,
    EncryptionDictAttributes,
    ImageAttributes,
    StreamAttributes,
    FilterTypes,
    LzwFilterParameters,
    TypArguments,
    TypFitArguments,
    PageLayouts,
    GraphicsStateParameters,
    CatalogDictionary,
    Core,
    TrailerKeys,
    CatalogAttributes,
)
