# jerry609/PaperBot

⭐ 108 · Python · MIT · 推送 2026-06-16 · [GitHub](https://github.com/jerry609/PaperBot) · [官网](https://paper-bot-git-test-milestone-v12-jerrys-projects-bfbe8245.vercel.app/studio) · 个人维护 · 中文 README

**个人学术 AI 基础设施：论文发现、LLM 评审、追踪与 Paper2Code 一体化**

端到端研究助手，覆盖论文发现→分析→复现流程：聚合 arXiv、Semantic Scholar、OpenAlex、HF Daily Papers、papers.cool 多源搜索并去重评分；LLM-as-Judge 做五维评分与低质过滤；支持每日报告生成与多渠道推送（Email/Slack/钉钉/飞书等）；提供 Paper2Code 代码骨架生成、AgentSwarm 多智能体编排（Claude Code 集成、Docker/E2B 沙箱）、学者追踪与模拟同行评审。后端 Python+FastAPI，前端 Next.js+Ink CLI，配置至少一个 LLM API key 后运行，部分模块处于 Usable/Planned 状态。

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

- 多源论文搜索聚合与 LLM-as-Judge 五维评分（相关性/新颖性/严谨性/影响力/清晰度）
- Paper2Code：论文→代码骨架（规划→分析→生成→验证）带自修复调试
- AgentSwarm 多智能体编排，Claude Code 集成与 Docker/E2B 沙箱执行
- 研究记忆系统（FTS5+BM25）及 MemoryBench 离线评测套件

## 适用场景

- 每日自动追踪研究主题相关论文并推送到协作渠道
- 用 LLM 评分筛选低质量论文、管理个人文献库
- 从论文生成可复现代码骨架
- 追踪目标学者的引用动态与会议投稿截止时间

## 场景标签

`科研工具` `多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L27: "Oh, God! My idea comes true." is an end-to-end research assistant that automates the paper discovery → analysis → 
> L57: - **LLM-as-Judge** — 5-dimensional scoring (Relevance / Novelty / Rigor / Impact / Clarity) with multi-round calibr
> L70: - **Paper2Code** — Paper → code skeleton (Planning → Analysis → Generation → Verification) with self-healing debugg

## 星数曲线

```mermaid
xychart-beta
    title "jerry609/PaperBot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 107 --> 109
    line [108, 108]
```

2026-10-18 108 → 2026-10-27 108（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `7fa97a41304f` · [字段定义](../../DATASET.md)*
