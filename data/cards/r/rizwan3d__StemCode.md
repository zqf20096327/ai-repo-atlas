# rizwan3d/StemCode

⭐ 32 · C# · Apache-2.0 · 推送 2026-10-22 · [GitHub](https://github.com/rizwan3d/StemCode) · [官网](https://growbitlabs.com/stemcode) · 个人维护

**本地优先的 AI 编程 Agent，覆盖桌面/终端/IDE/CI**

面向开发者的本地优先 AI 编程代理：在真实本地仓库中运行，理解代码、规划变更、编辑文件、执行校验、审查 diff 并自动化 PR 反馈。提供桌面应用、CLI、VS Code/Visual Studio/JetBrains 扩展与 GitHub Actions 等 CI 集成。机制上支持订阅登录、API key、OpenAI 兼容端点或 Ollama/LM Studio 等本地模型；带权限审批、tracked edit 撤销/重做、.stemcode/ 版本化记忆文件、子代理与 LSP 代码智能。CLI 为自包含二进制，SDK 基于 .NET 并包装为 Python/JS 包。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同一 Agent 跨桌面/CLI/IDE/CI 四类界面运行
- 支持订阅登录、API key、OpenAI 兼容端点与 Ollama/LM Studio 本地模型
- 权限规则、tracked edit 撤销重做与版本化 .stemcode/ 工作区记忆
- LSP 代码智能与子代理（独立上下文）委托任务

## 适用场景

- 在终端或 IDE 中让 AI 理解仓库并实施代码变更
- 自动审查 pull request / merge request 并给出 findings
- 用本地模型或订阅账号在本地仓库完成规划与编辑工作

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L5:  Local AI coding agent for desktop, terminal, editor, and CI workflows.
> L273: - OpenAI

## 星数曲线

```mermaid
xychart-beta
    title "rizwan3d/StemCode 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-28 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `915480da630d` · [字段定义](../../DATASET.md)*
