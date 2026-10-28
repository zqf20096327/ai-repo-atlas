# m-zakeri/iust_deep_fuzz

⭐ 41 · Python · MIT · 推送 2026-07-31 · [GitHub](https://github.com/m-zakeri/iust_deep_fuzz) · [官网](https://m-zakeri.github.io/iust_deep_fuzz/) · 个人维护

**基于神经语言模型的文件格式模糊测试工具，生成测试数据**

IUST-DeepFuzz 是一个用深度神经语言模型（TensorFlow/Keras，含 RNN）学习文件格式并生成测试数据的模糊测试工具。提供四个深度模型与两个新算法（DataNeuralFuzz、MetadataNeuralFuzz），并实现论文 SampleFuzz 算法；附带 PDF 格式预训练模型与多种文件格式数据集。需 Python 3.6.x、TensorFlow、Keras，通过 git clone 获取源码，配置 config.py 后运行脚本。当前版本 0.3.0，最后更新 2022 年 9 月。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个深度模型与 DataNeuralFuzz/MetadataNeuralFuzz 两个新算法
- 提供 PDF 格式预训练模型（model_checkpoint/best_models）
- 内置多种文件格式学习数据集（dataset 目录）
- 实现 arXiv:1701.07232 的 SampleFuzz 算法

## 适用场景

- 对任意应用做文件格式模糊测试
- 用深度模型学习文件格式后自动生成测试数据
- 基于 PDF 预训练模型直接生成 fuzz 输入

## 场景标签

 · 领域:软件测试/安全

## 证据(README 行号)

> L12: In the current release (0.3.0), you can use IUST-DeepFuzz for test data generation and then fuzz every application.
> L32: ISUT-DeepFuzz has implemented four new deep models and two new fuzz algorithms: DataNeuralFuzz and MetadataNeuralFu

## 星数曲线

```mermaid
xychart-beta
    title "m-zakeri/iust_deep_fuzz 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-28 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `adf991f7be6b` · [字段定义](../../DATASET.md)*
