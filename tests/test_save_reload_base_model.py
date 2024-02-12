# tests/test_save_reload_base_model.py
import unittest
from models import storage
from models.base_model import BaseModel
import os

class TestSaveReloadBaseModel(unittest.TestCase):
    def test_save_reload_base_model(self):
        all_objs = storage.all()
        self.assertEqual(len(all_objs), 0)
        
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model.save()

        all_objs = storage.all()
        self.assertEqual(len(all_objs), 1)

        my_model_id = list(all_objs.keys())[0]
        self.assertTrue(my_model_id in all_objs)

        my_model_copy = all_objs[my_model_id]
        self.assertEqual(my_model.name, my_model_copy.name)
        self.assertEqual(my_model.my_number, my_model_copy.my_number)

        os.remove("file.json")

if __name__ == "__main__":
    unittest.main()
