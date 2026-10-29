# lipish/llm-connector

⭐ 20 · Rust · MIT · 推送 2026-05-07 · [GitHub](https://github.com/lipish/llm-connector) · [官网](https://llmconn.com) · 个人维护

**Rust 的 LLM 服务统一接入协议适配库**

面向 Rust 开发者的 LLM 协议适配层 crate：通过适配器模式将不同厂商 API 转换为统一内部接口，支持聊天、流式响应、OpenAI Responses API（不支持时自动回退到 /chat/completions）、推理模型（o1/o3、Claude 3.7）与文件上传（Base64 编码与 MIME 检测）。设计上零硬编码 URL，base_url 由使用者提供，无外部配置管理或数据库依赖。以 crates.io 发布，最低 Rust 版本 1.85+，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 适配器模式统一多厂商 LLM API 接口
- 零硬编码 URL，base_url 由用户提供
- OpenAI Responses API 不支持时自动回退 /chat/completions
- 推理模型与文件上传（自动 Base64/MIME 检测）支持

## 适用场景

- 在 Rust 项目中用统一接口调用不同 LLM 厂商
- 接入自建或非默认地址的 LLM 服务端点
- 构建支持流式输出与工具调用的聊天应用

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L16: `llm-connector` is a lightweight protocol adapter for connecting various LLM services. It handles protocol conversi
> L24: The `src/protocols/` module uses adapter pattern to convert different vendor APIs into unified internal interface:

## 星数曲线

```mermaid
xychart-beta
    title "lipish/llm-connector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `4c9b79be418b` · [字段定义](../../DATASET.md)*
