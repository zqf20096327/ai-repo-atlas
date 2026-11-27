# skyfiredao/opencode-cursor-proxy

⭐ 3 · Rust · GPL-3.0 · 推送 2026-11-20 · [GitHub](https://github.com/skyfiredao/opencode-cursor-proxy) · 个人维护 · 中文 README

**在 OpenCode 中使用 Cursor 模型的本地代理**

一个独立代理程序，通过 ACP 将 Cursor CLI 的对话以流式方式接入 OpenCode，并通过 MCP 桥接工具。启动时自动写入 OpenCode 的端点与模型列表配置（支持 V1/V2），每小时刷新模型列表且保留既有自定义并生成备份。另暴露 OpenAI 兼容的 HTTP 接口（/v1/chat/completions），仅支持文本输入与单响应，不支持图像、音频与采样参数。依赖已安装并登录的 Cursor CLI；兼容性不保证随官方 cursor-agent 更新持续有效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 ACP 将 Cursor 模型以流式方式接入 OpenCode，端点与模型列表自动配置
- 暴露 OpenAI 兼容 HTTP 接口，支持 Bearer 密码与会话延续
- 通过 MCP 桥接工具，支持 Plan/Build 模式切换与空回复恢复
- 提供 Linux/macOS/Windows 预编译包，配置变更自动生成 .bak 备份

## 适用场景

- 在 OpenCode 里以 Cursor 账号的模型配额进行编码对话
- 让 OpenCode 管理工具执行权限的同时使用 Cursor 模型
- 用任意 OpenAI 兼容客户端通过本地 HTTP 接口调用 Cursor 模型

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: Use Cursor models in OpenCode with streaming replies, tools, automatic connection setup and model-list updates.
> L126: OpenCode executes client-provided tools and controls their argument validation, permissions and retries. Cursor's 

## 星数曲线

```mermaid
xychart-beta
    title "skyfiredao/opencode-cursor-proxy 星数(近 2 点)"
    x-axis ["2026-11-13", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-13 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `8d654c7190b0` · [字段定义](../../DATASET.md)*
