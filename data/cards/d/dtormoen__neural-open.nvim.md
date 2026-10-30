# dtormoen/neural-open.nvim

⭐ 69 · Lua · MIT · 推送 2026-06-24 · [GitHub](https://github.com/dtormoen/neural-open.nvim) · 个人维护

**为开发者学习文件选择偏好的 Neovim 神经网络文件选择器**

基于 Snacks.nvim 的 Neovim 文件选择器插件：对每个候选文件计算 11 个归一化特征（模糊匹配、缓冲区状态、目录邻近度、frecency、文件转移模式等），默认用多层感知机（pairwise hinge loss 在线训练）输出排序分，也提供经典加权和与朴素求和两种算法。内置 1.6 万+样本预训练权重，学习结果持久化到磁盘并可随时重置；支持为任意字符串选择场景创建自定义 picker，各 picker 独立训练。要求 Neovim >= 0.11.0 且已安装 Snacks.nvim，经 lazy.nvim 安装。

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

- MLP 在线学习用户选择偏好并跨会话持久化权重
- 11 个归一化打分特征（模糊匹配/frecency/目录邻近度/转移模式等）
- 随附 16k+ 样本预训练默认权重，首次启动即可用
- 三种排序算法可运行时切换（nn/classic/naive）

## 适用场景

- 在大型项目中更快跳转到我常打开的文件
- 为任意字符串选择场景（make targets、vim 命令等）训练专用排序 picker
- 观察模型打分明细与训练过程（debug 预览）

## 场景标签

 · 领域:开发者工具/编辑器插件

## 证据(README 行号)

> L3: A Neovim file picker that learns how you navigate. A neural network trains on your file selections to rank results b
> L9: - **Neural Network Ranking**: An MLP trains online from your selections using pairwise hinge loss, learning to rank 
> L127: A multi-layer perceptron that takes the 11 normalized features as input and outputs a ranking score. Trained onlin

## 星数曲线

```mermaid
xychart-beta
    title "dtormoen/neural-open.nvim 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-30"]
    y-axis "stars" 68 --> 71
    line [70, 69, 69]
```

2026-10-18 70 → 2026-10-30 69（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `277f938e3fc2` · [字段定义](../../DATASET.md)*
