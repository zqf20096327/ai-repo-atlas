# KlaatAI/klaatcode

⭐ 353 · TypeScript · NOASSERTION · 推送 2026-09-16 · [GitHub](https://github.com/KlaatAI/klaatcode) · [官网](https://klaatai.com) · 组织维护

**终端 AI 编程代理，按任务难度自动路由模型档位以降成本**

终端原生的 AI 编程代理，属 Claude Code、opencode、Codex CLI、Aider 同类产品：读代码、改文件、执行命令并自检。核心机制是托管服务 Klaatu 逐条消息分类并路由到六个成本档位（nano→fast→code→reason→heavy→titan），工具调用不计费；客户端是开源薄终端，路由与代码图谱索引在服务端，需登录 KlaatAI 账号。另支持接入任意 OpenAI 兼容端点自带模型。提供 npm、curl 安装脚本、Homebrew 与独立编译二进制，附 33 项任务可复现基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 逐请求六档模型路由，工具调用轮次不计费
- 项目索引为调用图谱，支持符号/调用者/影响面查询与语义搜索
- 编辑后自动运行类型检查/linter 并将错误回传模型自修复
- 实时燃烧率监控、任务成本归因与会话费用上限

## 适用场景

- 在终端里让 AI 代理跨文件修复错误、执行重构
- CI 中用 headless 模式跑固定预算的自动修复任务
- 按任务难度自动匹配模型档位以控制推理开销

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9:  The terminal-native AI coding agent, powered by Klaatu smart model routing.
> L26: **KlaatAI** is an AI platform built around **Klaatu-o1**, a small, fast, agentic router model. Instead of sending e
> L34: Klaat Code is this repo: a terminal-native coding agent you install once and run in any project. It reads your code

## 星数曲线

```mermaid
xychart-beta
    title "KlaatAI/klaatcode 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-27"]
    y-axis "stars" 352 --> 360
    line [359, 353, 353]
```

2026-10-18 359 → 2026-10-27 353（-6）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `f49fb55b4a05` · [字段定义](../../DATASET.md)*
