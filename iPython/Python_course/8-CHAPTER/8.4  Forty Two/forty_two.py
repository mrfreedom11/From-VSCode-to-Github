# Write code below 💖
# import #wikipedia

# query = "Philosophy of life"

# try:
#     result = wikipedia.summary(query, sentences=3)
#     print(f"🔍 {query} haqida qisqacha ma'lumot:\n")
#     print(result)
# except wikipedia.DisambiguationError as e:
#     print(f"❗ '{query}' uchun bir nechta natijalar topildi:")
#     print(e.options[:5])  # faqat 5 tasini ko‘rsatamiz
# except wikipedia.PageError:
#     print(f"❌ '{query}' haqida sahifa topilmadi.")
