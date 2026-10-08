total_seconds = int(input("Seconds: "))
hours, remainder = divmod(total_seconds, 3600)
minutes, seconds = divmod(remainder, 60)
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
