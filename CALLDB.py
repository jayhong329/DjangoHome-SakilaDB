from DB_DEMO import Category

#刪除
print(Category.category_delete(18))
#修改
# print(Category.category_upodate(18, "xyz"))
#新增
# print(Category.category_create("abc"))
# 讀取
print(Category.category_all())
print(Category.category_single(1))