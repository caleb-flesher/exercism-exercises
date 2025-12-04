import static java.lang.String.format;

class Badge {
    public String print(Integer id, String name, String department) {
        return format("%s%s - %s",
                (id != null) ? format("[%s] - ", id) : "",
                name,
                (department == null) ? "OWNER" : department.toUpperCase());
    }
}
