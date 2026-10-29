# heyuxuan0209/read-anything

⭐ 31 · JavaScript · MIT · 推送 2026-08-06 · [GitHub](https://github.com/heyuxuan0209/read-anything) · 个人维护 · 中文 README

**让 AI agent 读链接/播客/视频并产出中文结构化解读的自包含 skill**

面向 AI agent 使用者的自包含技能包：丢入网页、YouTube/B站视频、小宇宙播客、X 帖子或本地录音链接后，由脚本抓取材料、可选经 faster-whisper 本地转写，再产出精读稿、快扫、访谈拆解、会议纪要、论文拆解等六种中文结构化解读模板，并可就材料继续追问（答案只基于原文）。核心逻辑为纯 markdown 剧本加零依赖命令行脚本，可接入 Claude Code、Codex、Cursor、Gemini CLI 等任意能跑 shell 的 agent。限制：解读质量取决于所用模型，不承诺跨模型一致；登录墙后文档无法抓取。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 网页/视频/播客/本地录音统一入口，自动抓取与本地转写（faster-whisper，音频不出本机）
- 六种解读模板（精读稿/快扫/访谈拆解/会议纪要/论文拆解/选题素材），支持自定义模板
- agent 无关设计：PLAYBOOK.md + 零依赖脚本，一条 clone 命令接入各类 agent
- 诚实降级原则：抓取失败或材料残缺时如实告知，不硬编解读

## 适用场景

- 把收藏的英文长文/播客快速读成中文结构化笔记
- 在 AI agent 里就一篇材料持续追问细节
- 会议录音或播客本地转写后按人拆观点、拆待办

## 场景标签

`语音识别` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L9:  演示：丢一个链接进去 → 自动抓取 / 转写 → 出中文结构化解读（精读稿 / 快扫 / 访谈拆解…）→ 就着材料继续追问。
> L72: **Other agents (Codex / Cursor / Gemini CLI / OpenClaw…)**: the core logic all lives in
> L73: `PLAYBOOK.md` (a pure-markdown playbook) + `scripts/` (plain command-line tools, JSON in and out),

## 星数曲线

```mermaid
xychart-beta
    title "heyuxuan0209/read-anything 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 29 --> 32
    line [30, 31, 31]
```

2026-10-18 30 → 2026-10-29 31（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 low · 依据 README sha `207da435c33d` · [字段定义](../../DATASET.md)*
