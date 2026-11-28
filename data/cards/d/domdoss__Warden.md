# domdoss/Warden

⭐ 171 · JavaScript · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/domdoss/Warden) · [官网](https://aionsystems.ca) · 个人维护

**本地桌面个人 AI 助理：本地+云混合模型执行日常操作**

Warden 是一个运行在用户桌面上的个人 AI 助理应用，通过 Ollama 运行本地模型处理快速、私有任务，并调用云端模型处理更重的工作，两者在单一对话中混合使用。它执行 shell 命令、控制鼠标键盘、驱动真实浏览器、收发邮件、管理日历，并可编辑和重启自身源代码；README 明确声明无沙箱与容器隔离，模型错误或提示注入可能造成与用户终端权限相当的任意操作。采用多 seat 架构：主 seat 直接执行多数任务，仅将邮件/日程、重代码、审计等移交给子 agent，后台任务通过 inbox 与确定性 churn detector 管理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 Ollama 模型与云端模型在同一对话中混合路由
- 多 seat 架构：主 seat 自行执行浏览器/桌面/shell 任务，按 WHAT brief 移交子 agent
- 确定性 churn detector 检测只读调用循环并注入 commit nudge
- 后台任务 inbox 与失败自动重委托机制

## 适用场景

- 在个人桌面机上通过对话让 agent 代替操作浏览器、文件和 shell
- 本地模型处理私密任务、云端模型处理重任务的混合使用
- 长任务的委托与后台运行、完成结果统一汇报

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L27: Warden is an AI agent with **the same access as your user account**. It executes shell commands, moves your mouse a
> L37: Warden is a personal AI assistant that lives on your desktop. It runs local models through Ollama for fast, private

## 星数曲线

```mermaid
xychart-beta
    title "domdoss/Warden 星数(近 3 点)"
    x-axis ["2026-10-26", "2026-11-14", "2026-11-28"]
    y-axis "stars" 170 --> 173
    line [172, 171, 171]
```

2026-10-26 172 → 2026-11-28 171（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 low · 依据 README sha `7f92443b3ded` · [字段定义](../../DATASET.md)*
