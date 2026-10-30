# dwave-examples/image-generation

⭐ 27 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/dwave-examples/image-generation) · 组织维护

**量子-经典混合示例：用 DVAE+GRBM 在 MNIST 上生成手写数字图像**

D-Wave 官方示例仓库，演示混合量子-经典机器学习架构：经典 PyTorch 编码器将 MNIST 手写数字压缩到二进制自旋潜在空间，Graph-Restricted Boltzmann Machine（GRBM）让 QPU 学习该空间上的耦合与偏置并建模数据分布；训练损失由重构 MSE、分布距离 MMD 与针对 QPU 参数的负对数似然三项组成；新图像通过从训练后的 QPU 采样自旋串并经解码器生成。提供 Dash 网页界面（python app.py），需配置 Leap 量子云服务访问，支持 GitHub Codespaces 或 pip install -r requirements.txt 运行。面向量子和机器学习开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 经典编码器/解码器 + QPU 学习 Boltzmann 分布的二进制潜在空间
- 损失函数含重构 MSE、MMD 分布距离与 QPU 负对数似然三项
- Dash 网页界面可配置问题并提交求解器
- 支持 devcontainer（GitHub Codespaces）免安装运行

## 适用场景

- 学习混合量子-经典生成式模型的实现方式
- 在 MNIST 数据集上训练并生成 28x28 手写数字图像
- 了解 D-Wave QPU 与 PyTorch 的结合用法

## 场景标签

`图像生成` `教程课程` · 领域:内容生成

## 证据(README 行号)

> L3: This example showcases the use of hybrid quantum-classical machine learning architectures in the
> L14: of spin strings arising from encoding the input data into the binary latent space. New data is then
> L88: A discrete variational autoencoder is trained on these images in order to create a generative model,

## 星数曲线

```mermaid
xychart-beta
    title "dwave-examples/image-generation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `089ae7fa9c1f` · [字段定义](../../DATASET.md)*
