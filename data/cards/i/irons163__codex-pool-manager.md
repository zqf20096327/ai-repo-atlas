# irons163/codex-pool-manager

⭐ 48 · Swift · 推送 2026-10-23 · [GitHub](https://github.com/irons163/codex-pool-manager) · 个人维护 · 中文 README

**macOS 应用：集中管理与轮换多个 Codex/OpenAI 账户**

面向 macOS 用户的 Codex/OpenAI OAuth 账户池管理工具：支持账户增删分组、从 Codex/OpenAI 端点同步用量配额、智能/手动/专注三种切换模式自动轮换活动账户，并通过菜单栏与桌面小组件展示状态。读取本地 ~/.codex 等路径导入已有会话，可写 provider 块到 config.toml。含重置监控、会话用量分析（本地 sessions 元数据，不存对话内容）、JSON 快照备份。发布双架构 DMG，也可用 Xcode 16+ 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按剩余配额智能选择并自动轮换账户（Intelligent/Manual/Focus 三模式）
- 菜单栏与 macOS 桌面小组件展示剩余额度与重置时间
- 读取本地 Codex sessions 元数据做用量/费用估算分析，不存对话内容
- OAuth 登录、本地账户发现导入与 JSON 快照备份/恢复

## 适用场景

- 多个 Codex/OpenAI 账户集中管理并快速切换当前认证
- 监控各账户每周与 5 小时额度重置时间，规划使用排期
- 在菜单栏/小组件随时查看账户池剩余用量

## 场景标签

 · 领域:AI 服务账户管理/桌面工具

## 证据(README 行号)

> L5: Codex Pool Manager is a macOS app for operating a pool of Codex/OpenAI OAuth accounts from one control panel.
> L62: - Sync usage from Codex/OpenAI endpoints for all eligible accounts.

## 星数曲线

```mermaid
xychart-beta
    title "irons163/codex-pool-manager 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 47 --> 49
    line [48, 48]
```

2026-10-18 48 → 2026-10-26 48（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `18e1ffae58d7` · [字段定义](../../DATASET.md)*
