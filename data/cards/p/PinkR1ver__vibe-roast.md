# PinkR1ver/vibe-roast

⭐ 47 · JavaScript · MIT · 推送 2026-10-19 · [GitHub](https://github.com/PinkR1ver/vibe-roast) · [官网](https://www.npmjs.com/package/vibe-roast) · 个人维护 · 中文 README

**读取本地 AI 编码历史，生成 16 型编程人格画像与吐槽报告**

面向使用 AI 编码代理的开发者的本地优先分析工具：扫描 Codex、Claude Code、Cursor、Cline、Aider 等 15 种本地会话存储，基于四条行为轴的确定性本地计算得出 16 型编程人格之一，并输出基于证据的双语吐槽、词云与主题、Agent/provider/model/token 使用分析及可分享的人格卡片。AI 写作为可选路径：本地确定性格式、Cloudflare Workers AI 托管或自带 key 调用所选模型。以 npm 包提供，CLI 可输出 JSON 报告；不读取的源自动跳过，无需账号或 API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性本地人格计算，四轴（Maker/Orchestrator/Verifier/Focused 等）映射 16 型角色
- 覆盖 15 种本地编码代理历史源（Codex/Claude Code/Cursor/Aider 等）
- 吐槽/Hashtag 三种生成模式：本地确定文案、托管 Workers AI、自带 provider key
- CLI inspect 输出 JSON 报告，支持自定义各源存储路径

## 适用场景

- 查看自己使用 Claude Code/Codex/Cursor 等代理的编码行为画像
- 分析 token 用量、活动热力图与 provider/model 使用分布
- 生成可分享的 3:4 人格吐槽卡片
- 以 JSON 形式导出编程行为分析数据

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L44: The personality calculation is deterministic and local. AI writing is optional.
> L72: Vibe Roaster scans the supported local stores it can find, starts the local dashboard server, and opens:

## 星数曲线

```mermaid
xychart-beta
    title "PinkR1ver/vibe-roast 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 46 --> 48
    line [47, 47]
```

2026-10-18 47 → 2026-10-25 47（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `c3027c23a5cc` · [字段定义](../../DATASET.md)*
