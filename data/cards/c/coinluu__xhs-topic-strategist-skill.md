# coinluu/xhs-topic-strategist-skill

⭐ 28 · MIT · 推送 2026-07-21 · [GitHub](https://github.com/coinluu/xhs-topic-strategist-skill) · 个人维护 · 中文 README

**面向 AI Agent 的小红书选题策划 Markdown 规则包**

纯 Markdown、跨 Agent、无代码依赖的小红书选题策划 Skill：以轻量账号画像表为默认输入，把热点匹配、选题评分、风险审查、标题/封面/标签建议组织成 SKILL.md、WORKFLOW.md、SCORING_RULES.md、RISK_RULES.md 等规则文件，供 Claude、Codex、Cursor Agent、Manus、ChatGPT Agent 等任何能读取 Markdown 的 Agent 使用，输出 Markdown 报告与 JSON-like 结构化结果。覆盖 28 个赛道，含 9 类强制风险审查；支持联网 Live Hotspot 与离线 Evergreen 两种模式。个人博主、MCN 内容团队与营销顾问均可使用；无代码依赖，无 API Key。项目声明不自动发帖、不绕过平台限制、不替代合规判断。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯 Markdown 规则包，任何能读 Markdown 的 Agent 均可使用，不绑定模型或平台
- 轻量账号画像默认输入，不依赖账号主页链接
- 覆盖 28 个小红书赛道与 9 类强制风险审查赛道
- Live Hotspot / Evergreen / User-Provided 三种热点模式，明确标注核实状态

## 适用场景

- 让 Claude 或 Cursor Agent 按统一规则产出小红书选题策划包
- MCN 内容团队统一多账号的选题方法与风控口径
- 离线环境下基于常青需求生成非实时选题

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L37: `xhs-topic-strategist-skill` 是一个面向 AI Agent 的小红书选题策划规则包。
> L71: 这个 Skill 的所有规则都写在 Markdown 文件里：
> L81: 只要 Agent 能读取 Markdown，就可以使用这套规则。它不绑定某个模型、平台、插件、API 或运行环境。

## 星数曲线

```mermaid
xychart-beta
    title "coinluu/xhs-topic-strategist-skill 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-27 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `910da4ccb794` · [字段定义](../../DATASET.md)*
