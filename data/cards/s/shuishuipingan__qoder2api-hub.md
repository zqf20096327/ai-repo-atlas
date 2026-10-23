# shuishuipingan/qoder2api-hub

⭐ 341 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/shuishuipingan/qoder2api-hub) · [官网](https://qoder2api-hub-eybpg15659n.qoder.zone) · 个人维护 · 中文 README

**把 Qoder 双区多账号封装成 OpenAI/Anthropic 兼容接口的自托管网关**

用 Python 标准库实现的自托管代理网关：将 Qoder 国内版与国际版账号池封装为 OpenAI Chat Completions、Responses API（Codex）与 Anthropic Messages（Claude Code）三种兼容协议。面向在私有环境中使用自己合法授权账号的个人用户与开发者。机制包括账号轮询与会话亲和、COSY 签名、设备指纹对齐官方客户端形态、OAuth 设备授权登录、每日签到保活与 Web 监控看板。零第三方依赖，需 Python 3.9+，提供 amd64/arm64 Docker 镜像。项目自声明为非官方网关，仅供技术研究与个人使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种协议：OpenAI Chat Completions、Responses API、Anthropic Messages
- 国内/国际双区独立账号池，按模型自动选区，轮询与故障冷却换号
- 零依赖纯 Python 实现（COSY 签名、AES/RSA），提供 amd64/arm64 Docker 镜像
- Web 看板：账号、用量、请求流水与智能体一键配置

## 适用场景

- 让 Codex CLI、Claude Code 等 AI 编程客户端通过统一网关调用 Qoder 模型
- 多账号管理与轮询调度，配合每日签到与 Token 保活
- 在私有环境自托管部署并监控模型用量

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3:  把 Qoder 国内版（qoder.com.cn）与国际版（qoder.com）封装成 OpenAI / Anthropic 兼容接口的多账号网关
> L15: - **三种协议**：OpenAI Chat Completions、Responses API（Codex）、Anthropic Messages（Claude Code）

## 星数曲线

```mermaid
xychart-beta
    title "shuishuipingan/qoder2api-hub 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22", "2026-10-23"]
    y-axis "stars" 176 --> 356
    line [191, 233, 309, 341]
```

2026-10-18 191 → 2026-10-23 341（+150）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ebea3396b49c` · [字段定义](../../DATASET.md)*
