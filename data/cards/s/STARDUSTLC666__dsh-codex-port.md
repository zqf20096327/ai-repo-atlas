# STARDUSTLC666/dsh-codex-port

⭐ 10 · JavaScript · MIT · 推送 2026-11-23 · [GitHub](https://github.com/STARDUSTLC666/dsh-codex-port) · [官网](https://github.com/STARDUSTLC666/dsh-suite) · 个人维护 · 中文 README

**把本机 Codex 技能移植到 DeepSeek Harness 的插件**

面向 DeepSeek Harness（>=0.2.2-rc.3）的技能移植插件：发现本机 Codex 技能，列出可移植项及其依赖与许可，导入前预览目标路径与同名冲突，用户确认后按需导入，原技能保持不变。适配 Windows 路径与 Cordis 热重载清理。通过 DSH 桌面版插件面板安装，或用 dsh plugin 命令行安装；网页版对应 web 配置。技能运行所需的第三方依赖仍需用户单独准备。

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

- 导入前预览目标目录与重名冲突再决定
- 保留技能的调用策略与许可说明
- 按需选择导入并查看迁移结果
- 适配 Windows 路径与 Cordis 热重载清理

## 适用场景

- 把已有的 Codex 技能迁移到 DSH 工作区使用
- 导入前检查技能依赖与许可信息
- 多人环境中处理技能同名冲突

## 场景标签

 · 领域:AI agent 工具链/技能迁移

## 证据(README 行号)

> L7: DeepSeek Harness（`>=0.2.2-rc.3`）Codex 技能移植插件：支持发现本机 Codex 技能、预览目标路径与重名冲突、保留调用策略与许可说明，并适配 Windows 路径与 Cordis 热重载清理。
> L23: 在 DSH 桌面版「插件」面板安装 `dsh-codex-port`。已配置命令行时也可使用：

## 星数曲线

```mermaid
xychart-beta
    title "STARDUSTLC666/dsh-codex-port 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-24"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-11-18 10 → 2026-11-24 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `4328dbd3cf6b` · [字段定义](../../DATASET.md)*
