# turborg/turborg

⭐ 19 · Go · Apache-2.0 · 推送 2026-09-15 · [GitHub](https://github.com/turborg/turborg) · [官网](https://turborg.com) · 组织维护

**Go 单二进制 IRC 机器人框架：连接器+弹跳器+Web UI+可选 LLM**

用 Go 编写的聊天网络 agent 框架，编译为单个静态二进制、无运行时依赖。核心是 IRC 连接器（TLS/SASL/IRCv3）、内置 IRC bouncer（本地客户端经回环端口接入）与 WebSocket 网关及浏览器参考 UI；命令以数据定义（static 或 llm 类型），运行时从配置加载、无需重编译。LLM 为可选：默认 Anthropic，或任意 OpenAI 兼容端点，未设置时作为纯命令机器人运行。Discord/Telegram 连接器在路线图中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单静态二进制，无运行时依赖，含 IRC bouncer 与浏览器 UI
- 命令数据驱动：static/llm 类型，配置加载、免重编译
- LLM 可选：默认 Anthropic，支持任意 OpenAI 兼容端点
- 多架构 distroless Docker 镜像（amd64/arm64），覆盖率门槛 ≥94%

## 适用场景

- 部署常驻 IRC 频道机器人并配置命令
- 通过 bouncer 用 HexChat/irssi 等客户端接入自己的会话
- 在浏览器里通过 Web UI 查看/参与频道聊天
- 给机器人挂接 LLM 生成回答（可选）

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L20: - **Optional LLM, not the centerpiece** — point a command at an LLM (Anthropic, or any OpenAI-compatible endpoint v
> L132: LLM providers are **optional**. turborg runs perfectly fine as a pure command-driven bot without any LLM. When you

## 星数曲线

```mermaid
xychart-beta
    title "turborg/turborg 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-31"]
    y-axis "stars" 17 --> 20
    line [18, 19, 19]
```

2026-10-18 18 → 2026-10-31 19（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d36c5b48363f` · [字段定义](../../DATASET.md)*
