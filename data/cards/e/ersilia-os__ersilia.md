# ersilia-os/ersilia

⭐ 316 · Python · GPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/ersilia-os/ersilia) · [官网](https://ersilia.io) · 组织维护

**面向传染病药物发现研究的预训练 AI/ML 模型仓库与 CLI**

Ersilia Model Hub 提供统一平台与命令行工具，收录文献发表模型与自研模型，覆盖抗菌活性预测、ADMET、分子表示与生成化学等场景。每个模型独立打包为 Conda 环境或 Docker 容器，用户通过 fetch/serve/run/close 命令或等价 Python API 运行模型，以 CSV 为输入输出。支持按 eos 模板提交新模型。由非营利组织 Ersilia Open Source Initiative 维护，服务于全球南方实验室、高校与诊所，GPL-3 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文献模型与自研模型统一收录，每模型独立 Conda/Docker 打包
- CLI 完整生命周期命令：catalog/fetch/serve/run/close/delete
- 同一功能提供 Python API，校验与会话规则与 CLI 一致
- 按 eos-template 流程提交新模型

## 适用场景

- 用一行命令获取并运行抗菌活性或 ADMET 预测模型
- 批量处理 CSV 分子数据并输出预测结果
- 向平台提交自研传染病相关模型供他人复用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L15: The Ersilia Model Hub is a unified platform of pre-trained AI/ML models for 🦠 infectious and neglected disease rese
> L61: To **install each model**, you have two options. You can either package them from source, in which case only Conda 

## 星数曲线

```mermaid
xychart-beta
    title "ersilia-os/ersilia 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 310 --> 312
    line [311, 311]
```

2026-10-18 311 → 2026-10-28 311（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `b50da503eb47` · [字段定义](../../DATASET.md)*
