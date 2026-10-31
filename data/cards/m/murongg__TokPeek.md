# murongg/TokPeek

⭐ 14 · Swift · MIT · 推送 2026-10-20 · [GitHub](https://github.com/murongg/TokPeek) · 个人维护 · 中文 README

**macOS 菜单栏应用：本地追踪 AI token 用量与费用**

SwiftUI + Rust（tokscale-core）构建的本地优先 macOS 菜单栏应用：在本地发现、解析 AI 会话日志，展示 token 总量、估算费用、每日趋势、客户端占比与模型排行，支持预算与提醒、多周期报告和模型过滤，不向服务器上传会话内容。以签名公证的 Universal 2 安装包分发，要求 macOS 14 及以上；开发需 Xcode 16 与 Rust 工具链，应用未启用 App Sandbox 以便发现会话文件。提供中英文界面与 Sparkle 签名更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地解析会话日志并聚合 token/费用/趋势/模型排行
- 日/周/月预算与 80%/100% 本地提醒
- Universal 2 安装包，Developer ID 签名并经 Apple 公证
- Sparkle 签名更新，更新前需确认

## 适用场景

- 在日常编码中随时查看菜单栏的 token 用量与估算费用
- 按周期和模型过滤回顾 AI 使用情况
- 设置预算并收到用量告警

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L20: TokPeek turns local AI usage logs into a glanceable macOS menu bar dashboard.
> L21: See token totals, estimated cost, daily trends, client share, and model rankings

## 星数曲线

```mermaid
xychart-beta
    title "murongg/TokPeek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `3ca93d9ea19e` · [字段定义](../../DATASET.md)*
