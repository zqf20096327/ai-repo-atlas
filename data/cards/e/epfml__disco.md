# epfml/disco

⭐ 191 · TypeScript · Apache-2.0 · 推送 2026-10-21 · [GitHub](https://github.com/epfml/disco) · [官网](https://discolab.ai) · 组织维护

**浏览器端联邦/去中心化协作训练平台，无需代码与安装**

DISCO 是运行于浏览器的分布式协作机器学习平台，面向非技术用户：多个数据持有者在不共享原始数据的前提下共同训练深度学习模型。采用“公共模型-私有数据”模式，仅交换安全聚合后的模型更新，支持联邦式（中心服务器）与去中心化（用户间 P2P，无中心协调）两种训练方案。基于 TF.js 在浏览器内运行任意深度学习任务，提供 Titanic、MNIST、CIFAR-10、GPT2 等示例任务，并可在自定义训练页面上传初始模型、无代码创建训练任务。开发者以 JavaScript/TypeScript 参与开发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器内运行深度学习任务（基于 TF.js），无需安装
- 支持联邦式与去中心化（P2P、无中心协调）两种训练方案
- 仅交换模型更新而非数据，隐私保护设计
- 无代码创建自定义协作训练任务

## 适用场景

- 我想和他人一起在不共享私有数据的情况下联合训练模型
- 作为非技术用户在浏览器中参与机器学习训练
- 在移动设备上参与分布式学习实验

## 场景标签

 · 领域:分布式/联邦机器学习

## 证据(README 行号)

> L7: DISCO leverages federated :star2: and decentralized :sparkles: learning to allow several data owners to collaborativ
> L31: - DISCO runs arbitrary deep learning tasks and model architectures in your browser, via TF.js
> L55: - The example DISCOllaboratives are based on popular ML tasks such as GPT2, Titanic, MNIST or CIFAR-10

## 星数曲线

```mermaid
xychart-beta
    title "epfml/disco 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 190 --> 192
    line [191, 191]
```

2026-10-18 191 → 2026-10-22 191（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4b9a24cdaefc` · [字段定义](../../DATASET.md)*
