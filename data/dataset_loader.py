"""
数据集加载和预处理工具模块
提供统一的数据集接口，支持多种真实数据集
"""

import os
from typing import Dict, List, Tuple, Optional
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml, load_breast_cancer, load_wine
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split


class DatasetLoader:
    """数据集加载器"""

    def __init__(self, data_dir: str = None):
        """
        初始化数据集加载器

        Args:
            data_dir: 数据集存储目录，默认为项目 data 目录
        """
        if data_dir is None:
            # 获取项目根目录的 data 文件夹
            self.data_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
        else:
            self.data_dir = data_dir
        self.datasets = {}

    def load_iris(self) -> Tuple[pd.DataFrame, pd.Series]:
        """
        加载鸢尾花数据集

        Returns:
            X: 特征数据
            y: 标签数据
        """
        from sklearn.datasets import load_iris
        iris = load_iris()
        X = pd.DataFrame(iris.data, columns=iris.feature_names)
        y = pd.Series(iris.target, name='species')
        return X, y

    def load_boston(self) -> Tuple[pd.DataFrame, pd.Series]:
        """
        加载 Boston 房价数据集

        Returns:
            X: 特征数据
            y: 房价数据
        """
        # Boston 数据集在 sklearn 1.2+ 版本中被移除，使用 fetch_openml 加载
        boston = fetch_openml(name='boston', version=1, as_frame=True, parser='auto')
        X = boston.data
        y = boston.target.astype(float)
        return X, y

    def load_wine(self) -> Tuple[pd.DataFrame, pd.Series]:
        """
        加载 Wine 数据集

        Returns:
            X: 特征数据
            y: 标签数据
        """
        wine = load_wine(as_frame=True)
        X = wine.data
        y = wine.target.astype(int)
        return X, y

    def load_breast_cancer(self) -> Tuple[pd.DataFrame, pd.Series]:
        """
        加载 Breast Cancer 数据集

        Returns:
            X: 特征数据
            y: 标签数据（0: 恶性，1: 良性）
        """
        cancer = load_breast_cancer(as_frame=True)
        X = cancer.data
        y = cancer.target.astype(int)
        return X, y

    def get_dataset_info(self, dataset_name: str) -> Dict:
        """
        获取数据集信息

        Args:
            dataset_name: 数据集名称

        Returns:
            数据集信息字典
        """
        info_map = {
            'iris': {
                'name': '鸢尾花数据集',
                'task': '分类',
                'n_samples': 150,
                'n_features': 4,
                'n_classes': 3,
                'features': ['sepal_length', 'sepal_width', 'petal_length', 'petal_width'],
                'target': 'species',
                'description': '经典的鸢尾花数据集，用于分类任务练习'
            },
            'boston': {
                'name': 'Boston 房价数据集',
                'task': '回归',
                'n_samples': 506,
                'n_features': 13,
                'features': ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
                            'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'],
                'target': 'MEDV',
                'description': 'Boston 地区房价数据集，用于回归任务练习'
            },
            'wine': {
                'name': 'Wine 数据集',
                'task': '分类',
                'n_samples': 178,
                'n_features': 13,
                'n_classes': 3,
                'features': ['alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash',
                            'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols',
                            'proanthocyanins', 'color_intensity', 'hue', 'od280/od315_of_diluted_wines', 'proline'],
                'target': 'class',
                'description': '葡萄酒数据集，用于分类任务练习'
            },
            'breast_cancer': {
                'name': 'Breast Cancer 数据集',
                'task': '分类',
                'n_samples': 569,
                'n_features': 30,
                'n_classes': 2,
                'features': [f'feature_{i}' for i in range(30)],
                'target': 'target',
                'description': '乳腺癌诊断数据集，用于分类任务练习'
            }
        }

        return info_map.get(dataset_name.lower(), {})

    def list_datasets(self) -> List[Dict]:
        """
        列出所有可用的数据集

        Returns:
            数据集列表
        """
        return [
            self.get_dataset_info('iris'),
            self.get_dataset_info('boston'),
            self.get_dataset_info('wine'),
            self.get_dataset_info('breast_cancer')
        ]


class DatasetPreprocessor:
    """数据集预处理器"""

    def __init__(self):
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()

    def train_test_split(
        self,
        X: pd.DataFrame,
        y: pd.Series,
        test_size: float = 0.2,
        random_state: int = 42
    ) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """
        划分训练集和测试集

        Args:
            X: 特征数据
            y: 标签数据
            test_size: 测试集比例
            random_state: 随机种子

        Returns:
            X_train, X_test, y_train, y_test
        """
        return train_test_split(X, y, test_size=test_size, random_state=random_state)

    def standardize(
        self,
        X_train: pd.DataFrame,
        X_test: pd.DataFrame = None
    ) -> Tuple[np.ndarray, Optional[np.ndarray]]:
        """
        标准化特征数据

        Args:
            X_train: 训练集特征
            X_test: 测试集特征（可选）

        Returns:
            标准化后的训练集和测试集
        """
        X_train_scaled = self.scaler.fit_transform(X_train)
        if X_test is not None:
            X_test_scaled = self.scaler.transform(X_test)
            return X_train_scaled, X_test_scaled
        return X_train_scaled, None

    def encode_labels(
        self,
        y_train: pd.Series,
        y_test: pd.Series = None
    ) -> Tuple[np.ndarray, Optional[np.ndarray]]:
        """
        编码标签

        Args:
            y_train: 训练集标签
            y_test: 测试集标签（可选）

        Returns:
            编码后的训练集和测试集标签
        """
        y_train_encoded = self.label_encoder.fit_transform(y_train)
        if y_test is not None:
            y_test_encoded = self.label_encoder.transform(y_test)
            return y_train_encoded, y_test_encoded
        return y_train_encoded, None


def load_dataset(dataset_name: str, data_dir: str = None) -> Tuple[pd.DataFrame, pd.Series]:
    """
    加载指定数据集（便捷函数）

    Args:
        dataset_name: 数据集名称（iris, boston, wine, breast_cancer）
        data_dir: 数据集存储目录

    Returns:
        X, y: 特征数据和标签数据
    """
    loader = DatasetLoader(data_dir)

    dataset_map = {
        'iris': loader.load_iris,
        'boston': loader.load_boston,
        'wine': loader.load_wine,
        'breast_cancer': loader.load_breast_cancer
    }

    loader_func = dataset_map.get(dataset_name.lower())
    if loader_func is None:
        raise ValueError(f"未知的数据集: {dataset_name}. 可用的数据集: {list(dataset_map.keys())}")

    return loader_func()


def get_prepared_data(
    dataset_name: str,
    test_size: float = 0.2,
    random_state: int = 42,
    standardize: bool = True,
    encode_labels: bool = True
) -> Dict:
    """
    获取预处理后的完整数据集

    Args:
        dataset_name: 数据集名称
        test_size: 测试集比例
        random_state: 随机种子
        standardize: 是否标准化特征
        encode_labels: 是否编码标签

    Returns:
        包含训练集和测试集的字典
    """
    X, y = load_dataset(dataset_name)

    preprocessor = DatasetPreprocessor()
    X_train, X_test, y_train, y_test = preprocessor.train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    result = {
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test
    }

    if standardize:
        X_train_scaled, X_test_scaled = preprocessor.standardize(X_train, X_test)
        result['X_train_scaled'] = X_train_scaled
        result['X_test_scaled'] = X_test_scaled

    if encode_labels:
        y_train_encoded, y_test_encoded = preprocessor.encode_labels(y_train, y_test)
        result['y_train_encoded'] = y_train_encoded
        result['y_test_encoded'] = y_test_encoded

    result['info'] = DatasetLoader().get_dataset_info(dataset_name)

    return result


if __name__ == '__main__':
    # 示例用法
    print("可用数据集:")
    loader = DatasetLoader()
    for dataset in loader.list_datasets():
        print(f"  - {dataset['name']}: {dataset['task']}任务, {dataset['n_samples']}样本")

    print("\n加载数据集示例:")
    X_iris, y_iris = load_dataset('iris')
    print(f"\nIris 数据集:")
    print(f"  特征形状: {X_iris.shape}")
    print(f"  标签形状: {y_iris.shape}")
    print(f"  特征名称: {list(X_iris.columns)}")
    print(f"  标签分布:\n{y_iris.value_counts()}")

    X_boston, y_boston = load_dataset('boston')
    print(f"\nBoston 数据集:")
    print(f"  特征形状: {X_boston.shape}")
    print(f"  标签形状: {y_boston.shape}")
    print(f"  房价范围: {y_boston.min():.2f} - {y_boston.max():.2f}")

    X_wine, y_wine = load_dataset('wine')
    print(f"\nWine 数据集:")
    print(f"  特征形状: {X_wine.shape}")
    print(f"  标签形状: {y_wine.shape}")
    print(f"  类别数量: {y_wine.nunique()}")

    X_cancer, y_cancer = load_dataset('breast_cancer')
    print(f"\nBreast Cancer 数据集:")
    print(f"  特征形状: {X_cancer.shape}")
    print(f"  标签形状: {y_cancer.shape}")
    print(f"  类别数量: {y_cancer.nunique()}")