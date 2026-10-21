from rich import print 

def main():
  project_name = "Dockeraise python script"

  print(f"[bold green]success![/bold green] {project_name} is running inside docker")
  print("The same code can now run on any system with docker")

if __name__ == "__main__":
  main()