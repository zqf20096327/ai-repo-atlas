# D3-vin/Qoder2Api

⭐ 25 · Go · MIT · 推送 2026-08-19 · [GitHub](https://github.com/D3-vin/Qoder2Api) · [官网](https://t.me/D3_vin) · 个人维护

**将 Qoder IDE 账号转为 OpenAI/Anthropic 兼容 API 的 Go 网关**

单个 Go 二进制实现的 HTTP 网关：把 Qoder IDE 账号（PAT）封装为 OpenAI 兼容接口（/v1/chat/completions、/v1/models、/v1/usage）与 Anthropic 兼容接口（/v1/messages），供 Claude Code 及任意 OpenAI 格式客户端调用。内置账号池，遇到 agent 限额错误（code 115）自动切换下一个 PAT；根路径提供嵌入式 HTML 仪表盘，管理账号、配额、默认模型与上下文/thinking 设置并持久化到 config.json。提供跨平台预编译二进制，也可从源码构建。声明仅供教育目的，用户需遵守第三方服务条款。

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

- 单二进制同时提供 OpenAI 与 Anthropic 兼容端点
- 多 PAT 账号池，限额错误自动故障转移
- 嵌入式仪表盘管理账号/配额/模型设置并持久化
- 运行时账户增删与配额刷新 API

## 适用场景

- 让 Claude Code 通过环境变量接入 Qoder 模型
- 把 Qoder 账号接入任意 OpenAI 格式客户端
- 多账号池化并用仪表盘监控配额

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: OpenAI & Anthropic-compatible gateway for Qoder IDE accounts — single Go binary with an account pool.
> L20: - 🔓 **OpenAI-compatible** — `/v1/chat/completions`, `/v1/models`, `/v1/usage`; drop-in for any OpenAI-format client

## 星数曲线

```mermaid
xychart-beta
    title "D3-vin/Qoder2Api 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-23 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `88138e0424df` · [字段定义](../../DATASET.md)*
