import feedparser
import pygame
from bs4 import BeautifulSoup
from MySummarizeAssistant import MySummarizeAssistant

pygame.mixer.init()
print("Fetching blog posts...")
blog_feed = feedparser.parse("https://blog.jetbrains.com/feed/")
print(f"Posts: {len(blog_feed.entries)}\n")

print("Which post do you want to summarize?")
for i, entry in enumerate(blog_feed.entries):
    print(f"{i+1}. {entry.title}")
entry_num = input("Please enter a number: ")
selected_title = blog_feed.entries[int(entry_num)-1].title

assistant = MySummarizeAssistant()
soup = BeautifulSoup(blog_feed.entries[int(entry_num)-1].summary, "html.parser")
pure_text = soup.get_text()
summary = assistant.ask_assistant(pure_text)
print("\nPleas wait a moment while we summarize the article for you...\n")
print(f"Summary for <{selected_title}>:\n {summary}")

read_summary = input("Do you want to read the summary? (y/n): ")
if read_summary.lower() == "y":
    audio = assistant.text_to_speech(summary)
    audio_path = f"tts_cache/{selected_title}.mp3"
    audio.stream_to_file(audio_path)
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

2