# Анализ диалогов в художественном тексте

# 1. Создать список реплик
replicas = [
    "Я не знаю, что делать",
    "Ты должен принять решение",
    "Я боюсь ошибиться",
    "Но ты сказал, что готов к переменам",
    "Я действительно так думал",
    "А теперь передумал?",
    "Нет, просто я понял, что сказал слишком поспешно"
]

print("1. Исходный список реплик:")
for i, replica in enumerate(replicas, 1):
    print(f"{i}. {replica}")

# 2. Добавить новую реплику
replicas.append("Я нуждаюсь в большем времени на размышление")
print(f"\n2. Добавлена новая реплика: '{replicas[-1]}'")

# 3. Вывести каждую вторую реплику
print("\n3. Каждая вторая реплика:")
for i in range(1, len(replicas), 2):
    print(f"{i+1}. {replicas[i]}")

# 4. Найти самую короткую реплику
shortest_replica = min(replicas, key=len)
print(f"\n4. Самая короткая реплика: '{shortest_replica}'")

# 5. Посчитать сколько реплик начинается с буквы "Я"
count_ya = sum(1 for replica in replicas if replica.startswith("Я"))
print(f"\n5. Количество реплик, начинающихся с 'Я': {count_ya}")

# 6. Вывести на печать все реплики, в которых встречается слово "сказал"
print("\n6. Реплики со словом 'сказал':")
said_replicas = [replica for replica in replicas if "сказал" in replica.lower()]
for replica in said_replicas:
    print(f"- {replica}")

print("\n" + "="*50)
print("А теперь анализ эмоциональных состояний пациентов:")
print("="*50)

# Анализ эмоциональных состояний пациентов

# 1. Создать список эмоциональных состояний пациентов
emotional_states = [
    "чувствую тревогу и беспокойство",
    "ощущение полной апатии",
    "тревога не покидает меня уже неделю",
    "чувствую радость и удовлетворение",
    "постоянная тревога мешает сосредоточиться",
    "чувствую себя опустошенным",
    "легкая тревога по утрам"
]

print("1. Исходный список эмоциональных состояний:")
for i, state in enumerate(emotional_states, 1):
    print(f"{i}. {state}")

# 2. Добавить новое состояние
emotional_states.append("чувствую подавленность и тоску")
print(f"\n2. Добавлено новое состояние: '{emotional_states[-1]}'")

# 3. Вывести каждое третье состояние
print("\n3. Каждое третье состояние:")
for i in range(2, len(emotional_states), 3):
    print(f"{i+1}. {emotional_states[i]}")

# 4. Найти самое длинное описание состояния
longest_state = max(emotional_states, key=len)
print(f"\n4. Самое длинное описание состояния: '{longest_state}'")

# 5. Посчитать, сколько раз встречалось слово "тревога"
anxiety_count = sum(1 for state in emotional_states if "тревога" in state.lower())
print(f"\n5. Слово 'тревога' встречается: {anxiety_count} раз(а)")

# 6. Вывести все состояния начинающиеся со слова "чувствую"
print("\n6. Состояния, начинающиеся со слова 'чувствую':")
feeling_states = [state for state in emotional_states if state.startswith("чувствую")]
for state in feeling_states:
    print(f"- {state}")