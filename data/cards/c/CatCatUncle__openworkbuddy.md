# CatCatUncle/openworkbuddy

⭐ 339 · JavaScript · NOASSERTION · 推送 2026-10-22 · [GitHub](https://github.com/CatCatUncle/openworkbuddy) · [官网](https://catcatuncle.github.io/openworkbuddy/) · 个人维护 · 中文 README

**本机优先的开源 AI 办公助理：一句话生成 PPT/Word/Excel/网页文件**

本地优先的 AI 办公工作台，面向常做周报、PPT、表格、文档的个人及需自托管部署的团队。用户输入一句任务，agent 自行规划、调用工具并产出可打开的 PPTX/DOCX/XLSX/HTML 文件。模型可切换：设置页提供 OpenAI/Anthropic/OpenRouter/DeepSeek/通义/智谱/Kimi/火山方舟/Ollama 预设（BYOK），本机安装的 Claude Code / Codex CLI 可作为执行引擎。提供 macOS/Windows 安装包、源码运行与 Docker 多人部署；支持 MCP 接入、Markdown 技能扩展、定时任务与 IM 推送。许可证为 PolyForm Noncommercial 加商业授权（个人非商用/学校公益免费，公司及个人商用须购买）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 任务产出真实 PPTX/DOCX/XLSX/HTML 文件，成果面板可验收
- 模型可切换：DeepSeek/通义/智谱/Kimi/OpenRouter/Ollama 等预设（BYOK）
- 本机 Claude Code / Codex CLI 可作为执行引擎
- 技能以 Markdown 文件形式扩展（skills/<名字>/skill.md），存盘即生效
- 提供 Docker 多租户私有化部署与 CLI（与桌面版共享配置与会话）

## 适用场景

- 一句话生成项目汇报 PPT、周报、Word/Excel 文档
- 自托管部署给团队做多人 AI 办公工作台
- 配置定时任务抓取信息并推送到飞书/企微/钉钉
- 想读懂 agent 执行过程的开发者阅读模型路由、工具调用与 Trace 实现

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L3:  本机优先的 AI 办公工作台，把你的资料和要求变成可打开、可修改的文件。
> L71: |帮我出一份 Q3 复盘 PPT，数据用这个 Excel|读表 → 算 → 一个能直接放的 `.pptx`|
> L77:  一句话进去，OpenWorkBuddy 自己规划、动手、验收，出来的是 PPTX / DOCX / XLSX / HTML 文件

## 星数曲线

```mermaid
xychart-beta
    title "CatCatUncle/openworkbuddy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 324 --> 339
    line [325, 335, 338]
```

2026-10-18 325 → 2026-10-22 338（+13）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 mid · 依据 README sha `dc1e602915c7` · [字段定义](../../DATASET.md)*
