# codeaashu/grokbot-shim

⭐ 27 · JavaScript · ISC · 推送 2026-08-29 · [GitHub](https://github.com/codeaashu/grokbot-shim) · 个人维护

**让 Grok Bot 桌面代理在本地接入自选模型后端运行的垫片**

面向已安装 Grok Bot 桌面应用的 Linux 用户的本地运行时：从用户安装副本中提取宿主运行时文件，将应用的 Connect 协议推理请求解码后转发到可配置的模型提供方（Codex OAuth 的 ChatGPT 订阅会话或任意 OpenAI 兼容 /chat/completions 接口），并在同一机器上以 Docker 容器运行 Chrome/XFCE 计算机桌面，通过 noVNC 观看或接管。仓库不含应用二进制，依赖未公开的集成点，应用更新时可能需要随之更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | ISC |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 Grok Bot 的 Connect 协议推理流翻译到 Codex OAuth 或 OpenAI 兼容接口
- 本地 Docker 容器运行计算机桌面，noVNC 接管页仅绑定 127.0.0.1
- npm run setup 从已安装副本提取宿主运行时并生成本地 TLS 证书
- models.json 声明模型目录，API key 存于 .env，不入 Git

## 适用场景

- 用自有模型订阅在本地运行 Grok Bot 桌面代理
- 通过 noVNC 观看或接管代理操作的本地计算机桌面
- 为 Grok Bot 切换 OpenAI 兼容的模型后端

## 场景标签

`模型网关` `GUI 自动化` · 领域:Agent 开发

## 证据(README 行号)

> L6: The project connects the installed Grok Bot UI to its own local host runtime,
> L7: translates the app's inference protocol to supported model providers, and runs
> L108: - `openai-compatible` uses a streaming `/chat/completions` API;

## 星数曲线

```mermaid
xychart-beta
    title "codeaashu/grokbot-shim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-26 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `03135744e2ea` · [字段定义](../../DATASET.md)*
