from itertools import islice
import yaml


class Seed:
    def __init__(self, session):
        self.session = session

    def import_yml(self, Model, yaml_path,
                   each=1000, clean=False, autocommit=True):
        data = self._load_yaml(yaml_path)
        records = [Model(**record) for record in data]

        if clean:
            self._before_delete(Model)

        try:
            for chunked_records in self._chunk(records, size=each):
                self.session.bulk_save_objects(
                    chunked_records, return_defaults=True)
        except Exception as e:
            self.session.rollback()
            raise e
        else:
            if autocommit:
                self.session.commit()

    def _before_delete(self, Model):
        Model.query.delete()

    def _load_yaml(self, yaml_path):
        with open(yaml_path) as stream:
            return yaml.load(stream)

    def _chunk(self, it, size):
        it = iter(it)
        return iter(lambda: tuple(islice(it, size)), ())
