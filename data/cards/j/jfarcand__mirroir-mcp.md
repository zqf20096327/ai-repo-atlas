# jfarcand/mirroir-mcp

⭐ 424 · Swift · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/jfarcand/mirroir-mcp) · [官网](https://mirroir.dev) · 个人维护

**让 MCP agent 通过 macOS iPhone Mirroring 驱动真实 iPhone**

以 MCP 服务器形式提供 42 个工具（点击、输入、滑动、读屏、听音、启动应用等），使支持 MCP 的 agent 经由 macOS 的 iPhone Mirroring 操作一部真实 iPhone，无需开发者模式、Xcode 或越狱。探索过程可固化为 SKILL.md 技能，并编译为不依赖模型的确定性回放，在 CI 中运行并给出 pass/fail/DRIFT 判定。读屏默认用本地 OCR（Apple Vision + 设备端 YOLO），可选 AI vision 模式。默认只暴露 14 个只读工具，无遥测。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 42 个 MCP 工具驱动真实 iPhone，手机端无需安装任何东西
- 技能编译为无模型参与的确定性回放，可在 CI 中运行
- 本地 OCR 与 AI vision 两种读屏模式可配置
- 默认只读工具 + permissions.json/blockApps 的权限模型

## 适用场景

- 让 coding agent 代我完成 iPhone 上的应用操作和跨应用事务
- 把 agent 探索出的操作固化成可重复运行的自动化测试
- 在真实 iPhone 上做 iOS 应用的 e2e 测试
- 驱动 iPhone 上的游戏交互（如与 Chess.com 对弈）

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L27: No Developer Mode, no Xcode, nothing installed on the phone. mirroir-mcp drives your iPhone through macOS iPhone Mi
> L71: - **Tools.** 42 MCP tools: tap, type, swipe, read the screen, listen, launch, and `run_steps` to repeat a sequence 
> L49: your agent ──MCP──▶ mirroir ──iPhone Mirroring──▶ your iPhone

## 星数曲线

```mermaid
xychart-beta
    title "jfarcand/mirroir-mcp 星数(近 23 点)"
    x-axis ["2026-10-24", "2026-10-27", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-02", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-25", "2026-11-26"]
    y-axis "stars" 252 --> 439
    line [267, 268, 269, 270, 271, 272, 273, 267, 285, 289, 291, 296, 297, 298, 333, 362, 376, 385, 394, 398, 403, 414, 424]
```

2026-10-24 267 → 2026-11-26 424（+157）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-25 · 置信度 high · 依据 README sha `05598f32f45a` · [字段定义](../../DATASET.md)*
