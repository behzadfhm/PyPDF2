import binascii
import os
import sys
from io import BytesIO

import pytest

from PyPDF2 import PdfReader
from PyPDF2.constants import PageAttributes as PG
from PyPDF2.errors import PdfReadWarning

from . import get_pdf_from_url

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.dirname(TESTS_ROOT)
RESOURCE_ROOT = os.path.join(PROJECT_ROOT, "resources")

sys.path.append(PROJECT_ROOT)


def test_PdfReaderFileLoad():
    """
    Test loading and parsing of a file. Extract text of the file and compare to expected
    textual output. Expected outcome: file loads, text matches expected.
    """

    with open(os.path.join(RESOURCE_ROOT, "crazyones.pdf"), "rb") as inputfile:
        # Load PDF file from file
        reader = PdfReader(inputfile)
        page = reader.pages[0]

        # Retrieve the text of the PDF
        with open(os.path.join(RESOURCE_ROOT, "crazyones.txt"), "rb") as pdftext_file:
            pdftext = pdftext_file.read()

        text = page.extract_text(Tj_sep="", TJ_sep="").encode("utf-8")

        # Compare the text of the PDF to a known source
        for expected_line, actual_line in zip(text.split(b"\n"), pdftext.split(b"\n")):
            assert expected_line == actual_line

        assert text == pdftext, (
            "PDF extracted text differs from expected value.\n\nExpected:\n\n%r\n\nExtracted:\n\n%r\n\n"
            % (pdftext, text)
        )


def test_PdfReaderJpegImage():
    """
    Test loading and parsing of a file. Extract the image of the file and compare to expected
    textual output. Expected outcome: file loads, image matches expected.
    """

    with open(os.path.join(RESOURCE_ROOT, "jpeg.pdf"), "rb") as inputfile:
        # Load PDF file from file
        reader = PdfReader(inputfile)

        # Retrieve the text of the image
        with open(os.path.join(RESOURCE_ROOT, "jpeg.txt")) as pdftext_file:
            imagetext = pdftext_file.read()

        page = reader.pages[0]
        x_object = page[PG.RESOURCES]["/XObject"].get_object()
        data = x_object["/Im4"].get_data()

        # Compare the text of the PDF to a known source
        assert binascii.hexlify(data).decode() == imagetext, (
            "PDF extracted image differs from expected value.\n\nExpected:\n\n%r\n\nExtracted:\n\n%r\n\n"
            % (imagetext, binascii.hexlify(data).decode())
        )


def test_decrypt():
    with open(
        os.path.join(RESOURCE_ROOT, "libreoffice-writer-password.pdf"), "rb"
    ) as inputfile:
        reader = PdfReader(inputfile)
        assert reader.is_encrypted is True
        reader.decrypt("openpassword")
        assert len(reader.pages) == 1
        assert reader.is_encrypted is True
        metadict = reader.metadata
        assert dict(metadict) == {
            "/CreationDate": "D:20220403203552+02'00'",
            "/Creator": "Writer",
            "/Producer": "LibreOffice 6.4",
        }


def test_text_extraction_encrypted():
    inputfile = os.path.join(RESOURCE_ROOT, "libreoffice-writer-password.pdf")
    reader = PdfReader(inputfile)
    assert reader.is_encrypted is True
    reader.decrypt("openpassword")
    assert (
        reader.pages[0]
        .extract_text()
        .replace("\n", "")
        .strip()
        .startswith("Lorem ipsum dolor sit amet")
    )


@pytest.mark.parametrize("degree", [0, 90, 180, 270, 360, -90])
def test_rotate(degree):
    with open(os.path.join(RESOURCE_ROOT, "crazyones.pdf"), "rb") as inputfile:
        reader = PdfReader(inputfile)
        page = reader.pages[0]
        page.rotate(degree)


def test_rotate_45():
    with open(os.path.join(RESOURCE_ROOT, "crazyones.pdf"), "rb") as inputfile:
        reader = PdfReader(inputfile)
        page = reader.pages[0]
        with pytest.raises(ValueError) as exc:
            page.rotate(45)
        assert exc.value.args[0] == "Rotation angle must be a multiple of 90"


@pytest.mark.parametrize(
    ("enable", "url", "pages"),
    [
        (True, "https://arxiv.org/pdf/2201.00214.pdf", [0, 1, 5, 10]),
        (
            True,
            "https://github.com/py-pdf/sample-files/raw/main/009-pdflatex-geotopo/GeoTopo.pdf",
            [0, 1, 5, 10],
        ),
        (True, "https://arxiv.org/pdf/2201.00151.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/1707.09725.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00021.pdf", [0, 1, 5, 8]),
        (True, "https://arxiv.org/pdf/2201.00037.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00069.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00178.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00201.pdf", [0, 1, 5, 8]),
        (True, "https://arxiv.org/pdf/1602.06541.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00200.pdf", [0, 1, 5, 6]),
        (True, "https://arxiv.org/pdf/2201.00022.pdf", [0, 1, 5, 10]),
        (True, "https://arxiv.org/pdf/2201.00029.pdf", [0, 1, 6, 10]),
        # 6 instead of 5: as there is an issue in page 5 (missing objects)
        # and too complex to handle the warning without hiding real regressions
        (True, "https://arxiv.org/pdf/1601.03642.pdf", [0, 1, 5, 7]),
        (
            True,
            "https://github.com/py-pdf/PyPDF2/files/3796761/17343_2008_Order_09-Jan-2019.pdf",
            [0, 1],
        ),
        (
            True,
            "https://github.com/py-pdf/PyPDF2/files/8884471/ssi_manwaring.pdf",
            [0, 1],
        ),
        (True, "https://github.com/py-pdf/PyPDF2/files/8884469/999092.pdf", [0, 1]),
        (
            True,
            "file://" + os.path.join(RESOURCE_ROOT, "test Orient.pdf"),
            [0],
        ),  # TODO: preparation of text orientation validation
        (
            True,
            "https://github.com/py-pdf/PyPDF2/files/8884470/fdocuments.in_sweet-fundamentals-of-crystallography.pdf",
            [0, 1, 34, 35, 36, 118, 119, 120, 121],
        ),
        (True, "https://github.com/py-pdf/PyPDF2/files/8884493/998167.pdf", [0]),
        (
            True,
            "https://corpora.tika.apache.org/base/docs/govdocs1/971/971703.pdf",
            [0, 1, 5, 8, 14],
        ),
        (  # faulty PDF, wrongly linearized and with 2 trailer, second with /Root
            True,
            "https://corpora.tika.apache.org/base/docs/govdocs1/989/989691.pdf",
            [0],
        ),
    ],
)
def test_extract_textbench(enable, url, pages, print_result=False):
    if not enable:
        return
    try:
        reader = PdfReader(BytesIO(get_pdf_from_url(url, url.split("/")[-1])))
        for page_number in pages:
            if print_result:
                print(f"**************** {url} / page {page_number} ****************")
            rst = reader.pages[page_number].extract_text()
            if print_result:
                print(f"{rst}\n*****************************\n")
    except PdfReadWarning:
        pass
