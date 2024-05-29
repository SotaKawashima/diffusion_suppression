import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def main():
    path1 = sys.argv[1]
    df = pd.read_csv(path1 + '/result.csv', index_col = 0)
    # print(df)

    path2 = sys.argv[2]
    only_F = pd.read_csv(path2 + '/result.csv', index_col = 0)
    # print(only_F)
    # print(only_F.describe())

    df = pd.concat([only_F, df], ignore_index=True)
    print(df)

    one_image(path1, df)
    # four_images(path1, df)

def one_image(path1, df):
    sns.set() 
    sns.set_style('whitegrid')
    fig = plt.figure(figsize = (20, 10))

    # top left
    ax1 = fig.add_subplot(2, 2, 1)
    df1 = df[(df['pop_F'] == 1) & (df['pop_T'] == 1)]
    sns.lineplot(data = df1, x = 'k_T', y = 'infl_sprd_F', label = 'False (high popularity)', marker = 'o', ms = 8, ax = ax1, ci = 95)
    sns.lineplot(data = df1, x = 'k_T', y = 'infl_sprd_T', label = 'True (high popularity)', marker = '^', ms = 8, ax = ax1, ci = 95)
    ax1.legend()
    ax1.set_xlabel('Seed set size')
    ax1.set_ylabel('Influence spread')
    ax1.set_xticks(range(int(df['k_T'].max()) + 1))
    ax1.set_ylim((0, 1))

    # top right
    ax2 = fig.add_subplot(2, 2, 2)
    df2 = df[(df['pop_F'] == 1) & (df['pop_T'] == 0)]
    sns.lineplot(data = df2, x = 'k_T', y = 'infl_sprd_F', label = 'False (high popularity)', marker = 'o', ms = 8, ax = ax2, ci = 95)
    sns.lineplot(data = df2, x = 'k_T', y = 'infl_sprd_T', label = 'True (low popularity)', marker = '^', ms = 8, ax = ax2, ci = 95)
    ax2.legend()
    ax2.set_xlabel('Seed set size')
    ax2.set_ylabel('Influence spread')
    ax2.set_xticks(range(int(df['k_T'].max()) + 1))
    ax2.set_ylim((0, 1))

    # bottom left
    ax3 = fig.add_subplot(2, 2, 3)
    df3 = df[(df['pop_F'] == 0) & (df['pop_T'] == 1)]
    sns.lineplot(data = df3, x = 'k_T', y = 'infl_sprd_F', label = 'False (low popularity)', marker = 'o', ms = 8, ax = ax3, ci = 95)
    sns.lineplot(data = df3, x = 'k_T', y = 'infl_sprd_T', label = 'True (high popularity)', marker = '^', ms = 8, ax = ax3, ci = 95)
    ax3.legend()
    ax3.set_xlabel('Seed set size')
    ax3.set_ylabel('Influence spread')
    ax3.set_xticks(range(int(df['k_T'].max()) + 1))
    ax3.set_ylim((0, 1))

    # bottom right
    ax4 = fig.add_subplot(2, 2, 4)
    df4 = df[(df['pop_F'] == 0) & (df['pop_T'] == 0)]
    sns.lineplot(data = df4, x = 'k_T', y = 'infl_sprd_F', label = 'False (low popularity)', marker = 'o', ms = 8, ax = ax4, ci = 95)
    sns.lineplot(data = df4, x = 'k_T', y = 'infl_sprd_T', label = 'True (low popularity)', marker = '^', ms = 8, ax = ax4, ci = 95)
    ax4.legend()
    ax4.set_xlabel('Seed set size')
    ax4.set_ylabel('Influence spread')
    ax4.set_xticks(range(int(df['k_T'].max()) + 1))
    ax4.set_ylim((0, 1))

    # show plots
    fig.tight_layout()
    plt.show()
    fig.savefig(path1 + '/image.png')

def four_images(path1, df):
    sns.set() 
    sns.set_style('whitegrid')
    fig = plt.figure()
    # top left
    ax1 = fig.add_subplot(111)
    df1 = df[(df['pop_F'] == 1) & (df['pop_T'] == 1)]
    sns.lineplot(data = df1, x = 'k_T', y = 'infl_sprd_F', label = 'False (high popularity)', marker = 'o', ms = 8, ax = ax1, ci = 95)
    sns.lineplot(data = df1, x = 'k_T', y = 'infl_sprd_T', label = 'True (high popularity)', marker = '^', ms = 8, ax = ax1, ci = 95)
    ax1.legend()
    ax1.set_xlabel('Seed set size')
    ax1.set_ylabel('Influence spread')
    ax1.set_xticks(range(int(df['k_T'].max()) + 1))
    ax1.set_ylim((0, 1))
    # show plots
    fig.tight_layout()
    plt.show()
    fig.savefig(path1 + '/image1.png')

    sns.set() 
    sns.set_style('whitegrid')
    fig = plt.figure()
    # top right
    ax2 = fig.add_subplot(111)
    df2 = df[(df['pop_F'] == 1) & (df['pop_T'] == 0)]
    sns.lineplot(data = df2, x = 'k_T', y = 'infl_sprd_F', label = 'False (high popularity)', marker = 'o', ms = 8, ax = ax2, ci = 95)
    sns.lineplot(data = df2, x = 'k_T', y = 'infl_sprd_T', label = 'True (low popularity)', marker = '^', ms = 8, ax = ax2, ci = 95)
    ax2.legend()
    ax2.set_xlabel('Seed set size')
    ax2.set_ylabel('Influence spread')
    ax2.set_xticks(range(int(df['k_T'].max()) + 1))
    ax2.set_ylim((0, 1))
    # show plots
    fig.tight_layout()
    plt.show()
    fig.savefig(path1 + '/image2.png')

    sns.set() 
    sns.set_style('whitegrid')
    fig = plt.figure()
    # bottom left
    ax3 = fig.add_subplot(111)
    df3 = df[(df['pop_F'] == 0) & (df['pop_T'] == 1)]
    sns.lineplot(data = df3, x = 'k_T', y = 'infl_sprd_F', label = 'False (low popularity)', marker = 'o', ms = 8, ax = ax3, ci = 95)
    sns.lineplot(data = df3, x = 'k_T', y = 'infl_sprd_T', label = 'True (high popularity)', marker = '^', ms = 8, ax = ax3, ci = 95)
    ax3.legend()
    ax3.set_xlabel('Seed set size')
    ax3.set_ylabel('Influence spread')
    ax3.set_xticks(range(int(df['k_T'].max()) + 1))
    ax3.set_ylim((0, 1))
    # show plots
    fig.tight_layout()
    plt.show()
    fig.savefig(path1 + '/image3.png')

    sns.set() 
    sns.set_style('whitegrid')
    fig = plt.figure()
    # bottom right
    ax4 = fig.add_subplot(111)
    df4 = df[(df['pop_F'] == 0) & (df['pop_T'] == 0)]
    sns.lineplot(data = df4, x = 'k_T', y = 'infl_sprd_F', label = 'False (low popularity)', marker = 'o', ms = 8, ax = ax4, ci = 95)
    sns.lineplot(data = df4, x = 'k_T', y = 'infl_sprd_T', label = 'True (low popularity)', marker = '^', ms = 8, ax = ax4, ci = 95)
    ax4.legend()
    ax4.set_xlabel('Seed set size')
    ax4.set_ylabel('Influence spread')
    ax4.set_xticks(range(int(df['k_T'].max()) + 1))
    ax4.set_ylim((0, 1))
    # show plots
    fig.tight_layout()
    plt.show()
    fig.savefig(path1 + '/image4.png')

if __name__ == '__main__':
    main()