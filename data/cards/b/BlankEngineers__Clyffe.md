# BlankEngineers/Clyffe

⭐ 5 · Python · NOASSERTION · 推送 2026-11-25 · [GitHub](https://github.com/BlankEngineers/Clyffe) · 组织维护

**从零训练的 LittleBit-2 二值化小型语言模型实验项目**

Blank Engineers 团队发布的实验性语言模型 Clyffe（ARC-LB-01）：不使用预训练权重、外部 AI API 或知识蒸馏，从随机初始化训练，采用 LittleBit-2 二值潜因子分解、Joint-ITQ、Dual-SVID 补偿与量化感知训练，覆盖 99.76% 参数的密集等效参数量约 24.1 万。提供 100% 离线推理，通过 CLI 脚本与本地 web dashboard 在 int32 打包二值因子上运行，支持 Dense 对照与三种二值检查点的并排对比审计。许可为 All Rights Reserved，仅允许公开查看与展示，禁止复制、修改与再分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从随机初始化训练，不含预训练权重与知识蒸馏
- 全模型二值化：99.76% 参数以 LittleBit-2 形式存储，.pt 文件 94,817 字节
- 100% 离线打包推理：CLI 与本地 web dashboard，CPU 平均延迟约 51.5 ms
- 多检查点对比：Dense Control 与三种 LittleBit-2 变体并排审计

## 适用场景

- 在本地离线环境运行一个极小规模语言模型的文本生成
- 研究原生二值化训练与传统训练后压缩的差异
- 对比不同量化路径（SmoothSign/STE）的检查点表现

## 场景标签

`模型训练` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L13: **Clyffe** is an independently initialized, independently trained experimental language model built from random ini
> L23: - **100% Offline Packed Inference:** Executes directly on `int32`-packed binary factors and FP16 scales via CLI (`r


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `a1d5e60f4245` · [字段定义](../../DATASET.md)*
