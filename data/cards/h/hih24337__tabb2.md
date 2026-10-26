# hih24337/tabb2

⭐ 55 · Python · 推送 2026-10-14 · [GitHub](https://github.com/hih24337/tabb2) · 个人维护 · 中文 README

**将 Tabbit 浏览器内部 API 转为 OpenAI/Claude 兼容接口的适配器**

非官方 API 适配器：把 Tabbit 浏览器的内部 API 封装为 OpenAI（/v1/chat/completions）与 Anthropic Claude（/v1/messages）两种兼容接口，使支持这两类 API 的第三方应用可对接 Tabbit 账户。内置多账户 Token 池轮询与故障冷却机制，提供 Web 管理面板（Token 管理、请求日志、配置修改），支持流式/非流式响应与 Claude 模式下的工具调用和 <thinking> 块。通过 Docker Compose 部署，配置经数据卷持久化。限制：依赖用户自有的 Tabbit Access Token，为非官方实现。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 同时提供 OpenAI 与 Anthropic Claude 两种兼容 API 端点
- 多账户 Token 池轮询负载均衡与连续出错冷却机制
- Web 管理面板：Token 增删改、实时请求日志、配置修改
- Claude 兼容模式支持 Tool Use 与 <thinking> 块

## 适用场景

- 让仅支持 OpenAI/Claude API 格式的应用接入 Tabbit 账户
- 用多个 Tabbit 账户 Token 做负载均衡提供服务
- 通过管理面板统一管理 Token 与查看请求日志

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L7: **Tabbit2API** 是一个非官方的 API 适配器，它将 Tabbit 浏览器 的内部 API 转换为与 OpenAI 和 Anthropic Claude 兼容的标准化接口。通过本项目，您可以将各种支持 OpenAI 或
> L11: - **双协议兼容**：同时支持 OpenAI (`/v1/chat/completions`) 和 Anthropic Claude (`/v1/messages`) 两种主流 API 格式。

## 星数曲线

```mermaid
xychart-beta
    title "hih24337/tabb2 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 53 --> 56
    line [54, 55, 55]
```

2026-10-18 54 → 2026-10-26 55（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `16ee0fbf1c67` · [字段定义](../../DATASET.md)*
