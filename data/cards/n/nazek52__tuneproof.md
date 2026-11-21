# nazek52/tuneproof

⭐ 3 · Python · MIT · 推送 2026-11-16 · [GitHub](https://github.com/nazek52/tuneproof) · 个人维护

**可复现的 LoRA 微调实验教程：CPU 可跑、带负对照与数据审计**

一个独立教育性项目：用字节级因果 transformer 执行 LoRA 微调实验，含防泄漏的数据切分（精确提示与词法近重复先归入连通分量再划分）、held-out 评估（字节级 NLL 与贪婪精确匹配），以及 LR=0 的匹配负对照来验证 LoRA 权重变化确由训练产生。输出 HTML 报告、检查点、JSON 证据与 SHA-256 manifest，输出目录已存在则拒绝写入。使用小型合成任务，非预训练 LLM 基准；数据集限 10 MiB / 2000 行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPU 即可完整运行 LoRA 微调实验
- 防泄漏数据切分与数据集审计 CLI（audit/prepare/verify）
- LR=0 匹配负对照 + SHA-256 完整性 manifest 的证据链
- 支持 Alpaca 与单轮 ChatML 格式

## 适用场景

- 学习 LoRA 微调的完整可复现流程
- 构建微调数据集前做泄漏与冲突检查
- 参考带负对照与证据留存的实验设计

## 场景标签

`微调` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L5: A reproducible LoRA experiment with a byte-level causal transformer, leakage-aware dataset preparation, held-out eva
> L94: Independent educational implementation developed with AI assistance. Source code,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `92c830132bff` · [字段定义](../../DATASET.md)*
