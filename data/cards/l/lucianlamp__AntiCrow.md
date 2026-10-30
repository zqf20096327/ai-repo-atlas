# lucianlamp/AntiCrow

⭐ 22 · TypeScript · NOASSERTION · 推送 2026-03-25 · [GitHub](https://github.com/lucianlamp/AntiCrow) · [官网](https://anticrow.pages.dev) · 个人维护 · 中文 README

**从 Discord 远程控制 Antigravity AI 的桥接扩展**

AntiCrow 是一个 Antigravity 扩展，充当 Discord 与 Antigravity AI 编辑器之间的桥接层：用户从 Discord（手机/PC）发送自然语言指令，扩展通过 CDP（Chrome DevTools Protocol）直接操作本机的 Antigravity 执行任务，并把结果与进度实时回传。支持 cron 定时执行、多工作区自动映射为 Discord 分类、文件附件分析、模型/模式切换、连续自动模式与多 agent 并行模式，附带 21 种危险操作检测的安全护栏与本地记忆。所有处理在本机运行，需自行创建 Discord Bot，Node.js 18+ 为前提。采用 PolyForm Noncommercial 非商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言指令经 Discord 触发 Antigravity 即时或 cron 定时执行
- 通过 CDP 直接操作编辑器，不使用 OAuth/API key
- 连续自动模式与多 agent 并行执行，附 21 模式安全护栏
- 加密存储 Bot Token、用户 ID 白名单、本地记忆（全局/工作区）

## 适用场景

- 在手机上通过 Discord 远程让 AI 处理本机项目任务
- 定时自动执行例行任务（如每天汇总 GitHub 通知）
- 多人/多项目并行时按 Discord 分类管理各工作区任务

## 场景标签

`编码 Agent` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L50: AntiCrow acts as a bridge between Discord and Antigravity.
> L57: 🤖 Antigravity AI (Your PC)
> L286: AntiCrow does not use Antigravity's OAuth keys or API keys. It operates the Antigravity editor directly via **CDP 

## 星数曲线

```mermaid
xychart-beta
    title "lucianlamp/AntiCrow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-30 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `bf0faef365a4` · [字段定义](../../DATASET.md)*
