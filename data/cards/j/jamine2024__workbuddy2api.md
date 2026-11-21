# jamine2024/workbuddy2api

⭐ 3 · Go · NOASSERTION · 推送 2026-10-21 · [GitHub](https://github.com/jamine2024/workbuddy2api) · 个人维护 · 中文 README

**把 WorkBuddy 账号变为本地 OpenAI 兼容接口的 Windows 程序**

Windows 便携化封装：Go 网关提供 OpenAI 兼容的 /v1/models 与 /v1/chat/completions 接口（含 SSE 流式），多 WorkBuddy 账号轮转，上游返回 429/503 时自动改用同池其他账号；内置 Camoufox 指纹浏览器隔离各账号登录环境，并提供 opencode:/kilo: 前缀的免费匿名通道。Rust 控制面板收拢配置、账号与启停操作，悬浮窗每秒采样用量。数据全部留在本机。仅支持 Windows 10/11 x64，安装包约 178 MB 经 Release 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容接口，支持 SSE 流式与聚合 JSON
- 多账号池轮转与 429/503 自动故障转移
- 内置 Camoufox 指纹浏览器，账号登录环境互相隔离
- Rust 单文件控制面板与实时用量悬浮窗

## 适用场景

- 把 WorkBuddy 账号接入支持 OpenAI 接口的本地工具链
- 本地工具（如 OpenAI SDK 客户端）通过 base_url 指向本机网关调用
- 多账号轮转以分散单账号配额限制

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: 把 WorkBuddy 账号变成本地 OpenAI 兼容接口的 Windows 桌面程序：Rust 原生控制面板 + Go 网关 + 内置指纹浏览器，解压即用，不需要另装 Python 或 Go。
> L23: |**OpenAI 兼容**|`/v1/models`、`/v1/chat/completions`，支持 SSE 流式与聚合 JSON|

## 星数曲线

```mermaid
xychart-beta
    title "jamine2024/workbuddy2api 星数(近 2 点)"
    x-axis ["2026-11-01", "2026-11-21"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-01 3 → 2026-11-21 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `e4fad0d3eb9d` · [字段定义](../../DATASET.md)*
