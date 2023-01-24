
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    backLegSensorValues = np.load('data/backLegSensorValues.npy')
    frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
    targetValues = np.load('data/targetAngles.npy')

    plt.plot(targetValues)
    plt.show()
    exit()

    plt.plot(backLegSensorValues, label='back leg', linewidth=2)
    plt.plot(frontLegSensorValues, label='front leg', linewidth=1)
    plt.legend()

    plt.savefig('submission_materials/taskF.png')
    plt.show()