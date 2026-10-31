# privapps/github-copilot-svcs

⭐ 61 · Go · Apache-2.0 · 推送 2026-09-29 · [GitHub](https://github.com/privapps/github-copilot-svcs) · 个人维护

**把 GitHub Copilot 服务代理为 OpenAI 兼容 API 的反向代理**

Go 编写的反向代理，通过 OpenCode 同款 OAuth 设备流认证 GitHub Copilot，对外暴露 /v1/chat/completions、/v1/responses、/v1/models 等 OpenAI 兼容端点，供期望 OpenAI API 的工具和客户端使用。内置令牌主动刷新（剩余 20% 生命周期时刷新）与指数退避重试、失败回退到完整重认证；支持 base64 图像的视觉请求（是否可用取决于 Copilot 订阅）、allowed_models 模型白名单过滤、断路器与请求合并、pprof 监控端点。提供 Linux/macOS/Windows 多平台预编译二进制与 Docker 镜像，也可从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OAuth 设备流认证与令牌主动刷新/退避重试/回退重认证
- 暴露 OpenAI 兼容端点并处理模型名映射与请求转换
- allowed_models 配置过滤可用模型，未列出模型请求返回 400
- 连接池、断路器、请求合并与 pprof 监控端点

## 适用场景

- 让仅支持 OpenAI API 的客户端接入 GitHub Copilot 订阅
- 在自托管环境中统一转发 Copilot 的聊天与视觉请求
- 通过 /health 与 pprof 端点监控代理服务运行状态

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: This project provides a reverse proxy for GitHub Copilot, exposing OpenAI-compatible endpoints for use with tools an
> L24: - **OpenAI-Compatible API**: Exposes `/v1/chat/completions`, `/v1/responses`, and `/v1/models` endpoints

## 星数曲线

```mermaid
xychart-beta
    title "privapps/github-copilot-svcs 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 60 --> 62
    line [61, 61]
```

2026-10-18 61 → 2026-10-31 61（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b9e125143b88` · [字段定义](../../DATASET.md)*
