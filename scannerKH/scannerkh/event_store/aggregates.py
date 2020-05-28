from eventsourcing.domain.model.aggregate import AggregateRoot


class ArticleAggregate(AggregateRoot):
    def __init__(self, **kwargs):
        super(ArticleAggregate, self).__init__(**kwargs)
        self.articles = []

    def create_article(self, article):
        self.__trigger_event__(ArticleAggregate.ArticleCreator, what=article)

    def update_article(self, article):
        self.__trigger_event__(ArticleAggregate.ArticleUpdater, what=article)

    def remove_article(self, article):
        self.__trigger_event__(ArticleAggregate.ArticleRemover, what=article)

    class ArticleCreator(AggregateRoot.Event):
        def mutate(self, obf):
            pass

    class ArticleUpdater(AggregateRoot.Event):
        def mutate(self, obf):
            pass

    class ArticleRemover(AggregateRoot.Event):
        def mutate(self, obf):
            pass
