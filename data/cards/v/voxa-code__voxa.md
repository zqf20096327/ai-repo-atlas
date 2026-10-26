# voxa-code/voxa

⭐ 27 · Python · MIT · 推送 2026-08-04 · [GitHub](https://github.com/voxa-code/voxa) · [官网](https://voxa.space) · 个人维护

**语音遥控本机 AI agent 的工具：手机随时对话，完成后来电通知**

由笔记本端服务器与手机客户端组成的语音入口：用户通过 iPhone 对运行在笔记本上的编码 agent（当前支持 Claude Code）下达语音指令，agent 在笔记本上执行任务，完成后通过电话回拨通知用户。兼容 macOS 与 iPhone（Windows 可用未测试，Android 未支持）。仓库内 MIT 部分含服务器与 Web 客户端，可自带 API key 自托管、无需账号；原生 iOS 应用与托管中继/推送/计费服务位于独立闭源仓库，仅用于零配置托管体验。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 语音下达指令，agent 在笔记本执行，完成后手机来电回拨
- 自托管路径：自带 API key、无需账号、无需中继
- 笔记本服务器 + 手机 Web 客户端均在本仓库且 MIT 许可

## 适用场景

- 离开电脑时用手机语音继续指挥 Claude Code 工作
- 任务完成后通过来电获知结果
- 自托管部署语音编码代理环境

## 场景标签

 · 领域:开发者工具/AI 代理客户端

## 证据(README 行号)

> L5:  Talk to your AI agent from anywhere. When it finishes, your phone rings.
> L21: Speak, the agent works on your laptop, your phone calls you back
> L33: |Claude Code|✅ Working|

## 星数曲线

```mermaid
xychart-beta
    title "voxa-code/voxa 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `de67077c9714` · [字段定义](../../DATASET.md)*
