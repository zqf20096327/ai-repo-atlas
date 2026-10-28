# sparkorbit/sparkorbit

⭐ 21 · Python · MIT · 推送 2026-04-02 · [GitHub](https://github.com/sparkorbit/sparkorbit) · 组织维护 · 中文 README

**AI 资讯聚合面板：论文、模型、榜单、新闻一屏呈现并可本地摘要**

自托管的 AI 情报监控面板：按需抓取 40+ 来源（arxiv 论文、热门模型、公司动态、社区新闻），无需 API key 与登录；按点赞/下载/star/分数排序，内置多模态 AI 模型排行榜横向对比。可选启用本地 LLM（Qwen 3.5 4B，经 Ollama 运行）生成每日简报与论文主题分组，需 NVIDIA GPU 约 13GB VRAM，无 GPU 时仅保留来源聚合功能。通过 git clone 加 Docker 脚本一键部署，在 Linux/macOS 完整测试，Windows 仅 WSL 部分测试。属个人 hackathon 项目，LLM 处理稳定性仍在改进中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 40+ 来源按需抓取，无需 API key 与登录
- Text/Code/Vision/Image/Video/Search 榜单并列对比
- 本地 LLM（Qwen 3.5 4B + Ollama）生成每日简报与论文分组，数据不出本机
- Docker 脚本一键启停，无 GPU 亦可运行完整面板

## 适用场景

- 每天几分钟追上 AI 论文、模型发布与榜单变化
- 在一个面板里横向查看各模态模型排行榜
- 用本地 GPU 生成每日 AI 简报而不依赖云端 API

## 场景标签

`精选清单` `网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L35: - **Summarize** — local LLM (Qwen 3.5 4B) reads everything and generates a daily briefing + paper topic grouping. R
> L60: - No GPU? No problem — pick `N` and you still get the full dashboard with 40+ sources, leaderboards, and engagement

## 星数曲线

```mermaid
xychart-beta
    title "sparkorbit/sparkorbit 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `8d1633c95eec` · [字段定义](../../DATASET.md)*
