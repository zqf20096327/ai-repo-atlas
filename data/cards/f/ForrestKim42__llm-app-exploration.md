# ForrestKim42/llm-app-exploration

⭐ 23 · MIT · 推送 2026-04-08 · [GitHub](https://github.com/ForrestKim42/llm-app-exploration) · 个人维护

**LLM Agent 系统化探索与操控任意 App 的模式文档（idea file）**

一份方法论文档（自称 idea file），描述让 LLM agent 通过无障碍树（而非截图视觉）读取并操控移动/桌面应用的完整流程：将 App 建模为图（屏幕为节点、交互元素为边），经 DFS 探索后产出 ROUTES.md 路线图与 TRANSITIONS.md 转移表，再据此确定性执行用户流程。配套指认 mobile-mcp 与 desktop-mcp 两个 MCP server 实现。探索分 L1/L2/L3 三档深度，L3 会执行真实操作并可能产生真实花费。文档本身不含可安装代码。

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

- 读无障碍树替代截图，元素以 TYPE:Label 稳定 ID 标识
- 图模型 + DFS 系统化探索，产出 ROUTES.md 与 TRANSITIONS.md 两个结构化产物
- 探索/组织/分析三阶段严格分离，另派生 Act 阶段实现确定性批量执行
- 覆盖 Android/iOS（mobile-mcp）与 macOS 原生/Electron（desktop-mcp）

## 适用场景

- 让我的 agent 为 App 建立完整的界面地图与转移表
- 基于转移表批量、确定性地执行跨屏幕甚至跨应用的用户流程
- 做 UX 审计、竞品分析或用户流程梳理时获取完整覆盖数据

## 场景标签

`GUI 自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: This is an idea file. Share it with your LLM agent and explore together. The specifics will depend on your app, your
> L11: The idea here is different. An LLM agent connected to a device can read the screen (accessibility tree), understand

## 星数曲线

```mermaid
xychart-beta
    title "ForrestKim42/llm-app-exploration 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `62c11196b94d` · [字段定义](../../DATASET.md)*
