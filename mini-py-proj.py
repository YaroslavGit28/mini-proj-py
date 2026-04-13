import json
import os
from datetime import datetime

class TodoList:
	def __init__(self, filename="tasks.json"):
		self.filename = filename
		self.tasks = []
		self.load_tasks()

		def load_tasks(self):
			if os.path.exists(self.filename):
				try:
					with open(self.filename, 'r', encoding='utf-8') as file:
						self.tasks = json.load(file)
				except (json.JSONDecodeErroe, FileNotFoundError):
					self.tasks = []
			else:
				self.tasks = []

		def save_tasks(self):
			with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=2)

        def add_tasks(self, title, priority='средний'):
        	task = {
        		"id": len(self.tasks) + 1,
            	"title": title,
            	"priority": priority,
            	"completed": False,
            	"created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        	}
        	self.tasks.append(task)
        	self.save_tasks()
        	print(f"Задача '{title}' добавлена!")

        def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                removed = self.tasks.pop(i)
                self.save_tasks()
                print(f"Задача '{removed['title']}' удалена!")
                return
        print(f"Задача с ID {task_id} не найдена!")

    	def complete_task(self, task_id):
        	for task in self.tasks:
           		if task["id"] == task_id:
                	if not task["completed"]:
                    	task["completed"] = True
                    	self.save_tasks()
                    	print(f"Задача '{task['title']}' выполнена! Поздравляю!")
                	else:
                    	print(f"Задача '{task['title']}' уже была выполнена ранее.")
                	return
        	print(f"Задача с ID {task_id} не найдена!")

    	def show_tasks(self, show_completed=True):
        	if not self.tasks:
            	print("\nСписок задач пуст! Добавьте новую задачу.")
            	return

        	priority_order = {"высокий": 0, "средний": 1, "низкий": 2}
        
    	    pending = [t for t in self.tasks if not t["completed"]]
        	completed = [t for t in self.tasks if t["completed"]] if show_completed else []
        
        	pending.sort(key=lambda x: priority_order.get(x["priority"], 1))
        
        	print("\n" + "="*60)
        	print("МОЙ СПИСОК ЗАДАЧ")
        	print("="*60)
        
        	if pending:
            	print("\nАКТИВНЫЕ ЗАДАЧИ:")
            	print("-"*40)
            	for task in pending:
                	priority_icon = {"высокий": "🔴", "средний": "🟡", "низкий": "🟢"}
                	print(f"[{task['id']}] {priority_icon.get(task['priority'], '⚪')} {task['title']}")
        
        	if show_completed and completed:
            	print("\nВЫПОЛНЕННЫЕ ЗАДАЧИ:")
            	print("-"*40)
            	for task in completed:
                	print(f"[{task['id']}] ✓ {task['title']}")
        
        	print("\n" + "="*60)

def main():
    todo = TodoList()
    
    while True:
        print("\nМЕНЮ УПРАВЛЕНИЯ ЗАДАЧАМИ")
        print("1️ Показать все задачи")
        print("2️ Добавить задачу")
        print("3️ Выполнить задачу")
        print("4️ Удалить задачу")
        print("5️ Редактировать задачу")
        print("6️ Очистить выполненные")
        print("7️ Статистика")
        print("0️ Выход")
        
        choice = input("\nВыберите действие: ").strip()
        
        if choice == "1":
            todo.show_tasks()
        
        elif choice == "2":
            title = input("Название задачи: ").strip()
            if title:
                print("Приоритет: 1-высокий, 2-средний, 3-низкий")
                prior_choice = input("Выберите приоритет (по умолчанию средний): ").strip()
                priority_map = {"1": "высокий", "2": "средний", "3": "низкий"}
                priority = priority_map.get(prior_choice, "средний")
                todo.add_task(title, priority)
            else:
                print("Название задачи не может быть пустым!")
        
        elif choice == "3":
            todo.show_tasks(show_completed=False)
            try:
                task_id = int(input("ID задачи, которую выполнили: "))
                todo.complete_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректный ID!")
        
        elif choice == "4":
            todo.show_tasks()
            try:
                task_id = int(input("ID задачи для удаления: "))
                todo.delete_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректный ID!")
        
        elif choice == "5":
            todo.show_tasks()
            try:
                task_id = int(input("ID задачи для редактирования: "))
                new_title = input("Новое название (оставьте пустым, чтобы не менять): ").strip()
                print("Новый приоритет: 1-высокий, 2-средний, 3-низкий (0-не менять)")
                prior_choice = input("Выберите приоритет: ").strip()
                priority_map = {"1": "высокий", "2": "средний", "3": "низкий"}
                new_priority = priority_map.get(prior_choice)
                
                todo.edit_task(task_id, new_title if new_title else None, new_priority)
            except ValueError:
                print("Пожалуйста, введите корректный ID!")
        
        elif choice == "6":
            todo.clear_completed()
        
        elif choice == "7":
            total = len(todo.tasks)
            completed = len([t for t in todo.tasks if t["completed"]])
            pending = total - completed
            print("\nСТАТИСТИКА")
            print(f"Всего задач: {total}")
            print(f"Выполнено: {completed} ({completed*100//total if total>0 else 0}%)")
            print(f"Осталось: {pending}")
        
        elif choice == "0":
            print("До свидания! Все задачи сохранены.")
            break
        
        else:


if __name__ == "__main__":
    main()
