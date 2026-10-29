# shenjiecode/pi-wechat-assistant

⭐ 20 · TypeScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/shenjiecode/pi-wechat-assistant) · [官网](https://www.npmjs.com/package/pi-wechat-assistant) · 个人维护 · 中文 README

**微信桥接扩展：在微信中继续 pi 会话**

pi 的微信扩展：通过微信向运行中的 pi 会话发送任务、图片与文件，接收回复与项目文件，支持可定制的回复规则、回执通知与可选桌面同步。提供会话迁移功能，可在不同 pi 会话间转移微信连接。仅接受绑定的微信用户，同一时刻一个桥接占用本地账号状态；需 Node.js ≥20.3.0 与可用的 pi 模型配置，计算机与 pi 需保持运行。通过 pi install npm 命令安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 微信与 pi 会话间收发文本、图片与文件
- 可选桌面同步：镜像桌面输入与 AI 回复，不回放历史
- 会话迁移：在 pi 会话间转移活动微信连接
- /wechat 系列命令管理桥接状态与配置

## 适用场景

- 用手机微信向 pi 发任务并接收回复
- 在外出时继续桌面上的 pi 对话
- 通过微信远程取消 AI 任务与查看状态

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L17: A WeChat extension for pi: send tasks, read replies, and exchange files with a running pi session from your phone.
> L28: Requires Node.js **≥20.3.0**, a working pi model configuration, and the Node.js version required by your installed 

## 星数曲线

```mermaid
xychart-beta
    title "shenjiecode/pi-wechat-assistant 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-22 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `02641d661b79` · [字段定义](../../DATASET.md)*
