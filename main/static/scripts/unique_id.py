
from strgen import StringGenerator

def uu_id(doc_tag):
    """ 
    Doc Tags: String( doc, app, job, user, item)
    """
    tags = dict(
        doc='[h-z5-9]{8:16}',
        app='[a-z0-9]{16:32}',
        job='[a-j0-7]{8:8}',
        user='[0-9]{4:6}',
        item='[a-n1-9]{8:8}'
        )
    if doc_tag == 'user':
        u_id =  StringGenerator(tags[doc_tag]).render(unique=True)
        u_id = 'U{}'.format(u_id)
    else:
        u_id =  StringGenerator(tags[doc_tag]).render(unique=True)
    return u_id
print(uu_id('doc'))
