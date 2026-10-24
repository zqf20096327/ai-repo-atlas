# Ericyoung-183/alpha-insights

⭐ 71 · Python · MIT · 推送 2026-06-29 · [GitHub](https://github.com/Ericyoung-183/alpha-insights) · [官网](https://ericyoung-183.github.io/alpha-insights/) · 个人维护

**面向 Claude Code/Codex 的商业研究 AI 技能包**

以 SKILL.md 技能包形式装入 Claude Code 兼容运行时或 Codex Desktop 的商业分析 AI 助手：用户提问后自动识别研究场景、匹配 19 个分析框架（Porter 五力、SWOT、商业模式画布等）、执行多路并行检索并生成结构化 HTML 研究报告。V4 采用 harness 强制机制：状态机跟踪阶段、7 阶段+Stage 3.5 门校验、HTML 写入守卫、证据与数值完整性门、A-D 数据质量分级。数据源方面公开渠道开箱即用，小红书/知识库/内部数据为可选扩展。安装通过 git clone 加 Python 安装/校验脚本完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 19 个分析框架与 9 种思维方法论，自动匹配 10 类研究场景
- harness 强制工作流：阶段门校验、HTML 写入守卫、断点状态检查
- 证据链标注来源与置信度，A-D 四级数据质量分级
- 双平台适配：Claude Code frontmatter hooks 与 Codex wrapper

## 适用场景

- 让 Claude Code/Codex 生成带证据链的行业与竞争分析报告
- 按 MECE/金字塔原理等框架做结构化商业研究
- 投资尽调、市场进入、商业模式拆解等场景获得分级置信度的结论

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L13: Alpha Insights is a professional business analysis AI assistant for Claude Code compatible runtimes and Codex Deskt
> L137: 4. Generate a structured HTML research report

## 星数曲线

```mermaid
xychart-beta
    title "Ericyoung-183/alpha-insights 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-23", "2026-10-24"]
    y-axis "stars" 68 --> 72
    line [69, 70, 71, 71]
```

2026-10-18 69 → 2026-10-24 71（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `ef4186194f6c` · [字段定义](../../DATASET.md)*
