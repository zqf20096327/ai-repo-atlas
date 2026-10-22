# CamusGIT/EvoQuant

⭐ 141 · Python · Apache-2.0 · 推送 2026-09-02 · [GitHub](https://github.com/CamusGIT/EvoQuant) · 组织维护 · 中文 README

**量化投研自主 AI 研究代理：从研报到因子实验全流程**

面向量化投资研究的自演化多智能体（6 个子代理），构建于 DeepAgents/LangGraph 之上。将本地研报 PDF 提取为结构化知识库，基于文献锚点生成研究创意并用 ELO 锦标赛排序，随后在离线行情数据上复现方法为可执行 Research Artifact，以 IC/ICIR/RANKIC/coverage 指标评估。支持多 LLM 提供商切换、CLI/TUI/WebUI 及 Telegram/Slack/飞书/微信/Discord 多通道、定时任务与 MCP 技能扩展。需 Python 3.11+，支持 uv 安装与 Docker 运行。回测到实盘桥接等能力在 Roadmap 中尚未完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 研报 PDF → 结构化知识库（含出处引用、禁止编造规则）
- 锚点式创意生成（继承≥70%方法+≤30%创新）与 ELO 锦标赛排序
- 自包含实验运行时：离线数据发现、面板构建、IC/ICIR/RANKIC 评估
- 多提供商（Anthropic/OpenAI/Google/MiniMax/NVIDIA）与多通道会话

## 适用场景

- 把券商研报沉淀为可检索的私有量化知识库
- 无参考代码时从研报复现因子并在真实离线数据上验证
- 自动生成、排序并执行 alpha 因子研究创意

## 场景标签

`金融量化` `科研工具` `文档解析` · 领域:知识与检索

## 证据(README 行号)

> L5: EvoQuant is a self-evolving AI research agent specialized in **quantitative investment research**. It runs the full 
> L7: Where general-purpose "AI scientist" frameworks target broad academic discovery, EvoQuant is **purpose-built for the
> L21: - **🤖 Multi-Agent Team** — 6 sub-agents (plan, research, code, debug, analyze, write) working in concert.

## 星数曲线

```mermaid
xychart-beta
    title "CamusGIT/EvoQuant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 140 --> 142
    line [141, 141]
```

2026-10-18 141 → 2026-10-22 141（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `88f87d6a9d34` · [字段定义](../../DATASET.md)*
