

from bson.objectid import ObjectId


async def populate_object(object_id, collection):
    object = await collection.find_one({"_id": ObjectId(object_id)})
    return object


async def populate_array(array_ids, collection, key="_id"):
    objects = await collection.find({key: {'$in': array_ids}}).to_list(length=None)
    return objects
