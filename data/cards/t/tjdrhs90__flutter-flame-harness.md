# tjdrhs90/flutter-flame-harness

⭐ 61 · Shell · MIT · 推送 2026-09-01 · [GitHub](https://github.com/tjdrhs90/flutter-flame-harness) · 个人维护

**Claude Code 插件：把 Flutter/Flame 游戏从创意推进到应用商店上架**

面向 Claude Code 的插件，编排一条结构化技能流水线：市场调研→规划→设计→生成器与评估器协商完成标准→构建与 QA 门控→人工试玩审核→AdMob 集成、fastlane 构建、商店截图、提交与复盘。生成器按脚手架/API 接线/UI 打磨三个子阶段构建 Flutter/Flame 项目，评估器在每步交接前运行游戏做 QA。支持 --auto-idea/--auto-deploy 全自动跑通，默认在部署前暂停等待人工试玩批准（cd <slug> && flutter run）。凭据不入库，通过环境变量或密钥管理器传入。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 生成器↔评估器循环，评估器运行游戏后做 QA 门控
- Phase B 自动化 AdMob、fastlane 构建、TestFlight/内部轨道提交、商店截图与 ASO 元数据
- 11 个可单独触发的技能命令（research/plan/design/contract/generator/evaluator/admob/build/screenshot/submit/retro）
- 默认部署前暂停供人工试玩批准，可 --auto-deploy 跳过

## 适用场景

- 有游戏创意想用 AI 流水线生成并上架 Flutter/Flame 游戏
- 自动化 App Store / Play Store 的构建、截图与提交流程
- 在 Claude Code 中分阶段走市场调研→PRD→设计→构建→QA 的游戏开发流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: A Claude Code plugin that takes a Flutter/Flame game from raw idea all the way to the app stores. The harness orches
> L55: /plugin marketplace add tjdrhs90/flutter-flame-harness

## 星数曲线

```mermaid
xychart-beta
    title "tjdrhs90/flutter-flame-harness 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-27 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `808e68c6d68c` · [字段定义](../../DATASET.md)*
