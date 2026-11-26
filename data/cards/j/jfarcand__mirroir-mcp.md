# jfarcand/mirroir-mcp

⭐ 424 · Swift · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/jfarcand/mirroir-mcp) · [官网](https://mirroir.dev) · 个人维护

**让 MCP agent 通过 iPhone Mirroring 操控真实 iPhone 的服务器**

一个 MCP 服务器，通过 macOS iPhone Mirroring 驱动用户自己的 iPhone，提供 42 个工具（点击、输入、滑动、读屏、听音、启动应用等），供支持 MCP 的 AI 客户端调用。要求 macOS 15 及以上并连接 iPhone Mirroring；手机端无需开发者模式、Xcode 或任何安装。探索结果可固化为 SKILL.md 技能，并编译为不依赖模型的确定性回放，可在 CI 中运行并输出 DRIFT 判定。默认只暴露 14 个只读工具，通过 permissions.json 控制权限。

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

- 42 个 MCP 工具驱动 iPhone：tap、type、swipe、读屏、listen、launch、run_steps
- 探索生成 SKILL.md 技能，编译为无模型的确定性回放并在 CI 运行（pass/fail/DRIFT）
- describe_screen 支持本地 OCR（Apple Vision + 设备端 YOLO）与 AI vision 两种读屏模式
- 只读默认、blockedApps 屏蔽、无遥测、退出镜像即停止输入

## 适用场景

- 让编码 agent 代我在 iPhone 上跨应用办事和自动化操作
- 把 agent 在手机上的一次操作沉淀为可复用的技能和 E2E 测试
- 在 CI 中以确定性回放回归测试 iOS 登录界面等流程
- 让 agent 操控手机上的应用与游戏（如 Spotify、Chess.com）

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L28: No Developer Mode, no Xcode, nothing installed on the phone. mirroir-mcp drives your iPhone through macOS iPhone Mi
> L50: your agent ──MCP──▶ mirroir ──iPhone Mirroring──▶ your iPhone
> L72: - **Tools.** 42 MCP tools: tap, type, swipe, read the screen, listen, launch, and `run_steps` to repeat a sequence 

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
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `7cb232755a83` · [字段定义](../../DATASET.md)*
