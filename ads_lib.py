import math
import requests


def journal_names():
    # from http://astro.dur.ac.uk/~cole/Intro_LaTeX_PG/PhDthesis/rcrain/aas_macros.sty

    short_name = {}
    long_name = {}

    short_name['\\aj'] = 'AJ'
    short_name['\\araa'] = 'ARA\&A'
    short_name['\\apj'] = 'ApJ'
    short_name['\\apjl'] = 'ApJ'
    short_name['\\apjs'] = 'ApJS'
    short_name['\\ao'] = 'Appl.~Opt.'
    short_name['\\apss'] = 'Ap\&SS'
    short_name['\\aap'] = 'A\&A'
    short_name['\\aapr'] = 'A\&A~Rev.'
    short_name['\\aaps'] = 'A\&AS'
    short_name['\\azh'] = 'AZh'
    short_name['\\baas'] = 'BAAS'
    short_name['\\jrasc'] = 'JRASC'
    short_name['\\memras'] = 'MmRAS'
    short_name['\\mnras'] = 'MNRAS'
    short_name['\\pra'] = 'Phys.~Rev.~A'
    short_name['\\prb'] = 'Phys.~Rev.~B'
    short_name['\\prc'] = 'Phys.~Rev.~C'
    short_name['\\prd'] = 'Phys.~Rev.~D'
    short_name['\\pre'] = 'Phys.~Rev.~E'
    short_name['\\prl'] = 'Phys.~Rev.~Lett.'
    short_name['\\pasp'] = 'PASP'
    short_name['\\pasj'] = 'PASJ'
    short_name['\\qjras'] = 'QJRAS'
    short_name['\\skytel'] = 'S\&T'
    short_name['\\solphys'] = 'Sol.~Phys.'
    short_name['\\sovast'] = 'Soviet~Ast.'
    short_name['\\ssr'] = 'Space~Sci.~Rev.'
    short_name['\\zap'] = 'ZAp'
    short_name['\\nat'] = 'Nature'
    short_name['\\iaucirc'] = 'IAU~Circ.'
    short_name['\\aplett'] = 'Astrophys.~Lett.'
    short_name['\\apspr'] = 'Astrophys.~Space~Phys.~Res.'
    short_name['\\bain'] = 'Bull.~Astron.~Inst.~Netherlands'
    short_name['\\fcp'] = 'Fund.~Cosmic~Phys.'
    short_name['\\gca'] = 'Geochim.~Cosmochim.~Acta'
    short_name['\\grl'] = 'Geophys.~Res.~Lett.'
    short_name['\\jcp'] = 'J.~Chem.~Phys.'
    short_name['\\jgr'] = 'J.~Geophys.~Res.'
    short_name['\\jqsrt'] = 'J.~Quant.~Spec.~Radiat.~Transf.'
    short_name['\\memsai'] = 'Mem.~Soc.~Astron.~Italiana'
    short_name['\\nphysa'] = 'Nucl.~Phys.~A'
    short_name['\\physrep'] = 'Phys.~Rep.'
    short_name['\\physscr'] = 'Phys.~Scr'
    short_name['\\planss'] = 'Planet.~Space~Sci.'
    short_name['\\procspie'] = 'Proc.~SPIE'
    # additional
    short_name['\\nar'] = 'New~Astr.~Rev.'
    short_name['\\na'] = 'New~Astr.'
    short_name['\\rmxaa'] = 'Rev.~Mexicana~de~Astron.~y~Astrof.'
    short_name['\\icarus'] = 'Icarus'
    short_name['\\pasa'] = 'PASA'
    short_name['\\jcap'] = 'JCAP'
    short_name['\\caa'] = 'ChA&A'

    long_name['\\aj'] = 'Astronomical Journal'
    long_name['\\araa'] = 'Annual Review of Astron and Astrophys'
    long_name['\\apj'] = 'Astrophysical Journal'
    long_name['\\apjl'] = 'Astrophysical Journal, Letters'
    long_name['\\apjs'] = 'Astrophysical Journal, Supplement'
    long_name['\\ao'] = 'Applied Optics'
    long_name['\\apss'] = 'Astrophysics and Space Science'
    long_name['\\aap'] = 'Astronomy and Astrophysics'
    long_name['\\aapr'] = 'Astronomy and Astrophysics Reviews'
    long_name['\\aaps'] = 'Astronomy and Astrophysics, Supplement'
    long_name['\\azh'] = 'Astronomicheskii Zhurnal'
    long_name['\\baas'] = 'Bulletin of the AAS'
    long_name['\\jrasc'] = 'Journal of the RAS of Canada'
    long_name['\\memras'] = 'Memoirs of the RAS'
    long_name['\\mnras'] = 'Monthly Notices of the RAS'
    long_name['\\pra'] = 'Physical Review A: General Physics'
    long_name['\\prb'] = 'Physical Review B: Solid State'
    long_name['\\prc'] = 'Physical Review C'
    long_name['\\prd'] = 'Physical Review D'
    long_name['\\pre'] = 'Physical Review E'
    long_name['\\prl'] = 'Physical Review Letters'
    long_name['\\pasp'] = 'Publications of the ASP'
    long_name['\\pasj'] = 'Publications of the ASJ'
    long_name['\\qjras'] = 'Quarterly Journal of the RAS'
    long_name['\\skytel'] = 'ky and Telescope'
    long_name['\\solphys'] = 'Solar Physics'
    long_name['\\sovast'] = 'Soviet Astronomy'
    long_name['\\ssr'] = 'Space Science Reviews'
    long_name['\\zap'] = 'Zeitschrift fuer Astrophysik'
    long_name['\\nat'] = 'Nature'
    long_name['\\iaucirc'] = 'IAU Cirulars'
    long_name['\\aplett'] = 'Astrophysics Letters'
    long_name['\\apspr'] = 'Astrophysics Space Physics Research'
    long_name['\\bain'] = 'Bulletin Astronomical Institute of the Netherlands'
    long_name['\\fcp'] = 'Fundamental Cosmic Physics'
    long_name['\\gca'] = 'Geochimica Cosmochimica Acta'
    long_name['\\grl'] = 'Geophysics Research Letters'
    long_name['\\jcp'] = 'Journal of Chemical Physics'
    long_name['\\jgr'] = 'Journal of Geophysics Research'
    long_name['\\jqsrt'] = 'Journal of Quantitiative Spectroscopy and Radiative Transfer'
    long_name['\\memsai'] = 'Mem. Societa Astronomica Italiana'
    long_name['\\nphysa'] = 'Nuclear Physics A'
    long_name['\\physrep'] = 'Physics Reports'
    long_name['\\physscr'] = 'Physica Scripta'
    long_name['\\planss'] = 'Planetary Space Science'
    long_name['\\procspie'] = 'Proceedings of the SPIE'
    #
    long_name['\\nar'] = 'New Astronomy Review'
    long_name['\\na'] = 'New Astronomy'
    long_name['\\rmxaa'] = 'Revista Mexicana de Astronomia y Astrofisica'
    long_name['\\icarus'] = 'Icarus'
    long_name['\\pasa'] = 'Publications of the Astronomical Society of Australia'
    long_name['\\jcap'] = 'Journal of Cosmology and Astroparticle Physics'
    long_name['\\caa'] = 'Chinese Astronomy and Astrophysics'
    return short_name, long_name


def get_library(library_id, num_documents, config):
    # from https://github.com/adsabs/ads-examples/blob/master/library_csv/lib_2_csv.py
    """
    Get the content of a library when you know its id. As we paginate the
    requests from the private library end point for document retrieval,
    we have to repeat requests until we have all documents.
    :param library_id: identifier of the library
    :type library_id:
    :param num_documents: number of documents in the library
    :type num_documents: int
    :return: list
    """

    start = 0
    rows = 2000  # max number of list length from API
    num_paginates = int(math.ceil(num_documents / (1.0*rows)))
    documents = []
    for i in range(num_paginates):
        #print('Pagination {} out of {}'.format(i+1, num_paginates))

        r = requests.get(
            '{}/libraries/{id}?start={start}&rows={rows}'.format(
                config['url'],
                id=library_id,
                start=start,
                rows=rows
            ),
            headers=config['headers']
        )

        # Get all the documents that are inside the library
        try:
            data = r.json()['documents']
        except ValueError:
            raise ValueError(r.text)

        documents.extend(data)

        start += rows

    return documents


def fix_authornames(bib_str):
    # the bib_str is the ourput of response.json()['export']
    export = bib_str.split('\n')
    tt = []
    for e in export:
        if '@' in e:
            tt.append(e.replace(' ', '-'))
        else:
            tt.append(e)
    bib = '\n'.join(tt)

    return bib


def fix_journal_abbr(bib_str, format='short'):
    # the bib_str is the ourput of response.json()['export']
    # 'short' prints abbreviated journal name; e.g. A&A, MNRAS, ApJ
    # 'long' prints full name; Astronomy & Astrophysics
    short_name, long_name = journal_names()

    journal_dict = short_name
    if format == 'long':
        journal_dict = long_name

    export = bib_str.split('\n')
    tt = []
    for e in export:
        if 'journal' in e:
            head = e.split('{')
            tail = head[1].split('}')
            journal = tail[0]
            if journal[0] == '\\':
                name = journal_dict[journal]
                new_name = head[0] + '{' + name + '}' + tail[1]
                tt.append(new_name)
        else:
            tt.append(e)
    bib = '\n'.join(tt)

    return bib
