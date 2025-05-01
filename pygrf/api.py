from io import BufferedReader
from .exceptions import GRFParseError
from . import gat, grf_v1, grf_v2, grf_v3, spr, act


def open_grf(fp: BufferedReader) -> any:
    """
    Open a GRF archive

    :param filename: the path to the grf archive file
    """
    grf = None
    try:
        grf = grf_v3.GRF(fp)
    except GRFParseError:
        try:
            # If the file is not a GRF v3, try to parse it as GRF v2
            fp.seek(0)
            grf = grf_v2.GRF(fp)
        except GRFParseError:
            try:
                # If the file is not a GRF v2, try to parse it as GRF v1
                fp.seek(0)
                grf = grf_v1.GRF(fp)
            except GRFParseError as ex:
                raise GRFParseError(f"Failed to parse GRF file: {ex}")
    return grf

def open_grf_v1(fp: BufferedReader) -> grf_v1.GRF|None:
    """
    Open a GRF archive

    :param filename: the path to the grf archive file
    """
    grf = None
    try:
        grf = grf_v1.GRF(fp)
    except GRFParseError as ex:
        raise GRFParseError(f"Failed to parse GRF file: {ex}")
    return grf

def open_grf_v2(fp: BufferedReader) -> grf_v2.GRF|None:
    """
    Open a GRF archive

    :param filename: the path to the grf archive file
    """
    grf = None
    try:
        grf = grf_v2.GRF(fp)
    except GRFParseError as ex:
        raise GRFParseError(f"Failed to parse GRF file: {ex}")
    return grf

def open_grf_v3(fp: BufferedReader) -> grf_v3.GRF|None:
    """
    Open a GRF archive

    :param filename: the path to the grf archive file
    """
    grf = None
    try:
        grf = grf_v3.GRF(fp)
    except GRFParseError as ex:
        raise GRFParseError(f"Failed to parse GRF file: {ex}")
    return grf

def open_gat(filename: str) -> gat.GAT:
    """
    Open a GAT file

    :param filename: the path to the gat file
    """
    return gat.GAT(open(filename, 'rb'))


def open_spr(filename: str) -> spr.SPR:
    """
    Open a SPR file

    :param filename: the path to the spr file
    """
    with open(filename, 'rb') as f:
        return spr.SPR(f.read())


def open_act(filename: str) -> act.ACT:
    """
    Open a ACT file

    :param filename: the path to the act file
    """
    return act.ACT(open(filename, 'rb'))
