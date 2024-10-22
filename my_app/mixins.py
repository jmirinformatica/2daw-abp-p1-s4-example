from . import db_manager as db
from sqlalchemy.ext.hybrid import hybrid_property
from collections import OrderedDict
from sqlalchemy.engine.row import Row
from sqlalchemy.orm.collections import InstrumentedList

class BaseMixin():
    
    @classmethod
    def create(cls, **kwargs):
        r = cls(**kwargs)
        return r.save()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self.save()
    
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except:
            return False
        
    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except:
            return False

class SerializableMixin():

    exclude_attr = []

    def to_dict(self, max_levels=0):
        return self.__recursive_to_dict(max_levels)
    
    def __recursive_to_dict(self, level):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            if key not in self.__class__.exclude_attr:
                result[key] = getattr(self, key)
        
        for key in self.__mapper__.all_orm_descriptors:
            if type(key) == hybrid_property:
                name = key.__name__
                result[name] = getattr(self, name)
            
        for key in self.__mapper__.relationships.keys():
            if key not in self.__class__.exclude_attr:
                value = getattr(self, key)
                if isinstance(value, SerializableMixin):
                    if level > 0:
                        result[key] = value.__recursive_to_dict(level - 1)
                elif isinstance(value, InstrumentedList):
                    if level > 0:
                        result[key] = []
                        for x in value:
                            if isinstance(x, SerializableMixin):
                                result[key].append(x.__recursive_to_dict(level - 1))
        return result

    @staticmethod
    def to_dict_collection(collection, max_levels=0):
        result = []
        for x in collection:
            if isinstance(x, Row):
                obj = {}
                first = True
                for y in x:
                    if isinstance(y, SerializableMixin):
                        if first:
                            # model
                            obj = y.to_dict()
                            first = False
                        elif y:
                            # relationships
                            key = y.__class__.__name__.lower()
                            obj[key] = y.to_dict()
                result.append(obj)

            if isinstance(x, SerializableMixin):
                result.append(x.to_dict(max_levels))
               
        return result
