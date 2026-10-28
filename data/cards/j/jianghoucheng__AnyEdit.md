# jianghoucheng/AnyEdit

⭐ 49 · Python · MIT · 推送 2025-11-06 · [GitHub](https://github.com/jianghoucheng/AnyEdit) · 个人维护

**面向研究者：编辑 LLM 中任意长度/格式知识的即插即用框架**

AnyEdit 是 ICML 2025 论文的官方代码库，提出自回归知识编辑范式：将长文本知识分解为顺序 chunk，逐 chunk 迭代编辑关键 token，并以互信息链式法则作理论支撑。作为即插即用框架，它可使现有编辑方法（如 MEMIT）处理任意长度与格式的知识。运行需一块 A100 80G GPU，固定版本依赖 pytorch/transformers 等，需手动下载 UnKE 与 AKEW 数据集到 data/ 目录，通过 python 命令执行编辑与结果汇总实验。面向模型编辑方向的研究与复现者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自回归编辑范式：长文本知识分 chunk 后逐个迭代编辑关键 token
- 即插即用：可让现有编辑方法（如 MEMIT_ARE）处理任意长度/格式知识
- 在 UnKEBench、AKEW 及其新提出的 EditEverything 数据集上评估

## 适用场景

- 复现 ICML 2025 AnyEdit 论文的编辑实验
- 对 Llama3-8B-Instruct 等模型执行长文本知识编辑评测
- 将现有模型编辑方法扩展到任意长度/格式的知识更新场景

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L4: - In this work, we propose **AnyEdit**, a new autoregressive editing paradigm. It decomposes long-form knowledge int
> L38: ### An example for editing Llama3-8B-Instruct on UnKEBench dataset using AnyEdit

## 星数曲线

```mermaid
xychart-beta
    title "jianghoucheng/AnyEdit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-28 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `44802c259f8e` · [字段定义](../../DATASET.md)*
