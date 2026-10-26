# sainathadapa/spotify-sequential-skip-prediction

⭐ 27 · Jupyter Notebook · Apache-2.0 · 推送 2026-09-04 · [GitHub](https://github.com/sainathadapa/spotify-sequential-skip-prediction) · [官网](https://arxiv.org/abs/1904.10273) · 个人维护

**Spotify 序列跳过预测竞赛第 7 名解决方案（Keras/RNN）**

WSDM Cup 2019 Spotify 顺序跳过预测挑战赛的第 7 名参赛方案代码库。方案使用循环神经网络对用户听歌会话进行序列建模，预测用户是否会跳过某曲目。README 提供复现流程：从 CrowdAI 下载数据集，可选用 notebook 生成样本数据，用脚本分别训练各会话长度模型、在验证集评估、处理测试数据并生成提交文件。附 arXiv 论文引用（arXiv:1904.10273），代码以 Apache 2.0 许可共享。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于 RNN 的会话序列建模与跳过预测
- 按会话长度分别训练模型的脚本流程
- 提供从数据下载到提交文件生成的完整复现步骤
- 附 arXiv 论文（arXiv:1904.10273）

## 适用场景

- 复现竞赛方案或学习序列跳过预测建模
- 音乐推荐/用户行为预测研究参考
- 作为 WSDM Cup 2019 参赛方案的对照实现

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L1: # WSDM Cup 2019 - Spotify - Sequential Skip Prediction Challenge - 7th place solution
> L23:   title={Sequential modeling of Sessions using Recurrent Neural Networks for Skip Prediction},
> L14: 3. Train the models using the 05-train-each-len.py script.

## 星数曲线

```mermaid
xychart-beta
    title "sainathadapa/spotify-sequential-skip-prediction 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `37c5ae006b97` · [字段定义](../../DATASET.md)*
