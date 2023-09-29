#change file extension

import os

def change_file_extension(folder, old_ext, new_ext):
    for filename in os.listdir(folder):
        # Prüft, ob die Datei die alte Endung hat
        if not filename.endswith(old_ext):
            continue
        
        # Baut den neuen Dateinamen und den Pfad zur Datei
        new_name = filename[:-len(old_ext)] + new_ext
        file_path = os.path.join(folder, filename)
        
        # Ändert den Dateinamen
        os.rename(file_path, os.path.join(folder, new_name))

# Beispielaufruf: Ändere alle Dateien im Ordner "src" mit der Endung .cpp in .txt um
#change_file_extension("src", ".cpp", ".txt")

     #change_file_extension(R"C:\Users\jessy\OneDrive\Dokumente\Studium\Semester_1\INF\Lösungen_txt", ".cpp", ".txt")

     #print ("file extensions were changed")

user_input_path = input("Please enter the path to your folder in which changes shall happen:")
user_input_original_extension = input("Please enter the original extension.")
user_input_desired_extension = input("Please enter the desired extension:")

change_file_extension(R, user_input_path, user_input_original_extension, user_input_desired_extension)
print("file extension were changed")