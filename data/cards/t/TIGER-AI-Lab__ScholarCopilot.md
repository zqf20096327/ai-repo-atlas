# TIGER-AI-Lab/ScholarCopilot

⭐ 253 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/TIGER-AI-Lab/ScholarCopilot) · [官网](https://arxiv.org/abs/2504.00824) · 组织维护

**面向学术写作的 AI 助手：文本补全与引文推荐（COLM 2025）**

TIGER-Lab 开发的学术写作助手，基于统一模型架构将检索与生成结合：模型在写作过程中学习发出 [RET] 标记，暂停生成并用引文 token 的隐藏状态从语料库检索相关论文，插入引文后继续生成。功能包括下三句建议、整段自动补全、实时引文推荐、一键插入与 BibTeX 生成。提供自建 demo 的部署流程（克隆仓库、pip 安装、下载模型数据、启动脚本），也支持用 arXiv 元数据更新语料库并重建 HNSW 索引；训练复现需 32 张 GPU。论文被 COLM 2025 接收。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一架构联合优化学术文本生成与引文检索（[RET] 标记动态切换）
- 下三句建议与整段学术结构补全
- 实时引文推荐、一键插入与 BibTeX 自动生成
- 支持自建语料库：arXiv 元数据处理 + HNSW 索引构建

## 适用场景

- 写论文时获得上下文相关的句子与段落补全
- 写作过程中获取并插入真实文献引文
- 在自有服务器上部署学术写作 demo 并更新引文语料库

## 场景标签

`AI 写作` `RAG` `科研工具` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Scholar Copilot is an intelligent academic writing assistant that enhances the research writing process through AI-p
> L21: Scholar Copilot employs a unified model architecture that seamlessly integrates retrieval and generation through a 

## 星数曲线

```mermaid
xychart-beta
    title "TIGER-AI-Lab/ScholarCopilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 252 --> 254
    line [253, 253]
```

2026-10-18 253 → 2026-10-29 253（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `bcf6d4ab1353` · [字段定义](../../DATASET.md)*
