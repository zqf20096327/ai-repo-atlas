# evanlong-me/nvidia-anthropic-proxy

⭐ 40 · JavaScript · MIT · 推送 2026-08-08 · [GitHub](https://github.com/evanlong-me/nvidia-anthropic-proxy) · 个人维护 · 中文 README

**让 Claude Code 使用 NVIDIA NIM 模型的 Cloudflare Worker 代理**

部署在 Cloudflare Workers 上的代理服务：将 Claude Code 发出的 Anthropic 格式请求转发到 NVIDIA NIM API，使用户可在 Claude Code 中调用 Llama、GLM、Minimax、DeepSeek 等模型，并映射 opus/sonnet/haiku 模型名。采用 pass-through 模式支持全部 NIM 模型，NVIDIA API Key 保存在用户自己的 Cloudflare 账户，无公共托管实例。通过 git clone 与 npm 脚本部署，配置 ~/.claude/settings.json 的 ANTHROPIC_BASE_URL 即可使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Cloudflare Worker 部署，经全球边缘网络低延迟访问
- pass-through 模式支持全部 NVIDIA NIM 模型
- API Key 保存在用户自己的 Cloudflare 账户，无公共托管实例
- 映射 opus/sonnet/haiku 到 NIM 模型名

## 适用场景

- 在 Claude Code 中使用 NVIDIA NIM 上的开源模型
- 自建代理掌控 API Key 而不依赖第三方托管
- 通过 /model 命令切换不同 NIM 模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: A Cloudflare Worker proxy that enables Claude Code to use NVIDIA NIM API models.
> L71: Claude Code (Anthropic format)
> L73: This Proxy (Cloudflare Worker)

## 星数曲线

```mermaid
xychart-beta
    title "evanlong-me/nvidia-anthropic-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-30 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `903d448dbd3a` · [字段定义](../../DATASET.md)*
