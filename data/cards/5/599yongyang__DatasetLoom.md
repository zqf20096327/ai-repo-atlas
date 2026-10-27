# 599yongyang/DatasetLoom

⭐ 300 · TypeScript · MIT · 推送 2025-12-13 · [GitHub](https://github.com/599yongyang/DatasetLoom) · 个人维护 · 中文 README

**面向多模态大模型训练的数据集构建与评估平台**

基于 Next.js + NestJS + Turborepo 的 Monorepo Web 平台，面向 AI 工程师与研究人员，提供从文档解析、智能分块、图像标注到 RAG 增强对话生成、AI 自动评分、SFT/DPO 语料导出的数据流水线。支持 Qdrant 向量数据库、多模型接入（GPT-4V、LLaVA、Qwen-VL 等）与多人协作权限管理，可导出 JSON/CSV/HuggingFace Dataset 格式。通过 git clone + pnpm 本地运行，或 Docker Compose 一键部署（含 web/api/PostgreSQL/Qdrant 四个服务）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SFT/DPO 训练数据集生成与模型输出自动评分对比
- RAG 增强对话生成（Qdrant 向量检索 + 可配置 Embedding 模型）
- 图像标注、图文问答与图像描述生成
- JSON/CSV/HuggingFace Dataset 格式训练语料导出

## 适用场景

- 为多模态大模型微调构建 SFT/DPO 训练数据集
- 基于论文、教材等真实文档生成可追溯的问答语料
- 对比 GPT-4V、LLaVA、Qwen-VL 等模型的输出质量
- 团队协作进行文档标注与训练数据整理

## 场景标签

`文档解析` `RAG` · 领域:知识与检索

## 证据(README 行号)

> L26: - 监督微调（SFT）语料生成
> L27: - 偏好对齐（DPO）数据集构建
> L43: |**DPO/SFT 数据集构建**|可配置策略生成偏好对或指令微调语料|
> L44: |**RAG 增强对话生成**|结合向量数据库，**驱动模型**基于真实文档生成专业对话数据|

## 星数曲线

```mermaid
xychart-beta
    title "599yongyang/DatasetLoom 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 299 --> 301
    line [300, 300]
```

2026-10-18 300 → 2026-10-27 300（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `b8e318886879` · [字段定义](../../DATASET.md)*
