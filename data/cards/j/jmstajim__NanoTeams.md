# jmstajim/NanoTeams

⭐ 34 · Swift · MIT · 推送 2026-09-20 · [GitHub](https://github.com/jmstajim/NanoTeams) · [官网](https://github.com/jmstajim/NanoTeams/releases/) · 个人维护

**macOS 本地多智能体 AI 编码团队应用，全程离线运行**

面向 Mac 开发者的原生 Swift/SwiftUI 应用，通过本机 Ollama 或 LM Studio 运行本地模型：用户以 Supervisor 身份创建任务，由 PM、工程师、代码评审等角色按工件依赖协作执行；Coding Assistant/Coding Agent 可读写文件、运行 git 与 Xcode 构建。含自主调度的 Autovisor、需逐条批准的 Bash 与屏幕控制、51 个内置工具、本地模型速度基准等。要求 macOS 15.0+、Ollama 0.9+ 或 LM Studio 0.4.0+；无云端、无 API key、无遥测，文件访问沙箱限定于工作目录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多角色 AI 团队按工件依赖流水线协作，支持团队间委派与自定义团队导入导出
- Autovisor 自主创建/调度/审核任务，默认 3 小时睡眠计时器
- Bash 与屏幕控制默认人工逐条批准，可交由设备端判定器接管
- 本地模型基准：测生成速度、首 token 时间与 prefill，输出中位数排行榜

## 适用场景

- 用本地模型让 AI 团队规划、实现并评审代码改动
- 代码不能离开本机的隐私优先或 NDA 场景下做 AI 辅助开发
- 用自然语言把多文件任务委派给工程团队并跟踪工件流水线

## 场景标签

`多智能体` `编码 Agent` · 领域:Agent 开发

## 证据(README 行号)

> L11: **NanoTeams is a free, open-source, local-first AI coding agent and multi-agent AI team app for macOS.** It runs 10
> L13: Chat with the **Coding Assistant** to read and edit your files, or let the **Coding Agent** make small changes itse
> L48: Take the **FAANG Team**: you describe what you want → PM writes requirements → UX researches and designs → Tech Lea

## 星数曲线

```mermaid
xychart-beta
    title "jmstajim/NanoTeams 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-30 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `3bb99bba5ce0` · [字段定义](../../DATASET.md)*
