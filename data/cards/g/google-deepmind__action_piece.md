# google-deepmind/action_piece

⭐ 71 · Python · Apache-2.0 · 推送 2026-07-02 · [GitHub](https://github.com/google-deepmind/action_piece) · 组织维护

**生成式推荐的动作序列上下文化分词方法官方实现**

Google DeepMind 发布的 ICML 2025 Spotlight 论文 ActionPiece 的官方代码。方法将每个动作表示为物品特征集合，在动作序列语料上通过合并频繁共现的特征模式（集合内与相邻集合间）构建词表，把上下文显式纳入动作序列分词，用于生成式推荐（GR）模型。提供 main.py 训练/复现脚本，指定 category 参数后自动下载 Amazon Reviews 2014 数据集，首次运行自动构建并缓存分词器词表；代码含集合置换正则化（SPR）的训练与推理路径。运行命令使用 CUDA_VISIBLE_DEVICES 指定 GPU。

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

- 合并频繁共现特征模式构建上下文化动作词表
- 支持 Sports/Beauty/CDs 等 Amazon Reviews 2014 类目复现
- 首次运行自动构建并缓存 tokenizer 词表
- 含 SPR（集合置换正则化）训练与推理实现

## 适用场景

- 复现论文中生成式推荐的实验结果
- 研究生成式推荐中动作序列分词方法
- 在 Amazon Reviews 数据集上训练推荐模型

## 场景标签

`推荐系统` · 领域:学习与行业

## 证据(README 行号)

> L3: This repository provides the code for implementing ActionPiece described in our
> L6: Unlike existing generative recommendation (GR) models that tokenize each action
> L17: CUDA_VISIBLE_DEVICES=0 python main.py \

## 星数曲线

```mermaid
xychart-beta
    title "google-deepmind/action_piece 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-24 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `8bede870ed5c` · [字段定义](../../DATASET.md)*
