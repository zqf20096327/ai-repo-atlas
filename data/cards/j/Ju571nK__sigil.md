# Ju571nK/sigil

⭐ 15 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/Ju571nK/sigil) · [官网](https://sigilworks.net) · 个人维护

**扫描并评分 AI 编码代理配置的安全暴露面，支持车队级管理**

用 Rust 编写的本地客户端程序，读取 Claude Code、Codex、Cursor、Gemini CLI 等编码代理的权限、hooks、沙箱与 mcp.json 配置，对安全暴露面打分（如无沙箱、通配符 hook、空 deny 列表、指令文件中的提示注入），配置变更时即时重新评分。单机即可运行，无需账号、数据不出本机；车队模式下每台机器的客户端经 mTLS 向中央服务器发送哈希锚定事件，可接入 SIEM 并推送签名策略。默认只测量不阻断（阻断为可选且默认关闭）。作者自述为 alpha、单人维护。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 读取 7 种编码代理的权限/hooks/沙箱/MCP 配置并输出暴露面评分
- 配置变更即时重新评分，发现项含通配符 hook、空 deny 列表、提示注入等
- 车队模式：mTLS 哈希锚定事件上报、SIEM 接入、签名策略下发
- sigil-mcp 允许 AI 客户端经 MCP 读取自身风险评分

## 适用场景

- 检查本机 AI 编码代理配置是否存在危险权限或恶意 hook
- 多台机器无人值守运行编码代理时集中查看各主机风险
- 把代理配置风险事件接入 SIEM 做安全监控

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: skips its sandbox. Those decisions live in config files you never open. Sigil
> L98: A small Rust agent watches the config and posture files on each machine, hashes
> L100: `sigil-sender` ships those events over mTLS to `sigil-server`, which feeds your

## 星数曲线

```mermaid
xychart-beta
    title "Ju571nK/sigil 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-30"]
    y-axis "stars" 13 --> 16
    line [14, 15, 15]
```

2026-10-18 14 → 2026-10-30 15（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `0333016d9964` · [字段定义](../../DATASET.md)*
