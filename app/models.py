class Sources:
    '''
    Class that defines the sources object
    '''
    def __init__(self, id, name, description, url, category, country):
        '''
        Function that initiates the source class
        '''
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.country = country


class Articles:
    '''
    Class that defines the article objects
    '''
    def __init__(self, author, title, description, url,urlToImage, publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt