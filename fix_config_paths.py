import os

root_dir = r"d:\Vibe_Coding\plan_writing\.agent\skills"
target_string = '"../../config.yaml"'
replacement_string = '"../../../../config.yaml"'

count = 0
for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(subdir, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if target_string in content:
                new_content = content.replace(target_string, replacement_string)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filepath}")
                count += 1
print(f"Total updated: {count}")
