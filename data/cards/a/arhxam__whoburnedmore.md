# arhxam/whoburnedmore

⭐ 15 · TypeScript · MIT · 推送 2026-10-24 · [GitHub](https://github.com/arhxam/whoburnedmore) · [官网](https://whoburnedmore.com) · 个人维护

**统计 AI 编码代理 token 消耗并提交公共排行榜的 CLI**

通过 ccusage 读取本地 AI 编码工具（Claude Code、Codex、Gemini CLI、Copilot、Cursor 等）的使用记录，汇总 token 数与估算成本，并每日提交到 whoburnedmore.com 公共排行榜，生成可分享的仪表盘；仅上传聚合数字，不上传提示词、代码或文件路径。首次运行通过浏览器授权码登录并绑定机器；支持 --local 全离线模式、组织看板、每 15 分钟后台同步（Windows 依赖 Script Host/PowerShell）。另含 macOS 菜单栏应用 BurnBar 的源码。

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

- 聚合多个 AI 编码工具的 token 用量与估算成本
- 提交每日聚合数字到公共排行榜（不含提示词/代码/文件路径）
- --local 全离线模式，本地生成 HTML 仪表盘不上传
- 随附 macOS 菜单栏应用 BurnBar 源码

## 适用场景

- 统计并对比各 AI 编码工具的 token 消耗与成本
- 与朋友或组织成员在排行榜上比较用量
- 仅本地查看用量报告而不上传任何数据

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L15: `whoburnedmore` reads your local AI coding-agent usage (Claude Code, Codex, Gemini CLI,
> L17: the tokens and estimated cost, and **submits your daily totals to the whoburnedmore.com

## 星数曲线

```mermaid
xychart-beta
    title "arhxam/whoburnedmore 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-31 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b9d342e2baa3` · [字段定义](../../DATASET.md)*
