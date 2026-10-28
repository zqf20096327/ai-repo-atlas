# TianGzlab/OmicsClaw

⭐ 161 · Python · Apache-2.0 · 推送 2026-10-07 · [GitHub](https://github.com/TianGzlab/OmicsClaw) · [官网](https://TianGzlab.github.io/OmicsClaw/) · 组织维护 · 中文 README

**多组学研究的对话式 AI agent，88 个分析技能，CLI+桌面端**

面向多组学分析的本地优先 AI agent：用户用自然语言描述分析需求，agent 选择技能并按其指令在用户本地或服务器环境运行 Python、R 或命令行工具。内置覆盖空间转录组、单细胞、基因组学、蛋白质组学、代谢组学、bulk RNA-seq 与文献解析的 88 个技能。支持 13 家模型提供商（含 Ollama 本地端点），提供终端 CLI、桌面应用（各平台安装包）、远程 SSH 模式与 Telegram/飞书/Slack 等聊天平台接入；带执行审批机制与长期记忆存储。自述为研究工具，不提供临床诊断。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 88 个技能覆盖 7 个组学领域，技能为可独立运行的脚本
- 支持 13 家模型提供商，含 Ollama 与 OpenAI 兼容端点
- 桌面应用提供 macOS/Windows/Linux 安装包与远程 SSH 模式
- 执行审批机制、Docker 沙箱选项与对话/长期记忆存储

## 适用场景

- 用对话方式完成单细胞或空间转录组等组学分析
- 让 agent 在自己服务器上运行分析、数据不出服务器
- 通过 Telegram/飞书等聊天平台远程使用分析 agent
- 技能脚本脱离 agent 单独运行单次分析

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L21: OmicsClaw is an AI agent for multi-omics analysis. You describe the analysis
> L24: server. It ships 88 skills in seven domains, and the same agent answers in the
> L140: |Spatial transcriptomics|17|QC, domains, annotation, deconvolution, CNV, trajectory|spatial|

## 星数曲线

```mermaid
xychart-beta
    title "TianGzlab/OmicsClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 160 --> 162
    line [161, 161]
```

2026-10-18 161 → 2026-10-28 161（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `467d6b77ac3b` · [字段定义](../../DATASET.md)*
