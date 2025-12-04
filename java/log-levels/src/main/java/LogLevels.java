public class LogLevels {
    
    public static String message(String logLine) {
        String separator = ": ";
        logLine.indexOf(separator);
        return logLine.substring(logLine.indexOf(separator) + 2).trim();
    }

    public static String logLevel(String logLine) {
        char separatorStart = '[';
        char separatorEnd = ']';
        logLine.indexOf(separatorStart);
        logLine.indexOf(separatorEnd);
        return logLine.substring(
                logLine.indexOf(separatorStart) + 1, 
                logLine.indexOf(separatorEnd))
            .trim()
            .toLowerCase();
    }

    public static String reformat(String logLine) {
        return message(logLine) + " (" + logLevel(logLine) + ")";
    }
}
