class Todo:
    def __init__(self,title):
        self.title = title
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def __str__(self):
        return f"[{'√' if self.completed else ' '}] {self.title}"

def load_todos(filename):
    todos = []
    try:
        with open(filename,'r') as f:
            for line in f:
                title = line.strip()
                todos.append(Todo(title))
    except FileNotFoundError:
        print("待办事项文件未找到，已创建文件。")
    return todos

def save_todos(todos,filename):
    with open(filename,'w') as f:
        for todo in todos:
            f.write(todo.title+'\n')

def display_todos(todos):
    for i,todo in enumerate(todos):
        print(f"{i}. {todo}")

def main():
    filename = 'todos.txt'
    todos = load_todos(filename)

    while True:
        print("\n待办事项管理器")
        display_todos(todos)
        print("\n1. 添加待办事项")
        print("2. 标记待办事项为完成")
        print("3. 退出")

        choice = input("请选择一个选项: ")

        if choice == '1':
            title = input("请输入待办事项: ")
            todos.append(Todo(title))
            save_todos(todos, filename)
        elif choice == '2':
            index = int(input("请输入要标记为完成的事项编号: ")) - 1
            if 0 <= index < len(todos):
                todos[index].mark_completed()
                save_todos(todos, filename)
            else:
                print("无效的编号！")
        elif choice == '3':
            print("再见！")
            break
        else:
            print("无效的选项，请重新选择。")

if __name__ == "__main__":
    main()