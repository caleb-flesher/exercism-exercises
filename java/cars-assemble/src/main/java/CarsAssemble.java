public class CarsAssemble {
    static int CAR_ASSEMBLED = 221;

    public double productionRatePerHour(int speed) {
        if (speed > 0  && speed <= 4) { return speed * CAR_ASSEMBLED; }
        if (speed >= 5  && speed <= 8) { return (speed * CAR_ASSEMBLED) * .9; }
        if (speed == 9) { return (speed * CAR_ASSEMBLED) * .8; }
        if (speed == 10) { return (speed * CAR_ASSEMBLED) * .77; }
        else { return 0; }
        
    }

    public int workingItemsPerMinute(int speed) {
        return (int) productionRatePerHour(speed) / 60;
    }
}
