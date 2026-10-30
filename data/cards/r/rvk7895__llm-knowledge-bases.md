# rvk7895/llm-knowledge-bases

⭐ 35 · Shell · MIT · 推送 2026-06-16 · [GitHub](https://github.com/rvk7895/llm-knowledge-bases) · 个人维护

**Claude Code 插件：把原始研究资料编译为 LLM 维护的 Obsidian 维基**

面向 Claude Code 用户的插件：将文章、论文、仓库、YouTube 转录、数据集等原始资料放入 raw/ 目录后，由 Claude 编译为带摘要、反向链接、概念条目与自动索引的 Obsidian 知识库；支持三档深度问答（索引速答/全文交叉引用+网络搜索/多 agent 并行深度研究），输出 Markdown 报告、Marp 幻灯片与 matplotlib 图表；另提供自动健康检查（断链、孤页、不一致）与演化维护工作流。需 Claude Code CLI 与 Obsidian 作为前置条件，通过 Claude Code 插件市场安装，可选配置 Smaug 摄取 X/Twitter 内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单命令将原始资料编译为含索引与反向链接的 Obsidian 维基
- 三档深度问答，Deep 档为多 agent 并行网络研究
- 输出 Markdown 报告、Marp 幻灯片、matplotlib 图表
- 自动化健康检查（断链/孤页/不一致）与知识库演化维护

## 适用场景

- 把日常收集的论文、文章、视频转录整理成可检索的个人维基
- 基于个人知识库做多深度档位的问答与深度研究
- 持续维护知识库健康度并自动建议新条目与关联

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: A Claude Code plugin that turns raw research material into an LLM-maintained Obsidian wiki -- inspired by Andrej Kar
> L5: You drop source material into `raw/`, run a single command, and Claude handles the rest: compiling interlinked wiki 
> L12: 2. **Compile** -- Claude builds a structured Obsidian vault with summaries, backlinks, concept articles, and auto-g

## 星数曲线

```mermaid
xychart-beta
    title "rvk7895/llm-knowledge-bases 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-30 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `22e745b2431e` · [字段定义](../../DATASET.md)*
