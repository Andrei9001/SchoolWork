import pandas as pd
import matplotlib.pyplot as plt


# a punkts; CSV fails atrodas darbavirsmas sākuma mapītē
df = pd.read_csv('0254_data.csv')


# b punkts
plt.plot(df['altitude'])
plt.show()
