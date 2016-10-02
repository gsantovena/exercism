package hello

const testVersion = 2

func HelloWorld(name string) string {
    if name != "" {
        return "Hello, " + name + "!"
    } else {
        return "Hello, World!"
    }
}
