文件夹中包含1、.ipynb文件2、inputfile文件夹3、outfile文件夹
通过pd.read_csv读取inputfile中的数据集
数据集64wan.csv包含“id”“date”“energy_use”三列属性
经过数据预处理、清洗数据集（删除空值）、增加两列提高聚类维度。
数据处理过后进行聚类分析，得到id所属类别，保存csv文件到outfile文件夹
plot_energy_fingerprints()函数得出4个类别的用电行为，分别为：

第一类用户：用电量始终较低，未出现过较大波动；

第三、四类用户：用电量特征类似，表现为晚间用电量显著提高；

第二类用户：用电量自早晨5点开始即明显提升，可能是某些产品生产者。